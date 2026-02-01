# GitHub Issues Backlog Structure
## Modern Python Data Science Bootcamp

**Repository:** `ncolesummers/data-engineering-bootcamp`  
**Last Updated:** 2025-01-31  

---

## Overview

This document defines the Epic → User Story hierarchy for implementation tracking. Each Epic represents a major deliverable area, and User Stories represent individual notebooks or infrastructure components.

### Hierarchy
```
Epic (GitHub Issue with "epic" label)
└── User Story (GitHub Issue with "story" label, linked as sub-issue)
    └── Acceptance Criteria (Checklist within story)
```

### Labels
| Label | Color | Purpose |
|-------|-------|---------|
| `epic` | `#7057ff` | Epic-level issues |
| `story` | `#0e8a16` | User story issues |
| `module-0` through `module-8` | `#c5def5` | Module identification |
| `mvp` | `#d93f0b` | Minimum viable scope |
| `content` | `#bfdadc` | Notebook content work |
| `infrastructure` | `#f9d0c4` | CI/CD, tooling work |
| `documentation` | `#fef2c0` | Docs and guides |

---

## Epic 0: Repository & Infrastructure Setup

**Description:** Establish the repository structure, CI/CD pipelines, and development tooling required before content creation begins.

**Labels:** `epic`, `infrastructure`, `mvp`

### Story 0.1: Initialize Repository Structure

**As a** contributor  
**I want** a well-organized repository structure  
**So that** content can be developed consistently and found easily  

**Acceptance Criteria:**
- [ ] Repository has directory structure matching PRD specification
- [ ] `pyproject.toml` configured with all core dependencies
- [ ] `uv.lock` generated and committed
- [ ] `.gitignore` includes Python, IDE, and OS-specific patterns
- [ ] `README.md` includes project overview and quick start
- [ ] `.github/ISSUE_TEMPLATE/` contains epic and story templates
- [ ] `src/bootcamp/` package structure created with `__init__.py`
- [ ] Empty module directories created under `notebooks/`

**Labels:** `story`, `infrastructure`, `mvp`

---

### Story 0.2: Configure CI/CD Pipeline

**As a** maintainer  
**I want** automated quality checks on every PR  
**So that** broken content doesn't reach learners  

**Acceptance Criteria:**
- [ ] GitHub Actions workflow runs on PR and push to main
- [ ] Ruff linting passes for all Python files
- [ ] Ruff formatting check passes
- [ ] ty type checking passes (or reports acceptable errors)
- [ ] pytest runs and passes
- [ ] Workflow fails fast on first error
- [ ] Status checks required for PR merge

**Labels:** `story`, `infrastructure`, `mvp`

---

### Story 0.3: Configure Notebook Execution Tests

**As a** maintainer  
**I want** notebooks automatically executed in CI  
**So that** I know all notebooks run without errors  

**Acceptance Criteria:**
- [ ] Separate workflow for notebook execution (can be slower)
- [ ] All notebooks in `notebooks/` directory execute successfully
- [ ] Execution tested on Python 3.14 (and 3.12 fallback)
- [ ] Workflow runs on PR and nightly schedule
- [ ] Execution timeout configured (10 min per notebook max)
- [ ] Failed notebook identified clearly in logs

**Labels:** `story`, `infrastructure`, `mvp`

---

### Story 0.4: Create Issue and PR Templates

**As a** contributor  
**I want** standardized templates for issues and PRs  
**So that** contributions are consistent and complete  

**Acceptance Criteria:**
- [ ] Epic issue template with fields: description, success criteria, child stories
- [ ] User story template with fields: user story format, acceptance criteria checklist
- [ ] Bug report template with fields: expected, actual, reproduction steps
- [ ] PR template with fields: related issue, changes, testing done, checklist

**Labels:** `story`, `infrastructure`

---

### Story 0.5: Set Up GitHub Projects Board

**As a** project manager  
**I want** a visual board tracking work status  
**So that** progress is visible at a glance  

**Acceptance Criteria:**
- [ ] GitHub Project created linked to repository
- [ ] Columns: Backlog, Ready, In Progress, Review, Done
- [ ] Automation: Issues move to "In Progress" when assigned
- [ ] Automation: Issues move to "Done" when closed
- [ ] Views: By module, by assignee, MVP only

**Labels:** `story`, `infrastructure`

---

## Epic 1: Module 0 - Environment & Tooling Foundation

**Description:** Create notebooks that guide learners through setting up their development environment with modern Python tooling.

**Labels:** `epic`, `module-0`, `content`, `mvp`

**Success Criteria:**
- Learner can install Python 3.14 and UV
- Learner can create and run Marimo notebooks
- Learner understands project structure and pyproject.toml
- Learner can run Ruff, ty, and pytest

---

### Story 1.1: Notebook 0.1 - Welcome & Bootcamp Overview

**As a** learner  
**I want** to understand what this bootcamp covers and how to navigate it  
**So that** I can plan my learning journey effectively  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Includes bootcamp learning objectives (all 8 from curriculum)
- [ ] Shows module structure with estimated times
- [ ] Explains hybrid delivery format
- [ ] Includes "how to use Marimo" basics (running cells, saving)
- [ ] Provides links to support resources (office hours, Slack/Discord)
- [ ] Duration metadata: 15 minutes
- [ ] Prerequisites metadata: none

**Labels:** `story`, `module-0`, `content`, `mvp`

---

### Story 1.2: Notebook 0.2 - Installing Python & UV

**As a** learner  
**I want** step-by-step instructions to install Python and UV  
**So that** I have the foundation for all other tools  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Instructions provided for Windows, macOS, and Linux
- [ ] Python 3.14 installation covered (with 3.12 fallback noted)
- [ ] UV installation via official installer
- [ ] Verification commands provided (`python --version`, `uv --version`)
- [ ] Common installation issues and solutions documented
- [ ] Explains why UV over pip/conda
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: none

**Labels:** `story`, `module-0`, `content`, `mvp`

---

### Story 1.3: Notebook 0.3 - Project Structure & pyproject.toml

**As a** learner  
**I want** to understand modern Python project structure  
**So that** I can organize my own projects professionally  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains src layout vs flat layout
- [ ] Walks through pyproject.toml sections: [project], [tool.*]
- [ ] Shows how to add/remove dependencies with UV
- [ ] Demonstrates `uv sync` and `uv run`
- [ ] Exercise: Modify pyproject.toml to add a dependency
- [ ] Exercise solution provided (hidden by default)
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 0.2

**Labels:** `story`, `module-0`, `content`, `mvp`

---

### Story 1.4: Notebook 0.4 - Introduction to Marimo

**As a** learner  
**I want** to become proficient with Marimo notebooks  
**So that** I can complete all bootcamp content effectively  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains reactive execution model (vs Jupyter)
- [ ] Covers cell types: Python, Markdown, SQL
- [ ] Demonstrates Marimo UI elements (sliders, dropdowns, tables)
- [ ] Shows how to save and export notebooks
- [ ] Exercise: Create an interactive element that filters data
- [ ] Compares Marimo to Jupyter for those familiar
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 0.2, 0.3

**Labels:** `story`, `module-0`, `content`, `mvp`

---

### Story 1.5: Notebook 0.5 - Ruff: Linting & Formatting

