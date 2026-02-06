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
#     "Identify your audience profile and recommended starting point.",
#     "Navigate the module sequence and estimated study time.",
#     "Understand the hybrid delivery model and schedule options.",
#     "Experience core Marimo interactions: reactivity, sliders, and layout elements.",
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
    mo.vstack(
        [
            mo.md(
                """
            # Welcome to the Modern Python Data Science Bootcamp

            You are about to work through a practical, notebook-first learning path
            that takes you from environment setup to production-scale data pipelines.
            """
            ),
            mo.hstack(
                [
                    mo.stat(value="9", label="Modules", caption="Setup to Databricks"),
                    mo.stat(value="~44h", label="Total Hours", caption="At your own pace"),
                    mo.stat(value="55+", label="Notebooks", caption="Interactive lessons"),
                ],
                justify="space-around",
                wrap=True,
            ),
            mo.callout(
                mo.md(f"{mo.icon('lucide:clock')} **15 minutes** | No exercises | Just explore"),
                kind="info",
            ),
        ]
    )
    return


@app.cell
def __(mo):
    audience_selector = mo.ui.radio(
        options={
            "I have little or no Python experience": "beginner",
            "I know Python but am new to data science": "developer",
            "I'm interested in the content creation approach": "observer",
        },
        label="Which best describes you?",
    )
    mo.vstack([mo.md("## Who Is This For?"), audience_selector])
    return (audience_selector,)


@app.cell
def __(audience_selector, mo):
    mo.stop(
        not audience_selector.value,
        mo.md("*Select an option above to see your recommended path.*"),
    )

    _guidance = {
        "beginner": (
            "Start at **Module 0** and work through everything in order. "
            "The pace is designed for you, and every concept builds on the last. "
            "You will have a solid data science foundation by the end."
        ),
        "developer": (
            "**Skim Modules 0 and 1** for tooling setup, then dive deep starting at "
            "**Module 2 (Polars & DuckDB)**. You will pick up the Python 3.14+ "
            "patterns quickly and can focus your time on the data stack."
        ),
        "observer": (
            "Explore the **repository structure** and the `docs/` folder to see how "
            "this curriculum was designed. The notebooks themselves demonstrate "
            "AI-assisted content generation patterns in action."
        ),
    }

    mo.callout(mo.md(_guidance[audience_selector.value]), kind="success")
    return


@app.cell
def __(mo):
    mo.vstack(
        [
            mo.md("## What You Will Learn"),
            mo.accordion(
                {
                    "Modern Python Tooling": mo.md(
                        "Set up and manage Python projects using **uv**, **ruff**, **ty**, "
                        "and **pytest**. You will learn the modern Astral-powered workflow "
                        "that replaces pip, black, mypy, and more. *(Module 0)*"
                    ),
                    "Idiomatic Python 3.14+": mo.md(
                        "Write clean Python with **type hints**, **Pydantic models**, "
                        "**pattern matching**, **generators**, and **structured error handling**. "
                        "*(Module 1)*"
                    ),
                    "Polars & DuckDB": mo.md(
                        "Explore, clean, and transform data using **Polars** DataFrames and "
                        "**DuckDB** SQL queries. Learn lazy evaluation and efficient file "
                        "format handling. *(Module 2)*"
                    ),
                    "Data Acquisition": mo.md(
                        "Pull data from **REST APIs** with httpx, query **databases**, "
                        "and scrape web sources. Build robust data ingestion workflows. "
                        "*(Module 3)*"
                    ),
                    "Data Cleaning & Preparation": mo.md(
                        "Handle **missing data**, detect **outliers**, coerce types, and "
                        "validate with **Pandera**. This is the largest module because "
                        "cleaning is where most real-world time goes. *(Module 4)*"
                    ),
                    "Feature Engineering & Pipelines": mo.md(
                        "Build **reproducible data pipelines** with transformations, "
                        "encoding, and validation steps that work end to end. *(Module 5)*"
                    ),
                    "Data Visualization": mo.md(
                        "Create effective visualizations for **exploration** and "
                        "**communication** using Marimo's built-in charting and interactive "
                        "dashboard capabilities. *(Module 6)*"
                    ),
                    "Machine Learning with scikit-learn": mo.md(
                        "Apply **scikit-learn** to build, evaluate, and tune prediction models. "
                        "Culminates in a capstone project classifying IT support tickets. "
                        "*(Module 7)*"
                    ),
                    "Scaling to Databricks & PySpark": mo.md(
                        "Transition local workflows to **PySpark** and **Databricks**. Learn "
                        "Delta Lake, the medallion architecture, and cloud-scale patterns. "
                        "*(Module 8)*"
                    ),
                },
                multiple=True,
            ),
        ]
    )
    return


