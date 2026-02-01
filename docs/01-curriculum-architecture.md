# Modern Python Data Science Bootcamp
## Curriculum Architecture v1.0

### Overview

**Title:** Modern Python Data Science Bootcamp  
**Duration:** ~40 hours (designed for 1-2 week delivery)  
**Format:** Hybrid — instructor-led kickoffs with self-paced Marimo notebook progression  
**Platform:** Marimo notebooks (Python 3.14+)  

### Target Audience

| Audience | Profile | Entry Point |
|----------|---------|-------------|
| **Primary A** | OIT staff with little/no Python experience | Module 0 |
| **Primary B** | Developers new to data science | Module 0 (skim) or Module 2 |
| **Tertiary** | Faculty interested in AI-assisted content generation patterns | Meta-observation of project structure |

### Learning Outcomes

By completion, learners will be able to:

1. Set up and manage Python projects using modern tooling (uv, ruff, ty, pytest)
2. Write idiomatic Python 3.14+ code with proper typing and structure
3. Explore, clean, and transform data using Polars and DuckDB
4. Acquire data from APIs, databases, and web sources
5. Build reproducible data pipelines with validation
6. Create effective visualizations for data exploration and communication
7. Apply scikit-learn to build and evaluate prediction models
8. Transition local workflows to PySpark/Databricks at scale

---

## Module Structure

### Module 0: Environment & Tooling Foundation
**Duration:** 3 hours  
**Delivery:** Instructor-led setup session + self-paced exploration  

#### Learning Objectives
- Install and configure the Astral stack (uv, ruff, ty)
- Understand modern Python project structure
- Navigate and create Marimo notebooks
- Write and run basic pytest tests

#### Notebooks
| # | Title | Duration | Type |
|---|-------|----------|------|
| 0.1 | Welcome & Bootcamp Overview | 15 min | Orientation |
| 0.2 | Installing Python & UV | 30 min | Setup Guide |
| 0.3 | Project Structure & pyproject.toml | 30 min | Concept + Exercise |
| 0.4 | Introduction to Marimo | 45 min | Interactive Tutorial |
| 0.5 | Ruff: Linting & Formatting | 30 min | Concept + Exercise |
| 0.6 | Type Checking with ty | 20 min | Concept + Exercise |
| 0.7 | Testing with pytest | 30 min | Concept + Exercise |

#### Key Concepts
- Virtual environments and dependency management
- pyproject.toml configuration
- Pre-commit hooks and CI/CD integration concepts
- Test-driven development introduction

---

### Module 1: Modern Python Fundamentals
**Duration:** 5.5 hours  
**Delivery:** Self-paced with optional office hours  

#### Learning Objectives
- Write Python using 3.14+ idioms and features
- Apply type hints effectively throughout code
- Use dataclasses and Pydantic for data modeling
- Understand and apply pattern matching
- Validate data at runtime with Pydantic

#### Notebooks
| # | Title | Duration | Type |
|---|-------|----------|------|
| 1.1 | Python Syntax Refresher | 20 min | Tutorial (skippable for devs) |
| 1.2 | Type Hints Deep Dive | 45 min | Concept + Exercise |
| 1.3 | Generics and Protocols | 45 min | Concept + Exercise |
| 1.4 | Dataclasses & Attrs | 30 min | Concept + Exercise |
| 1.5 | Pydantic Fundamentals | 45 min | Concept + Exercise |
| 1.6 | Pydantic Deep Dive: Validators & Serialization | 45 min | Concept + Exercise |
| 1.7 | Pattern Matching (match/case) | 30 min | Concept + Exercise |
| 1.8 | Context Managers & Resource Handling | 30 min | Concept + Exercise |
| 1.9 | Iterators, Generators & Comprehensions | 45 min | Concept + Exercise |
| 1.10 | Error Handling Patterns | 30 min | Concept + Exercise |

#### Key Concepts
- PEP 695 type parameter syntax
- Structural subtyping with Protocol
- Exception groups and except*
- f-string debugging and formatting
- Pydantic BaseModel vs dataclasses (when to use which)
- Field validators, model validators, serialization aliases
- Pydantic Settings for configuration management

