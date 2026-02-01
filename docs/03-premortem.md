# Pre-mortem Analysis
## Modern Python Data Science Bootcamp

**Document Version:** 1.0  
**Last Updated:** 2025-01-31  
**Facilitator:** Nate  

---

## What is a Pre-mortem?

A pre-mortem is a risk identification technique where we imagine the project has already failed, then work backward to identify what caused the failure. This surfaces risks that optimism bias might otherwise hide.

**Scenario:** It's August 2025. The Modern Python Data Science Bootcamp launched, but it's considered a failure. What went wrong?

---

## Failure Modes & Mitigations

### 1. 🔴 Content Quality Failures

#### 1.1 "The notebooks are buggy and don't run"

**Why it happened:**
- Coding agents generated content without sufficient testing
- Dependencies changed between generation and learner execution
- Platform-specific issues (Windows vs Mac vs Linux) not caught
- Notebooks tested in isolation but fail when run in sequence

**Warning signs:**
- No CI/CD running notebooks end-to-end
- Infrequent human review of generated content
- No beta testing before launch

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Implement notebook execution CI that runs all notebooks | Infra | P0 |
| Pin ALL dependencies with exact versions | Infra | P0 |
| Test on all three major platforms | QA | P1 |
| Establish human review checkpoints after agent generation | Nate | P0 |
| Run pilot cohort 2 weeks before official launch | Nate | P1 |

#### 1.2 "The explanations don't make sense to beginners"

**Why it happened:**
- Content written at wrong level (curse of knowledge)
- Too much jargon without explanation
- Assumed prerequisites not actually covered
- Examples too abstract, not relatable

**Warning signs:**
- No review by actual target audience members
- All reviewers are already experts
- No readability scoring applied

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Recruit 2-3 target audience members as beta readers | Nate | P1 |
| Add glossary links for first use of technical terms | Content | P1 |
| Include "why does this matter?" sections | Content | P2 |
| Use university-relevant examples throughout | Content | P1 |

#### 1.3 "Exercises are too hard / too easy"

**Why it happened:**
- No difficulty calibration process
- Solutions not tested by novices
- Time estimates wildly inaccurate
- No scaffolding between concept and exercise

**Warning signs:**
- Exercise completion rates very low or 100%
- Time-to-complete data shows huge variance
- Learner feedback mentions frustration

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Include hints system with progressive revelation | Content | P2 |
| Time-box all exercises during development | Content | P1 |
| Add "challenge" extensions for advanced learners | Content | P2 |
| Test exercises with actual beginners before launch | QA | P1 |

---

### 2. 🟠 Technical Environment Failures

#### 2.1 "Learners can't get the environment set up"

**Why it happened:**
- UV installation issues on corporate Windows
- Python 3.14 not available or blocked by IT policies
- Firewall blocks package downloads
- Conflicting Python installations cause chaos

**Warning signs:**
- Setup guide assumes ideal conditions
- No troubleshooting section
- Office hours dominated by setup issues

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Create detailed setup guides for Windows/Mac/Linux | Docs | P0 |
| Include troubleshooting FAQ | Docs | P0 |
| Provide Python 3.12 fallback compatibility | Infra | P1 |
| Pre-record setup walkthrough video | Docs | P2 |
| Offer "setup session" office hours before bootcamp starts | Delivery | P1 |
| Test setup process on fresh corporate Windows machine | QA | P0 |

#### 2.2 "Marimo has breaking changes or becomes unmaintained"

**Why it happened:**
- Single platform dependency
- No abstraction layer
- Marimo project loses momentum

**Warning signs:**
- Marimo release velocity slows
- Breaking changes in minor versions
- Community activity declining

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Pin Marimo version strictly | Infra | P0 |
| Monitor Marimo GitHub for concerning signals | Nate | Ongoing |
| Document "escape hatch" to Jupyter conversion | Docs | P3 |
| Contribute to Marimo project if beneficial | Nate | P3 |

#### 2.3 "Python 3.14 features cause compatibility issues"

**Why it happened:**
- Python 3.14 too new, tooling not ready
- Type checker doesn't support new syntax
- Dependencies don't support 3.14 yet

**Warning signs:**
- Tool releases lagging Python release
- Community complaints about 3.14 adoption
- CI failures on 3.14-specific features

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Test full stack on Python 3.14 beta early | Infra | P0 |
| Identify 3.14-specific features used, have 3.12 alternatives | Content | P1 |
| Monitor Astral tools for 3.14 support status | Nate | Ongoing |
| Design content to gracefully degrade to 3.12 | Content | P1 |

---

### 3. 🟡 Scope & Schedule Failures

#### 3.1 "We only finished half the modules before launch"

**Why it happened:**
- Scope too ambitious for timeline
- Agent-generated content required more human editing than expected
- Perfectionism on early modules consumed budget
- Key person unavailable (illness, other priorities)

**Warning signs:**
- Milestone slippage in weeks 2-3
- "Almost done" status persisting
- Growing backlog of review items

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Define MVP scope: Modules 0-4 + 7 are minimum viable | Nate | P0 |
| Timebox each notebook: max 4 hours creation + review | Process | P1 |
| Weekly progress tracking against milestones | Process | P0 |
| Identify modules that could be "Phase 2" if needed | Nate | P1 |
| Have backup contributor identified | Nate | P2 |

**MVP Definition:**
If we can only ship partial content, prioritize:
1. Module 0 (Environment) - required
2. Module 1 (Python Fundamentals) - required  
3. Module 2 (Polars/DuckDB) - required
4. Module 4 (Data Cleaning) - core value prop
5. Module 7 (ML Capstone) - satisfying conclusion

