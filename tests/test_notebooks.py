"""Test suite for Marimo notebook execution.

This module provides automated testing of all Marimo notebooks in the notebooks/
directory, ensuring they execute without errors in CI/CD pipelines.
"""

import re
import subprocess
import time
from pathlib import Path
from typing import NamedTuple

import pytest


class NotebookResult(NamedTuple):
    """Result of notebook execution.

    Attributes:
        returncode: Exit code from notebook execution (0 = success)
        stdout: Standard output from notebook execution
        stderr: Standard error from notebook execution
        duration: Execution time in seconds
    """

    returncode: int
    stdout: str
    stderr: str
    duration: float


def discover_notebooks(root: Path = Path("notebooks")) -> list[Path]:
    """Discover all marimo notebooks in the notebooks directory.

    Args:
        root: Root directory to search for notebooks (default: notebooks/)

    Returns:
        List of notebook paths, sorted for consistent test order.
        Returns empty list if root directory doesn't exist.
    """
    if not root.exists():
        return []

    notebooks = sorted(root.rglob("*.py"))
    # Exclude __init__.py and other non-notebook files
    return [nb for nb in notebooks if nb.name != "__init__.py"]


def has_tag(notebook_path: Path, tag: str) -> bool:
    """Check if notebook has a specific tag in its docstring.

    Tags are specified in the notebook's module docstring using the format:
        Tags: tag1, tag2, tag3

    Args:
        notebook_path: Path to notebook file
        tag: Tag to search for (e.g., 'requires-databricks')

    Returns:
        True if tag is found in notebook's docstring Tags: line, False otherwise.
    """
    try:
        with open(notebook_path, encoding="utf-8") as f:
            # Read first 20 lines to find docstring
            lines = [f.readline() for _ in range(20)]
            content = "".join(lines)

            # Look for Tags: line in docstring
            match = re.search(r"Tags:\s*(.+)", content, re.IGNORECASE)
            if match:
                tags_line = match.group(1).strip()
                # Split by comma and check if tag is present
                tags = [t.strip() for t in tags_line.split(",")]
                return tag in tags
    except Exception:
        # If we can't read the file, don't skip it
        pass

    return False


def execute_notebook(notebook_path: Path, timeout_seconds: int = 600) -> NotebookResult:
    """Execute a marimo notebook using uvx marimo export html.

    This command runs the notebook and exports it to HTML, executing all cells
    and exiting with appropriate exit codes.

    Args:
        notebook_path: Path to the notebook to execute
        timeout_seconds: Maximum execution time in seconds (default: 600 = 10 minutes)

    Returns:
        NotebookResult with execution details including exit code, output, and duration.

    Note:
        If execution exceeds timeout, returns exit code -1 with timeout error message.
        HTML output is sent to /dev/null as we only care about execution success.
    """
    start_time = time.time()

    try:
        result = subprocess.run(
            ["uvx", "marimo", "export", "html", str(notebook_path), "-o", "/dev/null"],
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
            cwd=Path.cwd(),  # Ensure we run from repo root
        )
        duration = time.time() - start_time

        return NotebookResult(
            returncode=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
            duration=duration,
        )
    except subprocess.TimeoutExpired:
        duration = time.time() - start_time
        return NotebookResult(
            returncode=-1,
            stdout="",
            stderr=f"Notebook execution exceeded {timeout_seconds}s timeout",
            duration=duration,
        )


def get_notebook_params() -> list[Path]:
    """Get list of notebooks to test, excluding tagged notebooks.

    Returns:
        List of notebook paths that should be tested. Notebooks tagged with
        'requires-databricks' are excluded.
    """
    all_notebooks = discover_notebooks()

    # Filter out notebooks with requires-databricks tag
    notebooks = [nb for nb in all_notebooks if not has_tag(nb, "requires-databricks")]

    return notebooks


@pytest.mark.parametrize("notebook_path", get_notebook_params())
def test_notebook_execution(notebook_path: Path) -> None:
    """Test that a marimo notebook executes without errors.

    This test runs each discovered notebook and verifies it completes successfully.
    Failed executions will display the notebook path, exit code, duration, and
    full output for debugging.

    Args:
        notebook_path: Path to notebook to test (parametrized by pytest)
    """
    result = execute_notebook(notebook_path)

    # Build detailed error message if execution failed
    if result.returncode != 0:
        error_msg = f"""
Notebook execution failed: {notebook_path}
Exit code: {result.returncode}
Duration: {result.duration:.1f}s

Standard Output:
{result.stdout}

Standard Error:
{result.stderr}
"""
        pytest.fail(error_msg, pytrace=False)


def test_notebooks_exist() -> None:
    """Verify that at least one notebook exists (or skip if none found).

    This test ensures the notebook discovery mechanism is working. If no
    notebooks are found, the test is skipped rather than failed, allowing
    CI to pass during initial repository setup.
    """
    notebooks = discover_notebooks()

    if not notebooks:
        pytest.skip("No notebooks found in notebooks/ directory")

    assert len(notebooks) > 0, "Notebook discovery should find notebooks"