**As a** learner  
**I want** to use Ruff for code quality  
**So that** my code follows Python best practices  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains what linting and formatting are and why they matter
- [ ] Shows Ruff configuration in pyproject.toml
- [ ] Demonstrates `ruff check` and `ruff format`
- [ ] Covers common lint rules and how to fix violations
- [ ] Shows VS Code integration setup
- [ ] Exercise: Fix a file with intentional lint errors
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 0.3

**Labels:** `story`, `module-0`, `content`, `mvp`

---

### Story 1.6: Notebook 0.6 - Type Checking with ty

**As a** learner  
**I want** to understand static type checking  
**So that** I can catch errors before runtime  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains the value of static type checking
- [ ] Shows ty configuration in pyproject.toml
- [ ] Demonstrates running ty and interpreting output
- [ ] Covers common type errors and fixes
- [ ] Compares ty to mypy/pyright briefly
- [ ] Exercise: Add type hints to untyped functions
- [ ] Duration metadata: 20 minutes
- [ ] Prerequisites metadata: 0.3, 0.5

**Labels:** `story`, `module-0`, `content`, `mvp`

---

### Story 1.7: Notebook 0.7 - Testing with pytest

**As a** learner  
**I want** to write and run tests with pytest  
**So that** I can verify my code works correctly  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains test-driven development concept
- [ ] Shows pytest discovery and naming conventions
- [ ] Covers basic assertions and test structure
- [ ] Demonstrates fixtures (brief intro)
- [ ] Shows how to run tests: `uv run pytest`
- [ ] Exercise: Write tests for a provided function
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 0.3

**Labels:** `story`, `module-0`, `content`, `mvp`

---

## Epic 2: Module 1 - Modern Python Fundamentals

**Description:** Teach modern Python 3.14+ patterns including type hints, dataclasses, Pydantic, and pattern matching.

**Labels:** `epic`, `module-1`, `content`, `mvp`

**Success Criteria:**
- Learner writes idiomatic Python 3.14+ code
- Learner uses type hints effectively
- Learner chooses appropriately between dataclasses and Pydantic
- Learner applies pattern matching where beneficial

---

### Story 2.1: Notebook 1.1 - Python Syntax Refresher

**As a** learner new to Python  
**I want** a quick refresher on Python basics  
**So that** I have the foundation for advanced topics  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Marked as "skippable for experienced developers"
- [ ] Covers: variables, data types, control flow, functions
- [ ] Uses Python 3.14 syntax throughout (f-strings, walrus operator)
- [ ] Includes self-check quiz (5 questions)
- [ ] Duration metadata: 20 minutes
- [ ] Prerequisites metadata: 0.4

**Labels:** `story`, `module-1`, `content`, `mvp`

---

### Story 2.2: Notebook 1.2 - Type Hints Deep Dive

**As a** learner  
**I want** to master Python type hints  
**So that** I can write self-documenting, safer code  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers basic types: int, str, float, bool, None
- [ ] Covers container types: list, dict, set, tuple with generics
- [ ] Covers Optional, Union, and the `|` syntax
- [ ] Covers Callable and type aliases
- [ ] Shows PEP 695 type parameter syntax (`type` statement)
- [ ] Exercise: Add comprehensive type hints to a module
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 1.1 (optional), 0.6

**Labels:** `story`, `module-1`, `content`, `mvp`

---

### Story 2.3: Notebook 1.3 - Generics and Protocols

**As a** learner  
**I want** to understand generics and structural typing  
**So that** I can write flexible, reusable code  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains generic functions and classes
- [ ] Covers TypeVar and the new PEP 695 syntax
- [ ] Explains Protocol for structural subtyping
- [ ] Compares Protocol to ABC (when to use which)
- [ ] Exercise: Create a generic data container class
- [ ] Exercise: Define a Protocol and implement it
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 1.2

**Labels:** `story`, `module-1`, `content`, `mvp`

---

### Story 2.4: Notebook 1.4 - Dataclasses & Attrs

**As a** learner  
**I want** to understand dataclasses and attrs  
**So that** I can create clean data structures  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers @dataclass decorator and field options
- [ ] Shows frozen dataclasses for immutability
- [ ] Covers __post_init__ for validation/derived fields
- [ ] Brief introduction to attrs as alternative
- [ ] Explains when to use dataclass vs dict vs namedtuple
- [ ] Exercise: Model a university course as a dataclass
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 1.2

**Labels:** `story`, `module-1`, `content`, `mvp`

---

### Story 2.5: Notebook 1.5 - Pydantic Fundamentals

**As a** learner  
**I want** to use Pydantic for data validation  
**So that** I can ensure data integrity at runtime  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains Pydantic's purpose: validation + serialization
- [ ] Covers BaseModel creation and field types
- [ ] Shows automatic type coercion behavior
- [ ] Covers Field() for constraints (gt, lt, min_length, etc.)
- [ ] Demonstrates validation errors and handling
- [ ] Compares to dataclass: when to use which
- [ ] Exercise: Create a Pydantic model for student enrollment
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 1.4

**Labels:** `story`, `module-1`, `content`, `mvp`

---

### Story 2.6: Notebook 1.6 - Pydantic Deep Dive

**As a** learner  
**I want** to master advanced Pydantic features  
**So that** I can handle complex validation scenarios  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers field_validator and model_validator decorators
- [ ] Shows computed fields with @computed_field
- [ ] Demonstrates serialization aliases and exclude
- [ ] Covers model_dump() and model_dump_json()
- [ ] Introduces pydantic-settings for configuration
- [ ] Exercise: Build a config loader with pydantic-settings
- [ ] Exercise: Create a model with custom validators
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 1.5

**Labels:** `story`, `module-1`, `content`, `mvp`

---

### Story 2.7: Notebook 1.7 - Pattern Matching (match/case)

**As a** learner  
**I want** to use structural pattern matching  
**So that** I can write cleaner conditional logic  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains match/case syntax and semantics
- [ ] Covers literal patterns, capture patterns, wildcard
- [ ] Shows sequence and mapping patterns
- [ ] Demonstrates class patterns with dataclasses/Pydantic
- [ ] Covers guard clauses (if conditions)
- [ ] Compares to if/elif chains: when match is better
- [ ] Exercise: Refactor nested if/elif to match/case
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 1.4

**Labels:** `story`, `module-1`, `content`, `mvp`

---

### Story 2.8: Notebook 1.8 - Context Managers & Resource Handling

**As a** learner  
**I want** to manage resources safely with context managers  
**So that** I avoid resource leaks  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains the with statement and __enter__/__exit__
- [ ] Shows @contextmanager decorator for simple cases
- [ ] Covers ExitStack for multiple resources
- [ ] Demonstrates async context managers briefly
- [ ] Common use cases: files, connections, locks
- [ ] Exercise: Create a custom context manager for timing
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 1.2

**Labels:** `story`, `module-1`, `content`, `mvp`

---

### Story 2.9: Notebook 1.9 - Iterators, Generators & Comprehensions

**As a** learner  
**I want** to master Python's iteration patterns  
**So that** I can process data efficiently  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains iterator protocol (__iter__, __next__)
- [ ] Covers generator functions with yield
- [ ] Shows generator expressions vs list comprehensions
- [ ] Demonstrates memory efficiency of generators
- [ ] Covers dict and set comprehensions
- [ ] Introduces itertools highlights (chain, groupby, islice)
- [ ] Exercise: Convert a memory-heavy loop to a generator
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 1.2

