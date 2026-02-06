"""Example test notebook for validating CI pipeline.

This simple notebook validates that the notebook execution test infrastructure
works correctly. It should execute successfully in CI without errors.
"""

import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo

    return (mo,)


@app.cell
def __(mo):
    mo.md(
        """
        # Test Notebook

        This is an example notebook used to validate the CI pipeline setup.
        """
    )
    return


@app.cell
def __():
    # Simple computation to verify execution
    result = 2 + 2
    assert result == 4, "Basic computation should work"
    return (result,)


@app.cell
def __(mo, result):
    mo.md(
        f"""
        ## Validation Results

        ✅ Test notebook executed successfully!

        Computation result: {result}
        """
    )
    return


if __name__ == "__main__":
    app.run()
