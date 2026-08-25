# Playwright Automation Test

Learning and practice repository for test automation with **Playwright**, **pytest**, **Python**, **JavaScript**, and **TypeScript**. The examples cover UI, API, integration, design patterns, debugging, performance, and automation against external services.

> This repository contains independent examples. Each folder may have its own configuration, and not all tests are designed to run together from the root directory.

## Contents

### Playwright with Python

| Folder | What it demonstrates |
| --- | --- |
| `ambitosfuncion` | Session fixtures, browser/context arguments, authenticated storage, and browser detection. |
| `API_server` | Small user API/server and supporting Python model. |
| `API_test` | Python application/API tests. |
| `asserts` | Assertions and validations with Playwright/pytest. |
| `codegen` | Playwright Codegen flow against the Playwright documentation. |
| `datadriven` | Pytest parameterized tests for a mathematical function. |
| `emulationdevices` | Browser contexts with viewport and color scheme settings, plus manual navigation. |
| `GITHUBAPI` | GitHub API and UI tests: create issues, query issues, and capture screenshots. |
| `ICtest` | Additional test automation examples. |
| `JavascriptEvaluate` | JavaScript evaluation in a page and HTML report generation. |
| `networkevents` | Request/response observation, route interception, response modification, and screenshots. |
| `optimizacion` | Blocking images, fonts, stylesheets, media, and scripts to speed up tests. |
| `POM` | Page Object Model with login and Playwright documentation pages. |
| `pruebas_api_rest` | REST health check, user creation, user retrieval, and validation tests; includes historical results. |
| `pruebas_integracion` | User persistence and database queries through pytest fixtures. |
| `pruebas_interfaz_usuario` | Playwright/pytest UI cases for forms and browser interaction. |
| `pruebas_web_ui` | Web UI tests for forms. |
| `pytest` | Fixtures, utilities, assertions, report generation, and supporting tests. |
| `python_test` | Unit tests for totals, discounts, empty lists, and validation errors. |
| `TDC` | Behavior-Driven Development with `pytest-bdd`, Gherkin features, and login step definitions. |

### Playwright with JavaScript and TypeScript

| Folder | What it demonstrates |
| --- | --- |
| `APItestTypescript` | API test with `APIRequestContext` against JSONPlaceholder, TypeScript configuration, Docker, and its own workflow. |
| `mytypescript` | JavaScript/TypeScript examples, Playwright navigation, and a GitHub Actions workflow. |
| `testypescript` | TypeScript suite with Page Objects for login, products, product details, user data, and menus. |
| `typescript` | TypeScript suite with home, products, and cart Page Objects; includes Playwright configuration and a generated Allure report. |

## Technologies

- Python, pytest, and pytest-bdd.
- Playwright for Python, JavaScript, and TypeScript.
- Page Object Model, fixtures, parameterization, and integration testing.
- UI, REST API, network event, emulation, and JavaScript evaluation testing.
- HTML and Allure reporting.
- Docker for the TypeScript API project.
- GitHub Actions in projects containing `.github/workflows`.

## Requirements

- Python 3.9 or newer.
- Node.js LTS for JavaScript/TypeScript projects.
- Git.
- Playwright browsers.
- Allure CLI only if you want to open or generate Allure reports.
- Access to external services used by the examples, including Playwright Docs, Blass Academy, JSONPlaceholder, and GitHub.

## Python setup

From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
playwright install
```

Run a specific Python project from its own directory:

```powershell
cd python_test
pytest -q
```

Examples configured for visible execution can be run with `pytest` without `-q`. Some folders have a `pytest.ini` with options such as `--headed`, `--slowmo`, and a specific browser.

## Node and TypeScript setup

Each Node project maintains its own `package.json` and `package-lock.json`:

```powershell
cd APItestTypescript
npm ci
npx playwright install
npm test
```

Use the same approach for the other JavaScript/TypeScript projects. Inspect available scripts first:

```powershell
npm run
```

## GitHub API and secrets

`GITHUBAPI` reads `GITHUB_TOKEN` from an environment variable. Never store tokens in source code or commit them to the repository.

```powershell
$env:GITHUB_TOKEN = "your-local-token"
cd GITHUBAPI
pytest -q
```

The example targets the test repository configured in `GITHUBAPI/creds.py`. Use a test account and repository because the fixture creates and deletes a repository and creates an issue.

## Reports

Projects with HTML reporters usually generate results in `playwright-report/` or `reports/`. Open a Playwright report with:

```powershell
npx playwright show-report
```

Serve an existing Allure report with:

```powershell
allure serve allure-results
```

## Docker

`APItestTypescript/dockerfile` builds an image based on the official Playwright image:

```powershell
cd APItestTypescript
docker build -f dockerfile -t api-test-typescript .
docker run --rm api-test-typescript
```

## GitHub Actions

Workflows located inside individual projects run when those projects are part of the repository. The `APItestTypescript` workflow installs dependencies, installs browsers, runs Playwright, and uploads the report as an artifact.

For a maintainable development process:

1. Work on short-lived branches and open Pull Requests into `main`.
2. Keep each example self-contained and document external dependencies.
3. Do not commit generated reports, credentials, virtual environments, or `node_modules`.
4. Add a test that reproduces a regression before fixing it.
5. Use fixtures and Page Objects to reduce duplication without hiding test behavior.

## Known limitations

- Most examples depend on external websites and may fail because of UI changes, network issues, rate limits, or service availability.
- Many configurations target visible local execution (`headed`) and may need adjustments for headless CI environments.
- There is not yet one root workflow that installs and runs every language and project.
- Some reports and screenshots are historical artifacts, not the result of a current execution.

## Related project

The `julietaPage` web application is maintained outside this repository at https://github.com/ricarlo44/julietamaga