**Labels:** `story`, `module-1`, `content`, `mvp`

---

### Story 2.10: Notebook 1.10 - Error Handling Patterns

**As a** learner  
**I want** to handle errors gracefully  
**So that** my programs are robust and debuggable  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers try/except/else/finally flow
- [ ] Shows creating custom exceptions
- [ ] Explains exception chaining (from e)
- [ ] Covers Python 3.11+ exception groups and except*
- [ ] Best practices: what to catch, when to re-raise
- [ ] Exercise: Add proper error handling to a data processing function
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 1.2

**Labels:** `story`, `module-1`, `content`, `mvp`

---

### Story 2.11: Module 1 Capstone - University Course Catalog Model

**As a** learner  
**I want** to apply Module 1 concepts in a realistic project  
**So that** I can demonstrate my understanding  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Project: Build a typed data model for course catalog
- [ ] Requires: Pydantic models for Course, Section, Instructor
- [ ] Requires: Custom validators (e.g., CRN format, credit range)
- [ ] Requires: Pattern matching for course categorization
- [ ] Requires: Generator for iterating large catalogs
- [ ] Includes rubric for self-assessment
- [ ] Duration metadata: 60 minutes
- [ ] Prerequisites metadata: 1.1-1.10

**Labels:** `story`, `module-1`, `content`, `mvp`

---

## Epic 3: Module 2 - Local Data Stack (Polars & DuckDB)

**Description:** Teach data manipulation with Polars and SQL queries with DuckDB for local data analysis.

**Labels:** `epic`, `module-2`, `content`, `mvp`

**Success Criteria:**
- Learner performs data transformations with Polars expressions
- Learner queries data with DuckDB SQL
- Learner understands lazy vs eager evaluation
- Learner works with multiple file formats

---

### Story 3.1: Notebook 2.1 - Why Polars?

**As a** learner  
**I want** to understand why Polars over Pandas  
**So that** I can make informed tooling choices  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains Polars design philosophy (Rust, Arrow, parallelism)
- [ ] Shows performance comparison with Pandas (concrete benchmark)
- [ ] Covers API differences at high level
- [ ] Discusses when Pandas might still be appropriate
- [ ] No exercises (conceptual notebook)
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 1.10

**Labels:** `story`, `module-2`, `content`, `mvp`

---

### Story 3.2: Notebook 2.2 - Polars Fundamentals

**As a** learner  
**I want** to learn basic Polars DataFrame operations  
**So that** I can start exploring data  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers DataFrame and Series creation
- [ ] Shows basic selection: select, filter, slice
- [ ] Demonstrates column operations: rename, drop, cast
- [ ] Covers basic aggregations: sum, mean, count, group_by
- [ ] Includes sample dataset for hands-on practice
- [ ] Exercise: Load and explore a CSV dataset
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 2.1

**Labels:** `story`, `module-2`, `content`, `mvp`

---

### Story 3.3: Notebook 2.3 - Polars Expressions & Method Chaining

**As a** learner  
**I want** to master Polars expression API  
**So that** I can write complex transformations cleanly  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains expression context (select vs filter vs with_columns)
- [ ] Shows pl.col(), pl.lit(), pl.when().then().otherwise()
- [ ] Covers string expressions: str.contains, str.extract, etc.
- [ ] Covers datetime expressions
- [ ] Demonstrates method chaining patterns
- [ ] Exercise: Transform a dataset with 5+ chained operations
- [ ] Duration metadata: 60 minutes
- [ ] Prerequisites metadata: 2.2

**Labels:** `story`, `module-2`, `content`, `mvp`

---

### Story 3.4: Notebook 2.4 - Lazy Evaluation & Query Optimization

**As a** learner  
**I want** to understand Polars lazy execution  
**So that** I can process large datasets efficiently  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains lazy vs eager DataFrames
- [ ] Shows .lazy() and .collect() workflow
- [ ] Demonstrates query plan visualization (explain())
- [ ] Covers predicate pushdown and projection pushdown
- [ ] Shows streaming mode for larger-than-memory data
- [ ] Exercise: Optimize an eager query using lazy evaluation
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 2.3

**Labels:** `story`, `module-2`, `content`, `mvp`

---

### Story 3.5: Notebook 2.5 - Introduction to DuckDB

**As a** learner  
**I want** to query data with SQL using DuckDB  
**So that** I can leverage SQL skills for analysis  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains DuckDB as embedded analytical database
- [ ] Shows basic SQL queries on CSV/Parquet files
- [ ] Covers DuckDB Python API basics
- [ ] Demonstrates querying without loading into memory
- [ ] Compares to SQLite (OLAP vs OLTP)
- [ ] Exercise: Write SQL queries against provided dataset
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 2.2

**Labels:** `story`, `module-2`, `content`, `mvp`

---

### Story 3.6: Notebook 2.6 - SQL in Python: DuckDB Patterns

**As a** learner  
**I want** to integrate DuckDB effectively in Python workflows  
**So that** I can combine SQL and Python strengths  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows parameterized queries (avoiding SQL injection)
- [ ] Covers registering Python objects as virtual tables
- [ ] Demonstrates CTEs and window functions
- [ ] Shows result conversion to Polars/Pandas
- [ ] Covers persistent vs in-memory databases
- [ ] Exercise: Build a multi-step analysis with CTEs
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 2.5

**Labels:** `story`, `module-2`, `content`, `mvp`

---

### Story 3.7: Notebook 2.7 - Polars + DuckDB Integration

**As a** learner  
**I want** to combine Polars and DuckDB seamlessly  
**So that** I can use the best tool for each task  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows zero-copy data sharing via Arrow
- [ ] Demonstrates SQL on Polars DataFrames
- [ ] Shows when to use SQL vs DataFrame API
- [ ] Covers mixed workflows: SQL for joins, Polars for transforms
- [ ] Exercise: Solve a problem using both tools
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 2.4, 2.6

**Labels:** `story`, `module-2`, `content`, `mvp`

---

### Story 3.8: Notebook 2.8 - Working with File Formats

**As a** learner  
**I want** to read and write various data formats  
**So that** I can work with real-world data sources  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers CSV: options for delimiters, headers, encoding
- [ ] Covers Parquet: compression, partitioning benefits
- [ ] Covers JSON and newline-delimited JSON
- [ ] Shows Excel reading (brief, not focus)
- [ ] Demonstrates format conversion workflows
- [ ] Exercise: Convert between formats with specific options
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 2.3

**Labels:** `story`, `module-2`, `content`, `mvp`

---

### Story 3.9: Module 2 Assessment - Dataset Analysis

**As a** learner  
**I want** to demonstrate my Polars and DuckDB skills  
**So that** I can confirm my understanding  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Provides a real-world dataset (e.g., public university data)
- [ ] Requires: Exploratory analysis with both Polars and DuckDB
- [ ] Requires: At least one lazy evaluation optimization
- [ ] Requires: File format conversion
- [ ] Includes analysis questions to answer
- [ ] Includes rubric for self-assessment
- [ ] Duration metadata: 60 minutes
- [ ] Prerequisites metadata: 2.1-2.8

**Labels:** `story`, `module-2`, `content`, `mvp`

---

