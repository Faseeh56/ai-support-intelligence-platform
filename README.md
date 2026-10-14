# SupportIQ — AI Support Intelligence Platform

**An evolving, evidence-grounded customer support intelligence platform for e-commerce businesses.**

> **Project status: Early development (v0.0.1).** The FastAPI foundation and initial automated tests are available. AI-powered answers, document retrieval, and analytics are **planned**, not yet implemented.

## Overview

E-commerce support teams handle recurring questions about orders, returns, refunds, and store policies. Answers can become inconsistent when information is scattered across documents, while repeated issues are difficult to identify without reliable reporting.

SupportIQ aims to help teams answer questions using approved company knowledge and understand recurring support problems. The longer-term objective is a maintainable application that prioritizes evidence, transparency, and human oversight over unsupported AI responses.

## Proposed workflow

```text
Customer question
       |
       v
Support API
       |
       v
Retrieve relevant approved knowledge
       |
       v
Generate an answer grounded in retrieved evidence
       |
       +----> Insufficient evidence? -> Abstain / request human review
       |
       v
Return answer with source references
       |
       v
Collect feedback and support analytics
```

*This diagram describes the target workflow, not the currently deployed application.*

## Current implementation

The public `main` branch currently contains:

- A FastAPI application in `app/main.py`.
- `GET /health` returning `{"status": "ok"}`.
- `GET /version` returning `{"version": "0.0.1"}`.
- Initial API tests using `pytest` and FastAPI's `TestClient`.
- Python dependencies recorded in `requirements.txt`.

**Work in progress:** GitHub Actions CI is being developed on a feature branch; it should not be considered active on `main` until merged and verified.

## Development roadmap

| Phase | Focus | Status |
| --- | --- | --- |
| 1 | Repository structure, FastAPI foundation, basic tests | In progress |
| 2 | CI, configuration, data models and persistence | Planned |
| 3 | Knowledge ingestion and retrieval | Planned |
| 4 | Grounded response generation, citations and safe fallback | Planned |
| 5 | Support analytics, evaluation and feedback | Planned |
| 6 | Security, deployment, observability and hardening | Planned |

The project follows an incremental, learning-driven **3–5-month development roadmap**. An initial competition demonstration, if developed, will represent only a focused subset of this broader system.

## Technology stack

**Currently used:** Python, FastAPI, Pydantic, Uvicorn, pytest, Git and GitHub.

**Under evaluation for future phases:** persistent storage, embeddings/vector search, an LLM provider, a lightweight user interface, and deployment/monitoring tools. Technology choices will be justified and documented as the project evolves.

## Run locally

Prerequisites: Python and Git. From a terminal:

```bash
# Clone the repository
git clone https://github.com/Faseeh56/ai-support-intelligence-platform.git
cd ai-support-intelligence-platform

# Create and activate a project-specific virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
python -m pip install -r requirements.txt

# Start the development server
uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive API documentation.

### Try the available endpoints

```bash
curl http://127.0.0.1:8000/health
# {"status":"ok"}

curl http://127.0.0.1:8000/version
# {"version":"0.0.1"}
```

### Run tests

```bash
python -m pytest -v
```

Tests currently cover the API foundation; they do not establish reliability of future AI features.

## Engineering principles

- **Evidence first:** prefer answers supported by approved knowledge; abstain when evidence is insufficient.
- **Incremental delivery:** implement small, testable workflows before introducing additional complexity.
- **Clear boundaries:** distinguish application logic, retrieval, model integration, and data handling.
- **Measurable quality:** evaluate retrieval and answer quality before making reliability claims.
- **Security by design:** avoid committing secrets or using sensitive customer data without proper authorization.

## Known limitations

- No document ingestion or RAG pipeline is implemented in the current public `main` branch.
- No integrated LLM response generation or source citation feature exists yet.
- No support analytics dashboard or production deployment is available yet.
- Authentication, monitoring, and production security controls remain future work.

## Project context

SupportIQ is both a practical AI engineering portfolio project and the subject of a proposal submitted to the **4th International AI Championship 2026**, under **AI in Retail & E-Commerce**. The competition proposal describes intended work; it does not imply the proposed features are already complete.

## Development and contributions

Development is ongoing. Issues and planned milestones are tracked in this repository. Please open an issue before proposing a major change so it can be discussed against the current scope.

---

**Maintained by:** [Faseeh56](https://github.com/Faseeh56) and project collaborators.