Modules 3, 5, 6, 8 could be "coming soon" in worst case.

#### 3.2 "Scope crept and we built something nobody needed"

**Why it happened:**
- Added "nice to have" features without cutting elsewhere
- Stakeholder requests accepted without prioritization
- Lost sight of primary audience needs

**Warning signs:**
- Requirements document growing after approval
- "Just one more thing" pattern
- Features added without user validation

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Freeze scope after PRD approval | Nate | P0 |
| All additions require removing something else | Process | P0 |
| Monthly check-in: "Are we still solving the original problem?" | Process | P1 |

---

### 4. 🟢 Adoption & Engagement Failures

#### 4.1 "Nobody signed up / completed the bootcamp"

**Why it happened:**
- Poor communication about bootcamp existence
- Value proposition unclear
- Time commitment too high for workload
- No management support for learning time

**Warning signs:**
- Low enrollment numbers
- High drop-off after Module 1
- Learner feedback: "I don't have time"

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Secure management endorsement for learning time | Nate | P0 |
| Clear communication: "40 hours over 4-6 weeks" | Comms | P0 |
| Testimonials from pilot cohort | Comms | P1 |
| Completion certificates / recognition | Delivery | P2 |
| Flexible pacing: no hard deadlines for self-paced | Delivery | P1 |

#### 4.2 "Learners completed but didn't apply skills"

**Why it happened:**
- Content too theoretical, not connected to real work
- No follow-up support or community
- No opportunities to practice
- Gap between bootcamp projects and real projects too large

**Warning signs:**
- Post-bootcamp survey: "Interesting but not useful"
- No observable behavior change
- Databricks usage unchanged

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Every module includes "apply this at work" section | Content | P1 |
| Create "office hours" for applying skills to real problems | Delivery | P2 |
| Capstone project should mirror real OIT use cases | Content | P0 |
| Post-bootcamp Slack channel for alumni | Community | P2 |
| Track Databricks usage as lagging indicator | Metrics | P2 |

---

### 5. 🔵 Meta/Process Failures

#### 5.1 "The agent-generated content was more work than manual creation"

**Why it happened:**
- Agents produced plausible but incorrect content
- Heavy editing required for tone/level
- Context window limitations caused inconsistency
- More time reviewing than would have been spent writing

**Warning signs:**
- Edit ratio (changes/original) > 50%
- Repeated similar errors across notebooks
- Human reviewers frustrated

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Develop detailed prompt templates with examples | Nate | P0 |
| Start with 2-3 notebooks to calibrate process | Process | P0 |
| Track edit ratio and adjust process if > 40% | Process | P1 |
| Build style guide and feed back to agents | Content | P1 |
| Accept that some notebooks may need manual creation | Process | P1 |

#### 5.2 "The backlog became stale and nobody used it"

**Why it happened:**
- Issues too granular or too vague
- GitHub Issues friction for non-developers
- Status updates not maintained
- Backlog disconnected from actual work

**Warning signs:**
- Issues not updated for weeks
- Work happening outside tracked items
- "Where are we?" questions frequent

**Mitigations:**
| Action | Owner | Priority |
|--------|-------|----------|
| Keep issues at right granularity (1-4 hours of work) | Process | P1 |
| Weekly backlog grooming | Process | P1 |
| Use GitHub Projects board for visibility | Infra | P1 |
| Link commits/PRs to issues | Process | P1 |

---

## Risk Heat Map

```
                    IMPACT
                Low    Med    High
           ┌────────┬────────┬────────┐
     High  │  3.2   │  3.1   │  1.1   │
           │        │  4.1   │  2.1   │
LIKELIHOOD ├────────┼────────┼────────┤
     Med   │  5.2   │  1.3   │  2.3   │
           │        │  4.2   │        │
           ├────────┼────────┼────────┤
     Low   │        │  1.2   │  2.2   │
           │        │  5.1   │        │
           └────────┴────────┴────────┘
```

**Priority Focus (High Likelihood + High/Med Impact):**
1. **1.1** Notebooks don't run → Robust CI/CD
2. **2.1** Environment setup fails → Detailed guides + testing
3. **3.1** Scope overrun → MVP definition + timeboxing
4. **4.1** Low adoption → Management buy-in + clear value prop

---

## Action Summary

### Immediate (Before Development Starts)
- [ ] Define MVP scope explicitly
- [ ] Set up CI/CD with notebook execution tests
- [ ] Create detailed setup guides for all platforms
- [ ] Secure management endorsement for learning time
- [ ] Develop prompt templates for agent content generation

### During Development
- [ ] Weekly milestone tracking
- [ ] Test on fresh corporate Windows machine
- [ ] Recruit beta readers from target audience
- [ ] Monitor edit ratios on agent-generated content

### Before Launch
- [ ] Run pilot cohort (minimum 3 learners)
- [ ] Platform testing on Windows/Mac/Linux
- [ ] Troubleshooting FAQ based on pilot feedback
- [ ] Communication plan for enrollment

---

## Pre-mortem Review Schedule

| Date | Review Focus |
|------|--------------|
| Week 2 | Are CI/CD and setup guides working? |
| Week 4 | Are we on track for MVP scope? |
| Week 6 | Pilot cohort feedback incorporated? |
| Week 8 | Launch readiness checklist |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-31 | Claude + Nate | Initial pre-mortem |
