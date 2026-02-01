# Product Requirements Document (PRD)
## Modern Python Data Science Bootcamp

**Document Version:** 1.0  
**Last Updated:** 2025-01-31  
**Owner:** Nate (Enterprise Applications Developer, University of Idaho OIT)  
**Status:** Draft

---

## 1. Executive Summary

### 1.1 Problem Statement

The University of Idaho OIT has staff and developers who need modern data science skills but lack a structured pathway to acquire them. Existing resources are either:
- Too academic (theory-heavy, disconnected from tooling reality)
- Outdated (teaching Pandas patterns when Polars exists, Python 3.8 idioms)
- Fragmented (no cohesive journey from fundamentals to production)

Additionally, the organization is investing in Azure Databricks infrastructure, requiring staff to bridge local development skills to distributed computing environments.

### 1.2 Proposed Solution

A comprehensive, self-paced bootcamp delivered as interactive Marimo notebooks covering:
- Modern Python (3.14+) fundamentals with proper typing
- Local data stack (Polars, DuckDB) for exploration and analysis
- Data acquisition, cleaning, and pipeline development
- Machine learning fundamentals with scikit-learn
- Transition to PySpark/Databricks for scale

### 1.3 Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Completion rate | ≥70% of enrolled learners | Tracking notebook progression |
| Competency assessment | ≥80% pass rate on capstone projects | Rubric-based evaluation |
| Time to completion | ≤6 weeks for self-paced learners | Timestamp tracking |
| Learner satisfaction | ≥4.2/5.0 | Post-bootcamp survey |
| Skill application | ≥50% apply skills within 3 months | Follow-up survey |

---

## 2. Background & Context

### 2.1 Current State

- OIT staff have varying Python proficiency levels
- Data work is often done in Excel or legacy tools
- No standardized training path for data skills
- Databricks investment underutilized due to skill gaps
- AI/ML initiatives require foundational data literacy

### 2.2 Strategic Alignment

This bootcamp supports:
- **OIT AI Literacy Initiative**: Foundation for understanding AI/ML systems
- **Databricks Adoption**: Skills pipeline for platform utilization
- **Operational Efficiency**: Enable data-driven decision making across teams
- **Staff Development**: Career growth pathways for technical staff

### 2.3 Stakeholders

| Stakeholder | Role | Interest |
|-------------|------|----------|
| OIT Leadership | Sponsor | ROI on training investment, Databricks adoption |
| OIT Staff (Primary A) | Learner | Career development, practical skills |
| Developers (Primary B) | Learner | Data science expansion, modern tooling |
| Faculty (Tertiary) | Observer | Content generation methodology |
| Nate | Product Owner | Successful delivery, AI integration showcase |

---

## 3. Product Requirements

### 3.1 Functional Requirements

#### 3.1.1 Content Delivery

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| FR-01 | All content delivered as Marimo notebooks | Must Have | Core platform decision |
| FR-02 | Notebooks are self-contained and runnable | Must Have | No external setup beyond initial environment |
| FR-03 | Each notebook includes learning objectives | Must Have | Machine-readable metadata |
| FR-04 | Notebooks include embedded exercises | Must Have | Hands-on learning |
| FR-05 | Progress can be saved and resumed | Should Have | Marimo's native state persistence |
| FR-06 | Notebooks render correctly in VS Code | Should Have | Primary development environment |

#### 3.1.2 Learning Experience

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| FR-07 | Clear prerequisite chain between notebooks | Must Have | Dependency graph |
| FR-08 | Estimated time displayed per notebook | Must Have | Learner planning |
| FR-09 | Self-assessment checkpoints within modules | Must Have | Formative feedback |
| FR-10 | Capstone projects for summative assessment | Must Have | Skills demonstration |
| FR-11 | "Skip ahead" paths for experienced learners | Should Have | Respect prior knowledge |
| FR-12 | Hints system for exercises | Could Have | Scaffolded learning |

#### 3.1.3 Technical Environment

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| FR-13 | Single `uv sync` sets up complete environment | Must Have | Zero-friction start |
| FR-14 | All dependencies pinned and reproducible | Must Have | Consistent experience |
| FR-15 | Works on Windows, macOS, Linux | Must Have | OIT has mixed environments |
| FR-16 | Databricks notebooks exportable/compatible | Should Have | Module 8 transition |
| FR-17 | Offline capability for core modules | Could Have | Travel/disconnected learning |

#### 3.1.4 Assessment & Tracking

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| FR-18 | Rubrics provided for all capstone projects | Must Have | Consistent evaluation |
| FR-19 | Self-check answers available after attempt | Must Have | Immediate feedback |
| FR-20 | Completion certificates generated | Could Have | Recognition/motivation |

### 3.2 Non-Functional Requirements

#### 3.2.1 Performance

