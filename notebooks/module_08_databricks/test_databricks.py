"""Test Databricks notebook - should be skipped in CI.

This notebook requires Databricks and should be excluded from CI execution.

Tags: requires-databricks
"""

import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


@app.cell
def __():
    # This would require Databricks environment
    from databricks import sql

    # Connection would fail without Databricks
    return


if __name__ == "__main__":
    app.run()