#### Assessment
- Mini-project: Build a typed data model for a university course catalog using Pydantic

---

### Module 2: Local Data Stack — Polars & DuckDB
**Duration:** 6 hours  
**Delivery:** Self-paced with mid-module check-in  

#### Learning Objectives
- Perform data manipulation with Polars expressions
- Query data using DuckDB's SQL interface
- Understand lazy vs eager evaluation
- Choose appropriate tools for different data tasks

#### Notebooks
| # | Title | Duration | Type |
|---|-------|----------|------|
| 2.1 | Why Polars? (Pandas Comparison) | 30 min | Concept |
| 2.2 | Polars Fundamentals: DataFrames & Series | 45 min | Tutorial |
| 2.3 | Polars Expressions & Method Chaining | 60 min | Concept + Exercise |
| 2.4 | Lazy Evaluation & Query Optimization | 45 min | Concept + Exercise |
| 2.5 | Introduction to DuckDB | 30 min | Tutorial |
| 2.6 | SQL in Python: DuckDB Patterns | 45 min | Concept + Exercise |
| 2.7 | Polars + DuckDB Integration | 30 min | Exercise |
| 2.8 | Working with Different File Formats | 45 min | Practical |

#### Key Concepts
- Expression API vs method chaining
- Predicate pushdown and projection pushdown
- Parquet, CSV, JSON handling
- When to use SQL vs DataFrame API

#### Assessment
- Exercise: Analyze a real dataset using both Polars and DuckDB approaches

---

### Module 3: Data Acquisition
**Duration:** 5.5 hours  
**Delivery:** Self-paced  

#### Learning Objectives
- Fetch data from REST APIs using httpx
- Validate API responses with Pydantic models
- Scrape web content ethically with Beautiful Soup
- Connect to databases (PostgreSQL, Oracle) for batch and streaming reads
- Handle authentication and rate limiting

#### Notebooks
| # | Title | Duration | Type |
|---|-------|----------|------|
| 3.1 | HTTP Fundamentals for Data Engineers | 30 min | Concept |
| 3.2 | httpx: Modern HTTP Client | 45 min | Tutorial + Exercise |
| 3.3 | Working with REST APIs | 60 min | Practical |
| 3.4 | Validating API Responses with Pydantic | 30 min | Concept + Exercise |
| 3.5 | API Authentication Patterns | 30 min | Concept + Exercise |
| 3.6 | Web Scraping with Beautiful Soup | 60 min | Tutorial + Exercise |
| 3.7 | Ethical Scraping & robots.txt | 20 min | Concept |
| 3.8 | Database Connections: Batch Reads | 45 min | Practical |
| 3.9 | Streaming Data from Databases | 30 min | Concept + Exercise |

#### Key Concepts
- Async HTTP patterns
- Request retry and backoff strategies
- Connection pooling
- Pagination handling

#### Assessment
- Project: Build a data collector that fetches from an API and stores locally

---

### Module 4: Data Cleaning & Preparation
**Duration:** 7.75 hours ⭐ (Heaviest module)  
**Delivery:** Instructor-led workshop + self-paced exercises  

#### Learning Objectives
- Identify and handle missing data appropriately
- Detect and treat outliers
- Normalize and standardize data
- Validate data quality with assertions and schemas

#### Notebooks
| # | Title | Duration | Type |
|---|-------|----------|------|
| 4.1 | The Anatomy of Dirty Data | 30 min | Concept (real examples) |
| 4.2 | Exploring Data Quality Issues | 45 min | Workshop |
| 4.3 | Missing Data: Detection & Strategies | 60 min | Concept + Exercise |
| 4.4 | Imputation Techniques | 45 min | Concept + Exercise |
| 4.5 | Outlier Detection & Treatment | 60 min | Concept + Exercise |
| 4.6 | Type Coercion & Parsing | 45 min | Practical |
| 4.7 | String Cleaning & Normalization | 45 min | Exercise |
| 4.8 | Date/Time Handling | 30 min | Practical |
| 4.9 | Row-Level Validation with Pydantic | 45 min | Concept + Exercise |
| 4.10 | DataFrame Validation with Pandera | 45 min | Concept + Exercise |
| 4.11 | Building a Cleaning Pipeline | 45 min | Capstone Exercise |