| ID | Requirement | Target |
|----|-------------|--------|
| NFR-01 | Notebook load time | <5 seconds on standard hardware |
| NFR-02 | Exercise execution time | <30 seconds for typical exercises |
| NFR-03 | Dataset sizes | Fit in 8GB RAM for local modules |

#### 3.2.2 Usability

| ID | Requirement | Target |
|----|-------------|--------|
| NFR-04 | Reading level | Accessible to non-CS backgrounds |
| NFR-05 | Code comments | All code blocks commented |
| NFR-06 | Error messages | Helpful, not cryptic |

#### 3.2.3 Maintainability

| ID | Requirement | Target |
|----|-------------|--------|
| NFR-07 | Notebook modularity | Each notebook independently runnable |
| NFR-08 | Content updates | Quarterly review cycle |
| NFR-09 | Dependency updates | Automated via Dependabot/Renovate |

#### 3.2.4 Accessibility

| ID | Requirement | Target |
|----|-------------|--------|
| NFR-10 | Alt text for visualizations | 100% coverage |
| NFR-11 | Color-blind friendly palettes | All visualizations |
| NFR-12 | Screen reader compatibility | Marimo's native support |

---

## 4. Technical Specifications

### 4.1 Technology Stack

#### Core Platform
- **Runtime:** Python 3.14+
- **Notebook Platform:** Marimo ≥0.10
- **Package Manager:** UV
- **Linter/Formatter:** Ruff
- **Type Checker:** ty

#### Data Processing
- **DataFrames:** Polars ≥1.0
- **SQL Engine:** DuckDB ≥1.0
- **Distributed:** PySpark (Databricks-provided)

#### Data Validation
- **Record-level:** Pydantic ≥2.10
- **DataFrame-level:** Pandera ≥0.20

#### Data Acquisition
- **HTTP Client:** httpx ≥0.27
- **Web Scraping:** Beautiful Soup 4 ≥4.12
- **API Framework:** FastAPI (optional examples)

#### Machine Learning
- **ML Framework:** scikit-learn ≥1.5

#### Testing
- **Test Framework:** pytest ≥8.0

### 4.2 Repository Structure

```
modern-python-ds-bootcamp/
├── pyproject.toml              # Project configuration
├── uv.lock                     # Locked dependencies
├── README.md                   # Getting started guide
├── .github/
│   ├── workflows/
│   │   ├── ci.yml             # Lint, type-check, test
│   │   └── notebooks.yml      # Notebook execution tests
│   └── ISSUE_TEMPLATE/
│       ├── epic.md
│       └── user-story.md
├── docs/
│   ├── instructor-guide.md    # Facilitation notes
│   ├── learner-guide.md       # How to use the bootcamp
│   └── assessment-rubrics/    # Capstone rubrics
├── src/
│   └── bootcamp/
│       ├── __init__.py
│       ├── datasets/          # Sample/synthetic data
│       ├── solutions/         # Exercise solutions (separate)
│       └── utils/             # Shared utilities
├── notebooks/
│   ├── module_00_environment/
│   │   ├── 00_01_welcome.py
│   │   ├── 00_02_installing_python_uv.py
│   │   └── ...
│   ├── module_01_modern_python/
│   ├── module_02_local_data_stack/
│   ├── module_03_data_acquisition/
│   ├── module_04_data_cleaning/
│   ├── module_05_feature_engineering/
│   ├── module_06_visualization/
│   ├── module_07_machine_learning/
│   └── module_08_databricks/
└── tests/
    ├── test_notebooks_execute.py
    └── test_solutions.py
```

### 4.3 Notebook Metadata Schema

Each notebook will include frontmatter-style metadata:

```python
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo",
#     "polars",
# ]
# [tool.bootcamp]
# module = "02"
# sequence = "03"
# title = "Polars Expressions & Method Chaining"
# duration_minutes = 60
# type = "concept_exercise"
# prerequisites = ["02_01", "02_02"]
# learning_objectives = [
#     "Write complex data transformations using Polars expressions",
#     "Chain methods effectively for readable pipelines",
#     "Understand expression context (select vs filter vs with_columns)",
# ]
# ///
```

### 4.4 Synthetic Data Requirements

#### IT Ticket Dataset (ML Capstone)
- **Size:** ~10,000 synthetic tickets
- **Fields:** ticket_id, created_date, category, priority, description, resolution_time, assigned_group
- **Categories:** ~15 categories modeled on TDX taxonomy
- **Characteristics:** Realistic text descriptions, class imbalance, missing values

#### Dirty Data Dataset (Module 4)
- **Purpose:** Intentionally messy data for cleaning exercises
- **Issues included:** Missing values (various patterns), duplicates, encoding problems, type mismatches, outliers, inconsistent formats

---

## 5. Scope

### 5.1 In Scope