## Epic 4: Module 3 - Data Acquisition

**Description:** Teach data collection from APIs, web scraping, and databases.

**Labels:** `epic`, `module-3`, `content`

**Success Criteria:**
- Learner fetches data from REST APIs with httpx
- Learner validates API responses with Pydantic
- Learner scrapes web content ethically
- Learner connects to databases for batch and streaming reads

---

### Story 4.1: Notebook 3.1 - HTTP Fundamentals for Data Engineers

**As a** learner  
**I want** to understand HTTP basics  
**So that** I can debug API integrations effectively  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers HTTP methods: GET, POST, PUT, DELETE
- [ ] Explains status codes: 2xx, 4xx, 5xx
- [ ] Covers headers: Content-Type, Authorization, Accept
- [ ] Explains request/response cycle
- [ ] No hands-on exercises (conceptual foundation)
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: none

**Labels:** `story`, `module-3`, `content`

---

### Story 4.2: Notebook 3.2 - httpx: Modern HTTP Client

**As a** learner  
**I want** to use httpx for HTTP requests  
**So that** I can fetch data from web services  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers basic GET and POST requests
- [ ] Shows query parameters and JSON bodies
- [ ] Demonstrates error handling with status codes
- [ ] Covers timeout configuration
- [ ] Shows httpx vs requests comparison
- [ ] Exercise: Fetch data from a public API
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 3.1

**Labels:** `story`, `module-3`, `content`

---

### Story 4.3: Notebook 3.3 - Working with REST APIs

**As a** learner  
**I want** to interact with real REST APIs  
**So that** I can collect external data  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Works with a real public API (e.g., GitHub, weather, data.gov)
- [ ] Covers pagination handling patterns
- [ ] Shows rate limiting and retry logic
- [ ] Demonstrates async requests with httpx (brief)
- [ ] Exercise: Build a data collector that handles pagination
- [ ] Duration metadata: 60 minutes
- [ ] Prerequisites metadata: 3.2

**Labels:** `story`, `module-3`, `content`

---

### Story 4.4: Notebook 3.4 - Validating API Responses with Pydantic

**As a** learner  
**I want** to validate API responses automatically  
**So that** I catch data issues early  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows Pydantic model for API response
- [ ] Demonstrates parsing with model_validate()
- [ ] Covers handling optional/nullable fields from APIs
- [ ] Shows error handling for validation failures
- [ ] Covers nested models for complex responses
- [ ] Exercise: Create Pydantic models for a real API
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 1.5, 3.3

**Labels:** `story`, `module-3`, `content`

---

### Story 4.5: Notebook 3.5 - API Authentication Patterns

**As a** learner  
**I want** to authenticate with protected APIs  
**So that** I can access restricted data sources  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers API keys (header and query parameter)
- [ ] Covers Bearer token authentication
- [ ] Introduces OAuth2 flow conceptually
- [ ] Shows secure credential handling (environment variables)
- [ ] Exercise: Authenticate with a protected API
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 3.2

**Labels:** `story`, `module-3`, `content`

---

### Story 4.6: Notebook 3.6 - Web Scraping with Beautiful Soup

**As a** learner  
**I want** to extract data from web pages  
**So that** I can collect data not available via APIs  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers Beautiful Soup basics: parsing, navigating DOM
- [ ] Shows finding elements: find, find_all, select (CSS)
- [ ] Demonstrates text extraction and cleaning
- [ ] Covers handling tables specifically
- [ ] Shows combining httpx + BeautifulSoup workflow
- [ ] Exercise: Scrape a table from a public website
- [ ] Duration metadata: 60 minutes
- [ ] Prerequisites metadata: 3.2

**Labels:** `story`, `module-3`, `content`

---

### Story 4.7: Notebook 3.7 - Ethical Scraping & robots.txt

**As a** learner  
**I want** to understand web scraping ethics and limits  
**So that** I scrape responsibly  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains robots.txt and how to parse it
- [ ] Covers rate limiting and being a good citizen
- [ ] Discusses legal considerations (brief, not legal advice)
- [ ] Shows User-Agent best practices
- [ ] Covers when NOT to scrape (ToS, legal restrictions)
- [ ] No hands-on exercises (ethics/policy focus)
- [ ] Duration metadata: 20 minutes
- [ ] Prerequisites metadata: 3.6

**Labels:** `story`, `module-3`, `content`

---

### Story 4.8: Notebook 3.8 - Database Connections: Batch Reads

**As a** learner  
**I want** to read data from databases  
**So that** I can work with enterprise data sources  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers connection strings and configuration
- [ ] Shows reading with SQLAlchemy or direct drivers
- [ ] Demonstrates Polars read_database() function
- [ ] Covers connection pooling basics
- [ ] Shows reading large tables in chunks
- [ ] Uses DuckDB as example database (self-contained)
- [ ] Exercise: Query and transform database data
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 2.5

**Labels:** `story`, `module-3`, `content`

---

### Story 4.9: Notebook 3.9 - Streaming Data from Databases

**As a** learner  
**I want** to process database data in a streaming fashion  
**So that** I can handle tables too large for memory  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains streaming vs batch read tradeoffs
- [ ] Shows cursor-based iteration pattern
- [ ] Demonstrates Polars lazy scan with databases
- [ ] Covers incremental loading with watermarks
- [ ] Introduces change data capture (CDC) concept
- [ ] Exercise: Process a large table in streaming fashion
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 3.8

**Labels:** `story`, `module-3`, `content`

---

### Story 4.10: Module 3 Project - Data Collector

**As a** learner  
**I want** to build a complete data collection pipeline  
**So that** I can demonstrate data acquisition skills  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Project: Build a collector that fetches from an API
- [ ] Requires: Pydantic validation of responses
- [ ] Requires: Pagination handling
- [ ] Requires: Error handling and retries
- [ ] Requires: Save to Parquet format
- [ ] Includes rubric for self-assessment
- [ ] Duration metadata: 60 minutes
- [ ] Prerequisites metadata: 3.1-3.9

**Labels:** `story`, `module-3`, `content`

---

## Epic 5: Module 4 - Data Cleaning & Preparation

**Description:** Deep dive into cleaning messy data, handling missing values, and validating data quality.

**Labels:** `epic`, `module-4`, `content`, `mvp`

**Success Criteria:**
- Learner identifies and handles missing data appropriately
- Learner detects and treats outliers
- Learner normalizes and validates data
- Learner builds reproducible cleaning pipelines

---

### Story 5.1: Notebook 4.1 - The Anatomy of Dirty Data

**As a** learner  
**I want** to recognize common data quality issues  
**So that** I know what to look for when exploring new data  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows real examples of dirty data (anonymized)
- [ ] Categorizes issues: missing, inconsistent, invalid, duplicate
- [ ] Demonstrates impact of dirty data on analysis
- [ ] Introduces data quality dimensions
- [ ] No exercises (eye-opening examples focus)
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 2.3

**Labels:** `story`, `module-4`, `content`, `mvp`

---

### Story 5.2: Notebook 4.2 - Exploring Data Quality Issues

**As a** learner  
**I want** systematic techniques to assess data quality  
**So that** I can create a cleaning plan  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows profiling techniques: null counts, unique counts, distributions
- [ ] Demonstrates Polars describe() and null_count()
- [ ] Covers detecting duplicates
- [ ] Shows visualization for quality assessment
- [ ] Provides a data quality checklist template
- [ ] Exercise: Profile a messy dataset and document issues
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 4.1