#### Key Concepts
- MCAR, MAR, MNAR missing data patterns
- IQR and Z-score outlier detection
- Unicode normalization
- Pydantic for record-level validation (parse/validate each row)
- Pandera for DataFrame-level schema validation (column types, constraints)
- When to use Pydantic vs Pandera vs both

#### Real-World Datasets
- Messy university enrollment data (synthetic)
- Public datasets with known quality issues

#### Assessment
- Capstone: Clean a provided "nightmare" dataset end-to-end

---

### Module 5: Feature Engineering & Pipelines
**Duration:** 4 hours  
**Delivery:** Self-paced  

#### Learning Objectives
- Create meaningful features from raw data
- Build reproducible transformation pipelines
- Implement feature stores concepts
- Version and track data transformations

#### Notebooks
| # | Title | Duration | Type |
|---|-------|----------|------|
| 5.1 | What is Feature Engineering? | 30 min | Concept |
| 5.2 | Numerical Feature Transformations | 45 min | Concept + Exercise |
| 5.3 | Categorical Encoding Strategies | 45 min | Concept + Exercise |
| 5.4 | Date/Time Feature Extraction | 30 min | Exercise |
| 5.5 | Text Feature Engineering Basics | 30 min | Concept |
| 5.6 | Building Reproducible Pipelines | 60 min | Concept + Exercise |
| 5.7 | Pipeline Testing & Validation | 30 min | Practical |

#### Key Concepts
- One-hot, ordinal, target encoding
- Binning and discretization
- Pipeline composition patterns
- Idempotency in data pipelines

---

### Module 6: Data Visualization
**Duration:** 3 hours  
**Delivery:** Self-paced with gallery review session  

#### Learning Objectives
- Choose appropriate visualizations for different data types
- Create publication-quality charts
- Build interactive visualizations in Marimo
- Apply visualization best practices

#### Notebooks
| # | Title | Duration | Type |
|---|-------|----------|------|
| 6.1 | Visualization Principles | 30 min | Concept |
| 6.2 | Exploratory vs Explanatory Viz | 20 min | Concept |
| 6.3 | Plotting with Marimo's Built-in Tools | 45 min | Tutorial |
| 6.4 | Statistical Visualizations | 45 min | Concept + Exercise |
| 6.5 | Interactive Dashboards in Marimo | 45 min | Practical |
| 6.6 | Visualization Anti-patterns | 15 min | Concept |

#### Key Concepts
- Grammar of graphics concepts
- Color theory for data
- Accessibility in visualization
- Marimo's reactive visualization model

---

### Module 7: Machine Learning with scikit-learn
**Duration:** 5 hours  
**Delivery:** Instructor-led intro + self-paced project work  

#### Learning Objectives
- Understand the ML workflow end-to-end
- Prepare data for machine learning
- Train and evaluate classification/regression models
- Avoid common ML pitfalls

#### Notebooks
| # | Title | Duration | Type |
|---|-------|----------|------|
| 7.1 | Machine Learning Fundamentals | 30 min | Concept |
| 7.2 | The scikit-learn API Pattern | 30 min | Tutorial |
| 7.3 | Train/Test Splits & Cross-Validation | 45 min | Concept + Exercise |
| 7.4 | Classification Models | 60 min | Concept + Exercise |
| 7.5 | Regression Models | 45 min | Concept + Exercise |
| 7.6 | Model Evaluation & Metrics | 45 min | Concept + Exercise |
| 7.7 | Hyperparameter Tuning | 30 min | Practical |
| 7.8 | Real-World Project: IT Ticket Classification | 60 min | Capstone |

#### Key Concepts
- Bias-variance tradeoff
- Feature scaling for ML
- Overfitting detection
- Model persistence
- Text classification fundamentals

#### Real-World Project: IT Ticket Classification
Build a classifier that predicts ticket categories from description text. This connects to real-world IT operations and demonstrates:
- Text preprocessing for ML
- TF-IDF or simple embeddings
- Multi-class classification
- Evaluation metrics for imbalanced classes
- Model interpretation basics

