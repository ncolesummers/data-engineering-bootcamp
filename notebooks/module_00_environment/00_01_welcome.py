"""Welcome and bootcamp overview notebook for Module 0.

This orientation notebook introduces the bootcamp structure, learning outcomes,
and core Marimo usage patterns for beginners.
"""

# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo",
# ]
# [tool.bootcamp]
# module = "00"
# sequence = "01"
# title = "Welcome & Bootcamp Overview"
# duration_minutes = 15
# type = "orientation"
# prerequisites = []
# learning_objectives = [
#     "Understand the full bootcamp journey and expected outcomes.",
#     "Navigate the module sequence and estimated study time.",
#     "Understand the hybrid delivery model used in this program.",
#     "Use core Marimo actions: run cells, save notebooks, and reason about reactivity.",
# ]
# ///

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
        # Welcome to the Modern Python Data Science Bootcamp

        You are about to work through a practical, notebook-first learning path.
        This short orientation shows what you will learn, how the modules are
        organized, and how to work effectively in Marimo.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        """
        ## Bootcamp Learning Outcomes

        By completion, you will be able to:

        1. Set up and manage Python projects using modern tooling (uv, ruff, ty, pytest)
        2. Write idiomatic Python 3.14+ code with proper typing and structure
        3. Explore, clean, and transform data using Polars and DuckDB
        4. Acquire data from APIs, databases, and web sources
        5. Build reproducible data pipelines with validation
        6. Create effective visualizations for data exploration and communication
        7. Apply scikit-learn to build and evaluate prediction models
        8. Transition local workflows to PySpark/Databricks at scale
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        """
        ## Module Structure and Estimated Time

        | Module | Focus | Estimated Time |
        |---|---|---|
        | 0 | Environment and Tooling Foundation | 3 hours |
        | 1 | Modern Python Fundamentals | 5.5 hours |
        | 2 | Local Data Stack (Polars and DuckDB) | 6 hours |
        | 3 | Data Acquisition | 5.5 hours |
        | 4 | Data Cleaning and Preparation | 7.75 hours |
        | 5 | Feature Engineering and Pipelines | 4 hours |
        | 6 | Data Visualization | 3 hours |
        | 7 | Machine Learning with scikit-learn | 5 hours |
        | 8 | Scaling to Databricks and PySpark | 4 hours |
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        """
        ## How This Bootcamp Is Delivered

        This bootcamp uses a **hybrid format**:

        - Instructor-led kickoffs for key modules and checkpoints
        - Self-paced progression through Marimo notebooks between sessions

        In practice, you will get guided starts where it matters, then hands-on
        reps at your own pace using the same notebook workflow throughout.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        """
        ## Marimo Basics You Need Right Away

        - **Run cells:** Execute a cell to compute its results.
        - **Save notebooks:** Save your `.py` notebook file as you work.
        - **Reactive model:** When one cell changes, dependent cells update automatically.

        Think of Marimo like a reproducible program with interactive behavior.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        """
        ## Before You Continue

        This notebook is orientation only, so there are no exercises here.
        Continue to **0.2 Installing Python and UV** to begin environment setup.
        """
    )
    return


if __name__ == "__main__":
    app.run()