**Labels:** `story`, `module-4`, `content`, `mvp`

---

### Story 5.3: Notebook 4.3 - Missing Data: Detection & Strategies

**As a** learner  
**I want** to handle missing data appropriately  
**So that** I don't introduce bias into my analysis  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains MCAR, MAR, MNAR patterns
- [ ] Shows detection patterns in Polars
- [ ] Covers deletion strategies: listwise, pairwise
- [ ] Discusses when deletion is appropriate
- [ ] Shows visualization of missingness patterns
- [ ] Exercise: Analyze and document missing data patterns
- [ ] Duration metadata: 60 minutes
- [ ] Prerequisites metadata: 4.2

**Labels:** `story`, `module-4`, `content`, `mvp`

---

### Story 5.4: Notebook 4.4 - Imputation Techniques

**As a** learner  
**I want** to fill missing values appropriately  
**So that** I preserve data while minimizing bias  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers mean/median/mode imputation and limitations
- [ ] Shows forward/backward fill for time series
- [ ] Introduces interpolation techniques
- [ ] Covers group-wise imputation
- [ ] Discusses imputation with ML (brief mention, not deep)
- [ ] Shows flagging imputed values
- [ ] Exercise: Apply multiple imputation strategies and compare
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 4.3

**Labels:** `story`, `module-4`, `content`, `mvp`

---

### Story 5.5: Notebook 4.5 - Outlier Detection & Treatment

**As a** learner  
**I want** to identify and handle outliers  
**So that** they don't skew my analysis  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers statistical methods: IQR, Z-score
- [ ] Shows visualization: box plots, scatter plots
- [ ] Discusses domain knowledge for outlier identification
- [ ] Covers treatment options: remove, cap, transform
- [ ] Explains when outliers are valuable signal
- [ ] Exercise: Detect and treat outliers in a dataset
- [ ] Duration metadata: 60 minutes
- [ ] Prerequisites metadata: 4.2

**Labels:** `story`, `module-4`, `content`, `mvp`

---

### Story 5.6: Notebook 4.6 - Type Coercion & Parsing

**As a** learner  
**I want** to convert data types correctly  
**So that** I can work with properly typed data  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers string to numeric conversion with error handling
- [ ] Shows parsing numbers with different formats (currency, percentages)
- [ ] Demonstrates boolean coercion from various representations
- [ ] Covers handling mixed-type columns
- [ ] Shows Polars cast() with strict and non-strict modes
- [ ] Exercise: Clean a column with mixed types
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 4.2

**Labels:** `story`, `module-4`, `content`, `mvp`

---

### Story 5.7: Notebook 4.7 - String Cleaning & Normalization

**As a** learner  
**I want** to clean and normalize text data  
**So that** string comparisons and joins work correctly  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers whitespace handling: trim, collapse
- [ ] Shows case normalization
- [ ] Covers Unicode normalization (NFC, NFKC)
- [ ] Demonstrates regex for pattern extraction/cleaning
- [ ] Shows standardizing formats (names, addresses)
- [ ] Exercise: Normalize a column of messy names
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 4.2

**Labels:** `story`, `module-4`, `content`, `mvp`

---

### Story 5.8: Notebook 4.8 - Date/Time Handling

**As a** learner  
**I want** to parse and normalize date/time data  
**So that** temporal analysis is accurate  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers parsing various date formats
- [ ] Shows timezone handling and conversion
- [ ] Demonstrates handling ambiguous dates (MM/DD vs DD/MM)
- [ ] Covers date arithmetic and differences
- [ ] Shows Polars temporal functions
- [ ] Exercise: Parse and normalize a column with mixed date formats
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 4.6

**Labels:** `story`, `module-4`, `content`, `mvp`

---

### Story 5.9: Notebook 4.9 - Row-Level Validation with Pydantic

**As a** learner  
**I want** to validate individual records with Pydantic  
**So that** I catch invalid data early  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows Pydantic model for row validation
- [ ] Demonstrates validating DataFrame rows
- [ ] Covers collecting and reporting validation errors
- [ ] Shows filtering valid vs invalid records
- [ ] Compares to Polars native validation
- [ ] Exercise: Validate a dataset and separate valid/invalid rows
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 1.5, 4.2

**Labels:** `story`, `module-4`, `content`, `mvp`

---

### Story 5.10: Notebook 4.10 - DataFrame Validation with Pandera

**As a** learner  
**I want** to validate DataFrames with schema definitions  
**So that** I can enforce data contracts  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Introduces Pandera for DataFrame validation
- [ ] Shows schema definition: column types, constraints
- [ ] Covers custom checks and hypothesis testing
- [ ] Demonstrates schema decorators for functions
- [ ] Compares Pydantic (row) vs Pandera (DataFrame) use cases
- [ ] Exercise: Define and apply a Pandera schema
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 4.9

**Labels:** `story`, `module-4`, `content`, `mvp`

---

### Story 5.11: Notebook 4.11 - Building a Cleaning Pipeline

**As a** learner  
**I want** to compose cleaning steps into a reproducible pipeline  
**So that** I can apply the same cleaning to new data  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows function composition for cleaning steps
- [ ] Demonstrates Polars pipe() method
- [ ] Covers logging and auditing transformations
- [ ] Shows testing cleaning functions
- [ ] Discusses idempotency in cleaning pipelines
- [ ] Exercise: Build a multi-step cleaning pipeline
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 4.3-4.10

**Labels:** `story`, `module-4`, `content`, `mvp`

---

### Story 5.12: Module 4 Capstone - Clean the Nightmare Dataset

**As a** learner  
**I want** to demonstrate end-to-end data cleaning skills  
**So that** I can prove my competency  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Provides intentionally messy "nightmare" dataset
- [ ] Dataset has: missing data, outliers, type issues, encoding problems
- [ ] Requires: Document all quality issues found
- [ ] Requires: Apply appropriate cleaning techniques
- [ ] Requires: Validate cleaned output with Pydantic or Pandera
- [ ] Requires: Build reproducible pipeline
- [ ] Includes detailed rubric
- [ ] Duration metadata: 90 minutes
- [ ] Prerequisites metadata: 4.1-4.11

**Labels:** `story`, `module-4`, `content`, `mvp`

---

## Epic 6: Module 5 - Feature Engineering & Pipelines

**Description:** Teach feature creation strategies and reproducible pipeline construction.

**Labels:** `epic`, `module-5`, `content`

**Success Criteria:**
- Learner creates meaningful features from raw data
- Learner builds reproducible transformation pipelines
- Learner tests and validates pipelines

---

### Story 6.1: Notebook 5.1 - What is Feature Engineering?

**As a** learner  
**I want** to understand feature engineering concepts  
**So that** I know how to improve model inputs  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains features vs raw data
- [ ] Shows examples of effective feature engineering
- [ ] Discusses feature engineering for ML vs analytics
- [ ] Introduces feature stores concept
- [ ] No exercises (conceptual)
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 4.11

**Labels:** `story`, `module-5`, `content`

---

### Story 6.2: Notebook 5.2 - Numerical Feature Transformations

