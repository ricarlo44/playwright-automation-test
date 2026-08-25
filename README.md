# playwright-automation-test
Implement diferents kind of test in automation
# Playwright Automation Test

Repositorio de aprendizaje y práctica de automatización de pruebas con **Playwright**, **pytest**, **Python**, **JavaScript** y **TypeScript**. Los ejemplos cubren pruebas UI, API, integración, patrones de diseño, depuración, rendimiento y automatización contra servicios externos.

> Este repositorio contiene ejemplos independientes. Cada carpeta puede tener su propia configuración y no todas las pruebas están diseñadas para ejecutarse juntas desde la raíz.

## Contenido

### Playwright con Python

| Carpeta | Qué demuestra |
| --- | --- |
| `ambitosfuncion` | Fixtures de sesión, argumentos de navegador/contexto, almacenamiento autenticado y detección de navegador. |
| `API_server` | Pequeño servidor/API de usuarios y modelo Python de apoyo. |
| `API_test` | Pruebas Python de aplicación/API. |
| `asserts` | Aserciones y validaciones con Playwright/pytest. |
| `codegen` | Flujo generado con Playwright Codegen contra la documentación de Playwright. |
| `datadriven` | Pruebas parametrizadas con pytest para una función matemática. |
| `emulationdevices` | Contextos con viewport, esquema de color y navegación manual usando Playwright. |
| `GITHUBAPI` | Pruebas de API y UI sobre GitHub: crear issues, consultar issues y tomar capturas. |
| `ICtest` | Ejemplos adicionales de pruebas de automatización. |
| `JavascriptEvaluate` | Evaluación de JavaScript en página y generación de reportes HTML. |
| `networkevents` | Observación de requests/responses, interceptación de rutas, modificación de respuestas y capturas. |
| `optimizacion` | Bloqueo de recursos como imágenes, fuentes, estilos, media y scripts para acelerar pruebas. |
| `POM` | Page Object Model con páginas de login y documentación de Playwright. |
| `pruebas_api_rest` | Pruebas REST de health check, creación, consulta y validación de usuarios; incluye resultados históricos. |
| `pruebas_integracion` | Persistencia de usuarios y consultas contra una base de datos mediante fixtures. |
| `pruebas_interfaz_usuario` | Casos UI de Playwright/pytest sobre formularios e interacción del navegador. |
| `pruebas_web_ui` | Pruebas web UI sobre formularios. |
| `pytest` | Fixtures, utilidades, aserciones, generación de reportes y pruebas de apoyo. |
| `python_test` | Pruebas unitarias de cálculo de totales, descuentos, listas vacías y errores de validación. |
| `TDC` | Behavior-Driven Development con `pytest-bdd`, features Gherkin y step definitions de login. |

### Playwright con JavaScript y TypeScript

| Carpeta | Qué demuestra |
| --- | --- |
| `APItestTypescript` | Prueba de API con `APIRequestContext` contra JSONPlaceholder, configuración TypeScript, Docker y workflow propio. |
| `mytypescript` | Ejemplos JavaScript/TypeScript, navegación Playwright y workflow de GitHub Actions. |
| `testypescript` | Suite TypeScript con Page Objects para login, productos, detalle de producto, datos del usuario y menú. |
| `typescript` | Suite TypeScript con Page Objects de home, productos y carrito; incluye configuración Playwright y un reporte Allure generado. |

## Tecnologías

- Python, pytest y pytest-bdd.
- Playwright para Python, JavaScript y TypeScript.
- Page Object Model, fixtures, parametrización y pruebas de integración.
- Pruebas UI, API REST, eventos de red, emulación y evaluación de JavaScript.
- Reportes HTML y Allure.
- Docker para el proyecto TypeScript de API.
- GitHub Actions en los proyectos que incluyen `.github/workflows`.

## Requisitos

- Python 3.9 o superior.
- Node.js LTS para los proyectos JavaScript/TypeScript.
- Git.
- Navegadores de Playwright.
- Allure CLI solo si se desea abrir o generar reportes Allure.
- Un servicio externo disponible cuando el ejemplo navega a Playwright Docs, Blass Academy, JSONPlaceholder o GitHub.

## Instalación Python

Desde la raíz del repositorio:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
playwright install
```

Para ejecutar un proyecto Python concreto, usa su carpeta como directorio de trabajo:

```powershell
cd python_test
pytest -q
```

Para los ejemplos configurados en modo visible, puedes ejecutar `pytest` sin `-q`. Algunas carpetas tienen `pytest.ini` con opciones como `--headed`, `--slowmo` y un navegador específico.

## Instalación Node/TypeScript

Cada proyecto Node mantiene su propio `package.json` y `package-lock.json`:

```powershell
cd APItestTypescript
npm ci
npx playwright install
npm test
```

Otros proyectos TypeScript/JavaScript se ejecutan de la misma forma desde su carpeta. Revisa primero sus scripts con:

```powershell
npm run
```

## GitHub API y secretos

`GITHUBAPI` usa `GITHUB_TOKEN` desde una variable de entorno. Nunca guardes tokens en el código ni los subas al repositorio.

```powershell
$env:GITHUB_TOKEN = "tu-token-local"
cd GITHUBAPI
pytest -q
```

El ejemplo apunta por defecto al repositorio de prueba definido en `GITHUBAPI/creds.py`. Usa una cuenta y un repositorio de pruebas, porque el fixture crea y elimina un repositorio y crea un issue.

## Reportes

Los proyectos con reporter HTML suelen generar sus resultados en `playwright-report/` o `reports/`. Para abrir un reporte Playwright:

```powershell
npx playwright show-report
```

Para un reporte Allure existente:

```powershell
allure serve allure-results
```

## Docker

`APItestTypescript/dockerfile` crea una imagen basada en la imagen oficial de Playwright:

```powershell
cd APItestTypescript
docker build -f dockerfile -t api-test-typescript .
docker run --rm api-test-typescript
```

## GitHub Actions

Los workflows ubicados dentro de cada proyecto se ejecutan cuando ese proyecto forma parte del repositorio. El workflow de `APItestTypescript` instala dependencias, instala navegadores, ejecuta Playwright y publica el reporte como artefacto.

Para evolucionar este repositorio con una metodología mantenible:

1. Trabaja en ramas cortas y abre Pull Requests hacia `main`.
2. Mantén cada ejemplo autocontenido y documenta sus dependencias externas.
3. No mezcles reportes generados, credenciales, entornos virtuales ni `node_modules` con el código fuente.
4. Añade una prueba que reproduzca el comportamiento antes de corregir una regresión.
5. Usa fixtures y Page Objects para reducir duplicación sin ocultar el comportamiento de la prueba.

## Limitaciones conocidas

- La mayoría de ejemplos dependen de sitios externos y pueden fallar por cambios de UI, red, rate limits o disponibilidad del servicio.
- Muchas configuraciones están orientadas a ejecución local visible (`headed`) y pueden necesitar ajustes para CI sin interfaz gráfica.
- No existe todavía un workflow único en la raíz que instale y ejecute todos los lenguajes y proyectos.
- Algunos reportes y capturas son artefactos históricos, no el resultado de una ejecución actual.

## Proyectos relacionados

La aplicación web `julietaPage` se mantiene fuera de este repositorio, en: https://github.com/ricarlo44/julietamaga