@app.cell
def __(mo):
    module_tabs = mo.ui.tabs(
        {
            "Mod 0": mo.md(
                "**Environment & Tooling** | 3 hours\n\n"
                "- Install Python 3.14+ and UV package manager\n"
                "- Learn modern project structure and pyproject.toml\n"
                "- Get started with Marimo notebooks\n"
                "- Set up Ruff, ty, and pytest\n\n"
                "*Delivery: Instructor-led setup session + self-paced exploration*"
            ),
            "Mod 1": mo.md(
                "**Modern Python Fundamentals** | 5.5 hours\n\n"
                "- Type hints and Pydantic models\n"
                "- Pattern matching and structural types\n"
                "- Generators, itertools, and comprehensions\n"
                "- Error handling and logging\n\n"
                "*Delivery: Instructor kickoff + self-paced*"
            ),
            "Mod 2": mo.md(
                "**Local Data Stack** | 6 hours\n\n"
                "- Polars DataFrames and expressions\n"
                "- DuckDB SQL queries from Python\n"
                "- Lazy evaluation and query optimization\n"
                "- Parquet, CSV, and JSON file handling\n\n"
                "*Delivery: Instructor kickoff + self-paced*"
            ),
            "Mod 3": mo.md(
                "**Data Acquisition** | 5.5 hours\n\n"
                "- REST APIs with httpx\n"
                "- Database connections and queries\n"
                "- Web scraping fundamentals\n"
                "- Rate limiting and error recovery\n\n"
                "*Delivery: Self-paced with office hours support*"
            ),
            "Mod 4": mo.md(
                "**Data Cleaning & Preparation** | 7.75 hours\n\n"
                "- Missing data strategies\n"
                "- Outlier detection and handling\n"
                "- Type coercion and validation with Pandera\n"
                "- Data quality assessment\n\n"
                "*Delivery: Instructor checkpoint + self-paced*"
            ),
            "Mod 5": mo.md(
                "**Feature Engineering & Pipelines** | 4 hours\n\n"
                "- Feature transformations and encoding\n"
                "- Building reproducible pipeline steps\n"
                "- Pipeline validation and testing\n\n"
                "*Delivery: Self-paced with office hours support*"
            ),
            "Mod 6": mo.md(
                "**Data Visualization** | 3 hours\n\n"
                "- Exploratory data analysis charts\n"
                "- Statistical plots and distributions\n"
                "- Interactive dashboards in Marimo\n\n"
                "*Delivery: Self-paced with office hours support*"
            ),
            "Mod 7": mo.md(
                "**Machine Learning with scikit-learn** | 5 hours\n\n"
                "- ML workflow: train, evaluate, tune\n"
                "- Classification and regression models\n"
                "- Model evaluation and cross-validation\n"
                "- Capstone: IT ticket classification\n\n"
                "*Delivery: Instructor kickoff + self-paced*"
            ),
            "Mod 8": mo.md(
                "**Scaling to Databricks & PySpark** | 4 hours\n\n"
                "- PySpark fundamentals\n"
                "- Delta Lake and medallion architecture\n"
                "- Transitioning local workflows to the cloud\n\n"
                "*Delivery: Instructor-led walkthrough + self-paced*"
            ),
        }
    )
    mo.vstack([mo.md("## Module Roadmap"), module_tabs])
    return (module_tabs,)


@app.cell
def __(mo):
    schedule_selector = mo.ui.dropdown(
        options=[
            "Intensive (2 weeks)",
            "Extended (4 weeks)",
            "Self-Paced (4-6 weeks)",
        ],
        label="Which schedule works for you?",
    )
    mo.vstack([mo.md("## Choose Your Pace"), schedule_selector])
    return (schedule_selector,)


@app.cell
def __(mo, schedule_selector):
    mo.stop(
        not schedule_selector.value,
        mo.md("*Pick a schedule above to see the breakdown.*"),
    )

    _schedules = {
        "Intensive (2 weeks)": mo.md(
            "**4-4.5 hours per day, Monday through Friday**\n\n"
            "| Week | Modules | Hours |\n"
            "|------|---------|-------|\n"
            "| 1 | 0, 1, 2, 3 | 20 |\n"
            "| 2 | 4, 5, 6, 7, 8 | 24 |\n\n"
            "Best if you can dedicate focused time and want to finish quickly."
        ),
        "Extended (4 weeks)": mo.md(
            "**2-2.5 hours per day**\n\n"
            "| Week | Modules | Hours |\n"
            "|------|---------|-------|\n"
            "| 1 | 0, 1 | 8.5 |\n"
            "| 2 | 2, 3 | 11.5 |\n"
            "| 3 | 4, 5 | 11.75 |\n"
            "| 4 | 6, 7, 8 | 12 |\n\n"
            "Good balance of steady progress without overwhelming your schedule."
        ),
        "Self-Paced (4-6 weeks)": mo.md(
            "**~8-10 hours per week, on your schedule**\n\n"
            "- Work through modules at whatever pace suits you\n"
            "- Weekly optional office hours for questions\n"
            "- Cohort communication channel for peer support\n\n"
            "Maximum flexibility. You set the rhythm."
        ),
    }

    mo.callout(_schedules[schedule_selector.value], kind="neutral")
    return