**As a** learner  
**I want** to transform numerical features effectively  
**So that** they work better for analysis and ML  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers scaling: standardization, min-max, robust
- [ ] Shows log and power transforms for skewed data
- [ ] Demonstrates polynomial features
- [ ] Covers binning/discretization
- [ ] Shows when to apply which transformation
- [ ] Exercise: Transform features and compare distributions
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 5.1

**Labels:** `story`, `module-5`, `content`

---

### Story 6.3: Notebook 5.3 - Categorical Encoding Strategies

**As a** learner  
**I want** to encode categorical variables properly  
**So that** they can be used in numerical analysis  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers one-hot encoding with handling high cardinality
- [ ] Shows ordinal encoding and when appropriate
- [ ] Introduces target encoding (with caveats)
- [ ] Covers frequency encoding
- [ ] Discusses handling unseen categories
- [ ] Exercise: Encode categorical features multiple ways
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 5.1

**Labels:** `story`, `module-5`, `content`

---

### Story 6.4: Notebook 5.4 - Date/Time Feature Extraction

**As a** learner  
**I want** to extract useful features from timestamps  
**So that** I capture temporal patterns  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows extracting: year, month, day, weekday, hour
- [ ] Covers cyclical encoding (sin/cos for circular features)
- [ ] Demonstrates time since events
- [ ] Shows holiday and business day features
- [ ] Exercise: Engineer time features from timestamp column
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 4.8

**Labels:** `story`, `module-5`, `content`

---

### Story 6.5: Notebook 5.5 - Text Feature Engineering Basics

**As a** learner  
**I want** to create features from text data  
**So that** I can use text in analysis  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers basic text features: length, word count, character patterns
- [ ] Introduces TF-IDF conceptually (detailed in ML module)
- [ ] Shows extracting structured info from text (regex)
- [ ] Demonstrates sentiment indicators (simple rules-based)
- [ ] Exercise: Create features from IT ticket descriptions
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 5.1

**Labels:** `story`, `module-5`, `content`

---

### Story 6.6: Notebook 5.6 - Building Reproducible Pipelines

**As a** learner  
**I want** to compose transformations into pipelines  
**So that** I can apply them consistently  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows function composition patterns
- [ ] Demonstrates sklearn Pipeline (preview for ML module)
- [ ] Covers Polars pipe() for DataFrame transforms
- [ ] Shows parameterized pipelines
- [ ] Covers Pydantic for pipeline input/output contracts
- [ ] Exercise: Build a feature engineering pipeline
- [ ] Duration metadata: 60 minutes
- [ ] Prerequisites metadata: 5.2-5.5

**Labels:** `story`, `module-5`, `content`

---

### Story 6.7: Notebook 5.7 - Pipeline Testing & Validation

**As a** learner  
**I want** to test my data pipelines  
**So that** I catch errors before production  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows unit testing pipeline functions
- [ ] Covers property-based testing with hypothesis (brief)
- [ ] Demonstrates schema validation in pipelines
- [ ] Shows testing with sample data
- [ ] Covers pipeline monitoring concepts
- [ ] Exercise: Write tests for a pipeline function
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 0.7, 5.6

**Labels:** `story`, `module-5`, `content`

---

## Epic 7: Module 6 - Data Visualization

**Description:** Teach effective data visualization for exploration and communication.

**Labels:** `epic`, `module-6`, `content`

**Success Criteria:**
- Learner chooses appropriate visualizations
- Learner creates interactive Marimo visualizations
- Learner applies visualization best practices

---

### Story 7.1: Notebook 6.1 - Visualization Principles

**As a** learner  
**I want** to understand visualization fundamentals  
**So that** I create effective charts  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers Tufte's principles of graphical excellence
- [ ] Shows chart type selection guide
- [ ] Discusses color theory basics
- [ ] Covers accessibility considerations
- [ ] No exercises (conceptual)
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 2.3

**Labels:** `story`, `module-6`, `content`

---

### Story 7.2: Notebook 6.2 - Exploratory vs Explanatory Viz

**As a** learner  
**I want** to distinguish exploration from presentation  
**So that** I use the right approach for my goal  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Defines exploratory visualization (for analyst)
- [ ] Defines explanatory visualization (for audience)
- [ ] Shows examples of each with same data
- [ ] Discusses iteration from exploration to presentation
- [ ] No exercises (conceptual)
- [ ] Duration metadata: 20 minutes
- [ ] Prerequisites metadata: 6.1

**Labels:** `story`, `module-6`, `content`

---

### Story 7.3: Notebook 6.3 - Plotting with Marimo

**As a** learner  
**I want** to create visualizations in Marimo  
**So that** I can explore data interactively  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows Marimo's native plotting capabilities
- [ ] Covers integrating matplotlib/altair/plotly
- [ ] Demonstrates reactive updates with UI elements
- [ ] Shows chart from DataFrame patterns
- [ ] Exercise: Create an interactive exploration dashboard
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 0.4, 2.3

**Labels:** `story`, `module-6`, `content`

---

### Story 7.4: Notebook 6.4 - Statistical Visualizations

**As a** learner  
**I want** to visualize statistical properties  
**So that** I understand data distributions  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers histograms and density plots
- [ ] Shows box plots and violin plots
- [ ] Demonstrates scatter plots with regression lines
- [ ] Covers correlation heatmaps
- [ ] Shows pair plots for multivariate exploration
- [ ] Exercise: Create statistical summary visualizations
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 6.3

**Labels:** `story`, `module-6`, `content`

---

### Story 7.5: Notebook 6.5 - Interactive Dashboards in Marimo

**As a** learner  
**I want** to build interactive dashboards  
**So that** users can explore data themselves  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows multi-chart dashboard layout
- [ ] Demonstrates linked filtering across charts
- [ ] Covers Marimo UI elements for user input
- [ ] Shows reactive data updates
- [ ] Exercise: Build a dashboard for the bootcamp dataset
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 6.3

**Labels:** `story`, `module-6`, `content`

---

### Story 7.6: Notebook 6.6 - Visualization Anti-patterns

**As a** learner  
**I want** to recognize bad visualization practices  
**So that** I avoid misleading charts  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows truncated axes and why they mislead
- [ ] Covers 3D charts problems
- [ ] Demonstrates dual-axis dangers
- [ ] Shows overplotting issues
- [ ] Covers chartjunk and decoration excess
- [ ] No exercises (gallery of anti-patterns)
- [ ] Duration metadata: 15 minutes
- [ ] Prerequisites metadata: 6.1

**Labels:** `story`, `module-6`, `content`

---

## Epic 8: Module 7 - Machine Learning with scikit-learn

**Description:** Teach the ML workflow from data preparation through model evaluation with a real-world classification project.

**Labels:** `epic`, `module-7`, `content`, `mvp`

**Success Criteria:**
- Learner understands end-to-end ML workflow
- Learner prepares data for machine learning
- Learner builds and evaluates classification models
- Learner completes IT ticket classification project

---

### Story 8.1: Notebook 7.1 - Machine Learning Fundamentals

**As a** learner  
**I want** to understand ML concepts  
**So that** I have the foundation for building models  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Defines supervised vs unsupervised learning
- [ ] Explains classification vs regression
- [ ] Covers the ML workflow: train, validate, test
- [ ] Introduces bias-variance tradeoff
- [ ] Discusses overfitting and underfitting
- [ ] No exercises (conceptual foundation)
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 5.6

