# Modern Python Data Science Bootcamp

A comprehensive, self-paced bootcamp delivered as interactive Marimo notebooks covering modern Python fundamentals, local data stack, and distributed computing.

## Overview

This bootcamp provides a structured pathway for staff and developers at the University of Idaho OIT to acquire modern data science skills. The content bridges local development with Polars and DuckDB to distributed computing with PySpark and Databricks.

### What You'll Learn

- **Module 0: Environment & Tooling** - Set up your development environment with Python 3.14+, UV, and modern tooling
- **Module 1: Modern Python** - Learn Python 3.14+ patterns, type hints, and professional coding practices
- **Module 2: Local Data Stack** - Master Polars and DuckDB for efficient local data analysis
- **Module 3: Data Acquisition** - Collect data from APIs, web scraping, and various sources
- **Module 4: Data Cleaning** - Clean and validate messy data with Pydantic and Pandera
- **Module 5: Feature Engineering** - Build reproducible data pipelines and engineer features
- **Module 6: Visualization** - Create effective visualizations to communicate insights
- **Module 7: Machine Learning** - Build classification models with scikit-learn
- **Module 8: Databricks** - Scale up to distributed computing with PySpark and Databricks

## Quick Start

### Prerequisites

- Python 3.14 or later
- [UV package manager](https://docs.astral.sh/uv/) installed
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ncolesummers/data-engineering-bootcamp.git
cd data-engineering-bootcamp
```

2. Set up the environment:
```bash
uv sync
```

3. Verify installation:
```bash
python -c "from bootcamp import __version__; print(__version__)"
```

You should see `0.1.0` printed to the console.

### Running Notebooks

Notebooks are delivered using [Marimo](https://marimo.io), a reactive Python notebook platform.

To run a notebook:
```bash
marimo edit notebooks/module_00_environment/00_01_welcome.py
```

## Repository Structure

```
data-engineering-bootcamp/
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Locked dependencies for reproducibility
├── README.md               # This file
├── docs/                   # Documentation and guides
│   ├── 01-curriculum-architecture.md
│   ├── 02-prd.md
│   ├── 03-premortem.md
│   └── 04-backlog-structure.md
├── src/
│   └── bootcamp/           # Python package for shared code
│       ├── datasets/       # Sample and synthetic datasets
│       ├── solutions/      # Exercise solutions
│       └── utils/          # Shared utilities
├── notebooks/              # Interactive Marimo notebooks
│   ├── module_00_environment/
│   ├── module_01_modern_python/
│   ├── module_02_local_data_stack/
│   ├── module_03_data_acquisition/
│   ├── module_04_data_cleaning/
│   ├── module_05_feature_engineering/
│   ├── module_06_visualization/
│   ├── module_07_machine_learning/
│   └── module_08_databricks/
└── tests/                  # Test files
```

## Getting Started with Learning

Start with **Module 0: Environment & Tooling** to set up your development environment and get familiar with the tools used throughout the bootcamp.

Each module builds on previous modules, so it's recommended to progress sequentially. However, experienced learners can skip ahead using the prerequisite information in each notebook's metadata.

## Documentation

- [Product Requirements Document](docs/02-prd.md) - Detailed specifications and requirements
- [Curriculum Architecture](docs/01-curriculum-architecture.md) - Learning objectives and structure
- [Backlog Structure](docs/04-backlog-structure.md) - GitHub issues and development tracking

## Contributing

This bootcamp is under active development. Contributions are welcome!

- Use the [Epic template](.github/ISSUE_TEMPLATE/epic.md) for major deliverable proposals
- Use the [User Story template](.github/ISSUE_TEMPLATE/user-story.md) for individual tasks or features

See the [GitHub Issues](https://github.com/ncolesummers/data-engineering-bootcamp/issues) for current development status.

## Technology Stack

- **Runtime:** Python 3.14+
- **Package Manager:** UV
- **Notebooks:** Marimo
- **DataFrames:** Polars
- **SQL Engine:** DuckDB
- **Validation:** Pydantic, Pandera
- **ML:** scikit-learn
- **Distributed:** PySpark (Databricks)

## License

MIT License - See LICENSE file for details.

## Contact

Nathan Summers - [nsummers72@gmail.com](mailto:nsummers72@gmail.com)

Project Link: [https://github.com/ncolesummers/data-engineering-bootcamp](https://github.com/ncolesummers/data-engineering-bootcamp)