*Dataset: Synthetic IT ticket data modeled on TDX patterns*

---

### Module 8: Scaling to Databricks & PySpark
**Duration:** 4 hours  
**Delivery:** Instructor-led demo + guided exercises  

#### Learning Objectives
- Understand when to scale beyond single-machine tools
- Translate Polars knowledge to PySpark
- Navigate the Databricks environment
- Work with Delta Lake tables

#### Notebooks
| # | Title | Duration | Type |
|---|-------|----------|------|
| 8.1 | When to Scale: Decision Framework | 20 min | Concept |
| 8.2 | PySpark Fundamentals | 45 min | Tutorial |
| 8.3 | Polars to PySpark Translation Guide | 45 min | Reference + Exercise |
| 8.4 | Introduction to Databricks | 30 min | Demo |
| 8.5 | Delta Lake Basics | 45 min | Concept + Exercise |
| 8.6 | Databricks Workflows | 30 min | Practical |
| 8.7 | Medallion Architecture Overview | 25 min | Concept |

#### Key Concepts
- Spark execution model
- Partitioning strategies
- Delta Lake ACID transactions
- Unity Catalog basics

---

## Assessment Strategy

### Formative (Throughout)
- Embedded exercises in each notebook
- Self-check quizzes via Marimo interactions
- Code review checkpoints

### Summative
| Module | Assessment | Weight |
|--------|------------|--------|
| 1 | Mini-project: Typed data model | 10% |
| 2 | Dataset analysis exercise | 10% |
| 3 | Data collector project | 15% |
| 4 | Data cleaning capstone | 20% |
| 5-6 | Pipeline + visualization | 15% |
| 7 | ML prediction project | 20% |
| 8 | Databricks migration exercise | 10% |

---

## Technical Requirements

### Learner Environment
- Python 3.14+
- UV package manager
- VS Code or similar editor (Marimo extension)
- Git basics
- Access to Databricks workspace (Module 8)

### Dependencies (Core)
```toml
[project]
requires-python = ">=3.14"
dependencies = [
    "marimo>=0.10",
    "polars>=1.0",
    "duckdb>=1.0",
    "httpx>=0.27",
    "beautifulsoup4>=4.12",
    "pydantic>=2.10",
    "pydantic-settings>=2.6",
    "pandera>=0.20",
    "scikit-learn>=1.5",
    "pytest>=8.0",
]

[tool.uv]
dev-dependencies = [
    "ruff>=0.8",
    "ty>=0.1",
]
```

### Optional/Module-Specific
- `fastapi` (if serving examples needed)
- `pyspark` (Module 8, or Databricks-provided)
- Database drivers as needed (cx_Oracle, psycopg)

---

## Delivery Schedule Options

*Total curriculum: ~44 hours*

### Option A: Intensive (2 weeks, 4-4.5 hrs/day)
| Week | Days | Modules | Hours |
|------|------|---------|-------|
| 1 | Mon-Fri | 0, 1, 2, 3 | 20 |
| 2 | Mon-Fri | 4, 5, 6, 7, 8 | 24 |

### Option B: Extended (4 weeks, 2-2.5 hrs/day)
| Week | Modules | Hours |
|------|---------|-------|
| 1 | 0, 1 | 8.5 |
| 2 | 2, 3 | 11.5 |
| 3 | 4, 5 | 11.75 |
| 4 | 6, 7, 8 | 12 |

### Option C: Self-Paced
- Estimated 4-6 weeks at ~8-10 hrs/week
- Weekly optional office hours
- Cohort Slack/Discord for peer support

---

## Content Generation Notes

*For tertiary audience (faculty interested in AI-assisted content creation):*

This curriculum was developed using a structured approach:
1. **Scope definition** via iterative refinement
2. **PRD and Pre-mortem** for risk identification
3. **Agile backlog** as GitHub Issues (Epics → Stories)
4. **Marimo notebooks** generated by coding agents from story specifications
5. **Human review** and pedagogical refinement

Each notebook includes metadata for:
- Learning objectives (machine-readable)
- Prerequisite notebooks
- Estimated duration
- Assessment criteria

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-31 | Initial curriculum architecture |