**Labels:** `story`, `module-7`, `content`, `mvp`

---

### Story 8.2: Notebook 7.2 - The scikit-learn API Pattern

**As a** learner  
**I want** to understand sklearn's consistent API  
**So that** I can use any model easily  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains fit/predict/transform pattern
- [ ] Shows estimators, transformers, predictors
- [ ] Demonstrates Pipeline for chaining
- [ ] Covers ColumnTransformer for mixed data
- [ ] Exercise: Build a simple pipeline
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 7.1

**Labels:** `story`, `module-7`, `content`, `mvp`

---

### Story 8.3: Notebook 7.3 - Train/Test Splits & Cross-Validation

**As a** learner  
**I want** to evaluate models properly  
**So that** I don't fool myself with overfitting  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows train_test_split with stratification
- [ ] Explains why holdout set matters
- [ ] Covers k-fold cross-validation
- [ ] Shows stratified k-fold for imbalanced data
- [ ] Demonstrates cross_val_score usage
- [ ] Exercise: Compare holdout vs cross-validation results
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 7.2

**Labels:** `story`, `module-7`, `content`, `mvp`

---

### Story 8.4: Notebook 7.4 - Classification Models

**As a** learner  
**I want** to build classification models  
**So that** I can predict categorical outcomes  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers Logistic Regression with interpretation
- [ ] Shows Decision Trees with visualization
- [ ] Introduces Random Forest as ensemble
- [ ] Demonstrates model training and prediction
- [ ] Compares model characteristics
- [ ] Exercise: Train multiple classifiers on same data
- [ ] Duration metadata: 60 minutes
- [ ] Prerequisites metadata: 7.3

**Labels:** `story`, `module-7`, `content`, `mvp`

---

### Story 8.5: Notebook 7.5 - Regression Models

**As a** learner  
**I want** to build regression models  
**So that** I can predict numerical outcomes  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers Linear Regression with interpretation
- [ ] Shows Ridge and Lasso regularization
- [ ] Introduces Random Forest regressor
- [ ] Demonstrates prediction and residual analysis
- [ ] Exercise: Build a regression model
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 7.3

**Labels:** `story`, `module-7`, `content`, `mvp`

---

### Story 8.6: Notebook 7.6 - Model Evaluation & Metrics

**As a** learner  
**I want** to evaluate models with appropriate metrics  
**So that** I choose the best model  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Covers classification: accuracy, precision, recall, F1
- [ ] Shows confusion matrix visualization
- [ ] Explains ROC curves and AUC
- [ ] Covers regression: MSE, RMSE, MAE, R²
- [ ] Discusses choosing metrics for business context
- [ ] Exercise: Evaluate a model with multiple metrics
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 7.4

**Labels:** `story`, `module-7`, `content`, `mvp`

---

### Story 8.7: Notebook 7.7 - Hyperparameter Tuning

**As a** learner  
**I want** to optimize model hyperparameters  
**So that** I get better performance  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains hyperparameters vs learned parameters
- [ ] Shows GridSearchCV usage
- [ ] Demonstrates RandomizedSearchCV for efficiency
- [ ] Covers common hyperparameters per model
- [ ] Discusses avoiding overfitting during tuning
- [ ] Exercise: Tune a model's hyperparameters
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 7.6

**Labels:** `story`, `module-7`, `content`, `mvp`

---

### Story 8.8: Module 7 Capstone - IT Ticket Classification

**As a** learner  
**I want** to build a real-world classification system  
**So that** I can demonstrate ML competency  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Uses synthetic IT ticket dataset (10K records)
- [ ] Requires: Exploratory data analysis
- [ ] Requires: Text feature engineering (TF-IDF)
- [ ] Requires: Handle class imbalance
- [ ] Requires: Train and compare multiple classifiers
- [ ] Requires: Proper evaluation with appropriate metrics
- [ ] Requires: Model interpretation (feature importance)
- [ ] Includes detailed rubric
- [ ] Duration metadata: 90 minutes
- [ ] Prerequisites metadata: 7.1-7.7

**Labels:** `story`, `module-7`, `content`, `mvp`

---

## Epic 9: Module 8 - Scaling to Databricks & PySpark

**Description:** Teach the transition from local tools to distributed computing with PySpark and Databricks.

**Labels:** `epic`, `module-8`, `content`

**Success Criteria:**
- Learner understands when to scale beyond single machine
- Learner translates Polars knowledge to PySpark
- Learner navigates Databricks environment
- Learner works with Delta Lake tables

---

### Story 9.1: Notebook 8.1 - When to Scale: Decision Framework

**As a** learner  
**I want** to know when distributed computing is needed  
**So that** I don't over-engineer or under-engineer solutions  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Provides decision framework: data size, complexity, latency
- [ ] Discusses costs of distributed systems
- [ ] Shows where Polars/DuckDB limits are
- [ ] Covers "scale up vs scale out" decision
- [ ] No exercises (decision framework)
- [ ] Duration metadata: 20 minutes
- [ ] Prerequisites metadata: 2.4

**Labels:** `story`, `module-8`, `content`

---

### Story 9.2: Notebook 8.2 - PySpark Fundamentals

**As a** learner  
**I want** to learn PySpark basics  
**So that** I can work with large datasets  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains Spark architecture (driver, executors)
- [ ] Shows SparkSession creation
- [ ] Covers DataFrame basics: select, filter, groupBy
- [ ] Demonstrates lazy evaluation and actions
- [ ] Shows reading/writing Parquet
- [ ] Exercise: Basic PySpark data manipulation
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 8.1

**Labels:** `story`, `module-8`, `content`

---

### Story 9.3: Notebook 8.3 - Polars to PySpark Translation Guide

**As a** learner  
**I want** a reference for translating Polars to PySpark  
**So that** I can apply my Polars knowledge  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Side-by-side comparison of common operations
- [ ] Covers: select, filter, group_by, join, window functions
- [ ] Highlights API differences and gotchas
- [ ] Shows performance considerations
- [ ] Exercise: Translate a Polars pipeline to PySpark
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 2.4, 8.2

**Labels:** `story`, `module-8`, `content`

---

### Story 9.4: Notebook 8.4 - Introduction to Databricks

**As a** learner  
**I want** to navigate the Databricks environment  
**So that** I can use it for data work  

**Acceptance Criteria:**
- [ ] Notebook executes without errors (Databricks export)
- [ ] Shows Databricks workspace navigation
- [ ] Covers notebook creation and execution
- [ ] Demonstrates cluster attachment
- [ ] Shows file browser and data upload
- [ ] Covers Databricks-specific magic commands
- [ ] No exercises (demo/walkthrough)
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 8.2

**Labels:** `story`, `module-8`, `content`

---

### Story 9.5: Notebook 8.5 - Delta Lake Basics

**As a** learner  
**I want** to work with Delta Lake tables  
**So that** I get ACID transactions on data lakes  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains Delta Lake benefits over raw Parquet
- [ ] Shows creating and writing Delta tables
- [ ] Covers MERGE (upsert) operations
- [ ] Demonstrates time travel queries
- [ ] Shows schema evolution
- [ ] Exercise: Create and update a Delta table
- [ ] Duration metadata: 45 minutes
- [ ] Prerequisites metadata: 8.4

**Labels:** `story`, `module-8`, `content`