@app.cell
def __(mo):
    demo_slider = mo.ui.slider(start=1, stop=10, value=5, label="Pick a number", show_value=True)
    mo.vstack(
        [
            mo.md(
                """
            ## How Marimo Works

            Marimo notebooks are **reactive**. Change an input, and everything
            downstream updates automatically. Try it yourself:
            """
            ),
            mo.callout(
                mo.md(
                    "- **Run cells** — each cell executes its Python code\n"
                    "- **Reactive** — move the slider below and watch the stats update\n"
                    "- **Save** — your notebook is a `.py` file, version it with git"
                ),
                kind="warn",
            ),
            demo_slider,
        ]
    )
    return (demo_slider,)


@app.cell
def __(demo_slider, mo):
    _n = demo_slider.value
    _squared = _n**2
    _cubed = _n**3

    mo.hstack(
        [
            mo.stat(value=str(_n), label="Your Number"),
            mo.stat(value=str(_squared), label="Squared", direction="increase"),
            mo.stat(value=str(_cubed), label="Cubed", direction="increase"),
        ],
        justify="space-around",
        wrap=True,
    )
    return


@app.cell
def __(mo):
    mo.vstack(
        [
            mo.md("## Quick Check"),
            mo.md("Think about each question, then expand to see the answer."),
            mo.accordion(
                {
                    "What happens when you move a slider in Marimo?": mo.md(
                        "All cells that **depend on that slider's value** re-execute "
                        "automatically. You saw this when the squared and cubed stats "
                        "updated above."
                    ),
                    "Where should you start if you already know Python?": mo.md(
                        "**Skim Modules 0 and 1** for tooling setup, then dive deep "
                        "starting at **Module 2** (Polars & DuckDB)."
                    ),
                    "How many total hours is the full bootcamp?": mo.md(
                        "About **44 hours** across 9 modules. You can spread this over "
                        "2 weeks (intensive) or 4-6 weeks (extended/self-paced)."
                    ),
                }
            ),
            mo.callout(
                mo.md("These are not graded. They are here to confirm you caught the key points."),
                kind="success",
            ),
        ]
    )
    return


@app.cell
def __(mo):
    mo.vstack(
        [
            mo.md("## Getting Help"),
            mo.hstack(
                [
                    mo.callout(
                        mo.md(
                            f"{mo.icon('lucide:calendar')} **Office Hours**\n\n"
                            "Drop-in sessions are held **[TBD: day/time]** via "
                            "**[TBD: platform]**.\n\n"
                            "Bring setup questions, concept clarifications, "
                            "or just come to work alongside others."
                        ),
                        kind="info",
                    ),
                    mo.callout(
                        mo.md(
                            f"{mo.icon('lucide:message-circle')} **Community Channel**\n\n"
                            "Join **[TBD: Slack/Discord channel]** for:\n"
                            "- Peer support and study groups\n"
                            "- Announcements and schedule changes\n"
                            "- Async Q&A with instructors"
                        ),
                        kind="info",
                    ),
                ],
                gap=2,
                wrap=True,
            ),
            mo.md("---"),
            mo.md("## Next Steps"),
            mo.md("Here is the full Module 0 sequence. You are on the first one."),
            mo.tree(
                {
                    "Module 0: Environment & Tooling": [
                        "0.1 Welcome & Bootcamp Overview (you are here)",
                        "0.2 Installing Python & UV",
                        "0.3 Project Structure & pyproject.toml",
                        "0.4 Introduction to Marimo",
                        "0.5 Ruff: Linting & Formatting",
                        "0.6 Type Checking with ty",
                        "0.7 Testing with pytest",
                    ]
                }
            ),
            mo.callout(
                mo.md(
                    f"{mo.icon('lucide:arrow-right')} **Continue to 0.2 Installing Python & UV.** "
                    "In the Marimo file browser, navigate to "
                    "`notebooks/module_00_environment/` and open "
                    "`00_02_installing_python_uv.py`."
                ),
                kind="success",
            ),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