- 9 modules of Marimo notebooks (~55 notebooks total)
- Synthetic datasets for exercises and capstones
- Instructor facilitation guide
- Learner quick-start guide
- Assessment rubrics for capstones
- GitHub Issues backlog for implementation tracking
- CI/CD pipeline for notebook validation

### 5.2 Out of Scope

- LMS integration (future consideration)
- Video content production
- Live Databricks cluster provisioning (learners use existing infrastructure)
- Deep learning / neural networks
- Advanced MLOps (model deployment, monitoring)
- Real-time streaming pipelines (mentioned conceptually only)

### 5.3 Future Considerations

- Integration with university LMS for credit tracking
- Advanced modules (deep learning, MLOps)
- Industry certifications alignment
- Multi-language support
- Community contribution model

---

## 6. User Stories Summary

*Detailed stories will be created as GitHub Issues. High-level epic structure:*

### Epic 1: Environment & Tooling (Module 0)
As a learner, I want to set up my development environment so I can run all bootcamp content.

### Epic 2: Modern Python (Module 1)
As a learner, I want to understand modern Python patterns so I can write professional-quality code.

### Epic 3: Local Data Stack (Module 2)
As a learner, I want to explore and transform data locally so I can perform analysis efficiently.

### Epic 4: Data Acquisition (Module 3)
As a learner, I want to collect data from various sources so I can work with real-world data.

### Epic 5: Data Cleaning (Module 4)
As a learner, I want to clean and validate messy data so I can prepare it for analysis.

### Epic 6: Feature Engineering & Pipelines (Module 5)
As a learner, I want to engineer features and build pipelines so I can create reproducible workflows.

### Epic 7: Visualization (Module 6)
As a learner, I want to create effective visualizations so I can communicate insights.

### Epic 8: Machine Learning (Module 7)
As a learner, I want to build prediction models so I can solve classification problems.

### Epic 9: Databricks Scale-Up (Module 8)
As a learner, I want to transition my skills to Databricks so I can work with large datasets.

### Epic 10: Infrastructure & CI/CD
As a maintainer, I want automated validation so I can ensure content quality.

### Epic 11: Documentation & Guides
As an instructor, I want facilitation materials so I can effectively deliver the bootcamp.

---

## 7. Risks & Mitigations

*See Pre-mortem Analysis document for detailed risk assessment.*

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Python 3.14 not widely available | Medium | High | Provide 3.12+ fallback path |
| Scope creep during development | High | Medium | Strict backlog prioritization |
| Marimo breaking changes | Low | High | Pin version, monitor releases |
| Learner environment issues | High | Medium | Detailed setup guides, office hours |
| Content becomes outdated | Medium | Medium | Quarterly review cycle |

---

## 8. Timeline & Milestones

### Phase 1: Foundation (Weeks 1-2)
- [ ] Repository setup and CI/CD
- [ ] Module 0 notebooks complete
- [ ] Module 1 notebooks complete
- [ ] Synthetic datasets created

### Phase 2: Core Data Skills (Weeks 3-4)
- [ ] Module 2 notebooks complete
- [ ] Module 3 notebooks complete
- [ ] Module 4 notebooks complete

### Phase 3: Advanced Topics (Weeks 5-6)
- [ ] Module 5 notebooks complete
- [ ] Module 6 notebooks complete
- [ ] Module 7 notebooks complete

### Phase 4: Scale & Polish (Weeks 7-8)
- [ ] Module 8 notebooks complete
- [ ] Documentation finalized
- [ ] Pilot testing with small group
- [ ] Feedback incorporation

### Phase 5: Launch (Week 9)
- [ ] First cohort enrollment
- [ ] Instructor training
- [ ] Launch communications

---

## 9. Dependencies & Assumptions

### Dependencies
- Access to Databricks workspace for Module 8 testing
- Availability of coding agents for notebook generation
- UV, Ruff, ty stable releases compatible with Python 3.14

### Assumptions
- Learners have basic computer literacy
- Learners can dedicate ~10 hours/week for 4-6 weeks
- IT support available for environment troubleshooting
- Marimo remains actively maintained

---

## 10. Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Product Owner | | | |
| Technical Lead | | | |
| Sponsor | | | |

---

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| Marimo | Reactive Python notebook platform |
| UV | Fast Python package manager from Astral |
| Ruff | Python linter and formatter from Astral |
| ty | Python type checker from Astral |
| Polars | High-performance DataFrame library |
| DuckDB | Embedded analytical database |
| Pydantic | Data validation using Python type hints |
| Pandera | DataFrame validation library |

---

## Appendix B: References

- [Marimo Documentation](https://marimo.io)
- [Polars User Guide](https://pola.rs)
- [DuckDB Documentation](https://duckdb.org)
- [Pydantic Documentation](https://docs.pydantic.dev)
- [scikit-learn User Guide](https://scikit-learn.org)
- [Astral Tools](https://astral.sh)