---

### Story 9.6: Notebook 8.6 - Databricks Workflows

**As a** learner  
**I want** to orchestrate jobs in Databricks  
**So that** I can run pipelines on a schedule  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Shows creating a Databricks Job
- [ ] Covers scheduling options
- [ ] Demonstrates notebook parameters
- [ ] Shows monitoring job runs
- [ ] Brief mention of Databricks Workflows (orchestration)
- [ ] Exercise: Create a scheduled job
- [ ] Duration metadata: 30 minutes
- [ ] Prerequisites metadata: 8.4

**Labels:** `story`, `module-8`, `content`

---

### Story 9.7: Notebook 8.7 - Medallion Architecture Overview

**As a** learner  
**I want** to understand the medallion architecture  
**So that** I can organize data lakes properly  

**Acceptance Criteria:**
- [ ] Notebook executes without errors
- [ ] Explains bronze/silver/gold layers
- [ ] Shows example transformations at each layer
- [ ] Discusses data quality gates between layers
- [ ] Covers Unity Catalog briefly
- [ ] No exercises (architecture overview)
- [ ] Duration metadata: 25 minutes
- [ ] Prerequisites metadata: 8.5

**Labels:** `story`, `module-8`, `content`

---

## Epic 10: Synthetic Datasets

**Description:** Create the synthetic datasets required for exercises and capstones.

**Labels:** `epic`, `infrastructure`, `mvp`

**Success Criteria:**
- IT ticket dataset ready for ML capstone
- Nightmare dataset ready for cleaning capstone
- Sample datasets for each module

---

### Story 10.1: Create IT Ticket Classification Dataset

**As a** content creator  
**I want** a realistic synthetic IT ticket dataset  
**So that** the ML capstone has appropriate data  

**Acceptance Criteria:**
- [ ] Dataset has ~10,000 records
- [ ] Fields: ticket_id, created_date, category, priority, description, resolution_time
- [ ] Categories: ~15 categories modeled on TDX taxonomy
- [ ] Descriptions: Realistic text (varied length, terminology)
- [ ] Class imbalance: Some categories much more common
- [ ] Missing values: ~5% in resolution_time
- [ ] Dataset saved as Parquet in `src/bootcamp/datasets/`
- [ ] Generation script included and reproducible

**Labels:** `story`, `infrastructure`, `mvp`

---

### Story 10.2: Create Nightmare Cleaning Dataset

**As a** content creator  
**I want** an intentionally messy dataset  
**So that** learners can practice cleaning skills  

**Acceptance Criteria:**
- [ ] Dataset has ~5,000 records
- [ ] Based on university enrollment data concept
- [ ] Issues included: multiple missing data patterns (MCAR, MAR)
- [ ] Issues included: outliers (obvious and subtle)
- [ ] Issues included: encoding problems (mixed UTF-8)
- [ ] Issues included: type mismatches (numbers as strings)
- [ ] Issues included: inconsistent formats (dates, names)
- [ ] Issues included: duplicates (exact and fuzzy)
- [ ] Documented "ground truth" for expected clean output
- [ ] Dataset saved in `src/bootcamp/datasets/`

**Labels:** `story`, `infrastructure`, `mvp`

---

### Story 10.3: Create Module Sample Datasets

**As a** content creator  
**I want** sample datasets for each module  
**So that** exercises have consistent data  

**Acceptance Criteria:**
- [ ] Module 2: Clean dataset for Polars/DuckDB exploration
- [ ] Module 3: API response samples for validation exercises
- [ ] Module 5: Dataset suitable for feature engineering
- [ ] Module 6: Dataset with good visualization potential
- [ ] All datasets documented with data dictionary
- [ ] Datasets sized appropriately (<10MB each)

**Labels:** `story`, `infrastructure`

---

## Epic 11: Documentation

**Description:** Create instructor guides, learner guides, and assessment rubrics.

**Labels:** `epic`, `documentation`

**Success Criteria:**
- Instructors can facilitate the bootcamp effectively
- Learners can self-navigate the content
- Assessments have clear, fair rubrics

---

### Story 11.1: Create Learner Quick Start Guide

**As a** learner  
**I want** a clear guide to get started  
**So that** I can begin learning quickly  

**Acceptance Criteria:**
- [ ] Single page (or very short) overview
- [ ] Prerequisites listed clearly
- [ ] Step-by-step environment setup
- [ ] How to navigate the modules
- [ ] Where to get help (office hours, Slack)
- [ ] Located at `docs/learner-guide.md`

**Labels:** `story`, `documentation`, `mvp`

---

### Story 11.2: Create Instructor Facilitation Guide

**As an** instructor  
**I want** guidance on facilitating the bootcamp  
**So that** I can deliver effectively  

**Acceptance Criteria:**
- [ ] Suggested delivery schedules (2-week, 4-week)
- [ ] Per-module facilitation notes
- [ ] Common learner questions and answers
- [ ] Troubleshooting guide for setup issues
- [ ] Tips for live sessions
- [ ] Located at `docs/instructor-guide.md`

**Labels:** `story`, `documentation`

---

### Story 11.3: Create Assessment Rubrics

**As an** instructor  
**I want** rubrics for capstone projects  
**So that** I can evaluate fairly  

**Acceptance Criteria:**
- [ ] Rubric for Module 1 capstone (Course Catalog Model)
- [ ] Rubric for Module 2 assessment (Dataset Analysis)
- [ ] Rubric for Module 3 project (Data Collector)
- [ ] Rubric for Module 4 capstone (Nightmare Dataset)
- [ ] Rubric for Module 7 capstone (IT Ticket Classification)
- [ ] Each rubric has: criteria, levels, point values
- [ ] Located in `docs/assessment-rubrics/`

**Labels:** `story`, `documentation`, `mvp`

---

### Story 11.4: Create Troubleshooting FAQ

**As a** learner  
**I want** solutions to common problems  
**So that** I can unblock myself quickly  

**Acceptance Criteria:**
- [ ] Windows-specific issues (UV, Python path)
- [ ] Mac-specific issues (permissions, Xcode)
- [ ] Linux-specific issues (system Python conflicts)
- [ ] Marimo-specific issues
- [ ] Notebook execution errors
- [ ] Located at `docs/troubleshooting.md`

**Labels:** `story`, `documentation`, `mvp`

---

## Summary Statistics

| Epic | Stories | MVP Stories | Estimated Hours |
|------|---------|-------------|-----------------|
| Epic 0: Infrastructure | 5 | 3 | 8 |
| Epic 1: Module 0 | 7 | 7 | 3 |
| Epic 2: Module 1 | 11 | 11 | 5.5 |
| Epic 3: Module 2 | 9 | 9 | 6 |
| Epic 4: Module 3 | 10 | 0 | 5.5 |
| Epic 5: Module 4 | 12 | 12 | 7.75 |
| Epic 6: Module 5 | 7 | 0 | 4 |
| Epic 7: Module 6 | 6 | 0 | 3 |
| Epic 8: Module 7 | 8 | 8 | 5 |
| Epic 9: Module 8 | 7 | 0 | 4 |
| Epic 10: Datasets | 3 | 2 | 6 |
| Epic 11: Documentation | 4 | 3 | 4 |
| **Total** | **89** | **55** | **~62** |

*Note: Hours are development hours, not learner hours.*
