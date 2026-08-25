# AutomationExercise Playwright TypeScript tests

Quick steps to run the test and generate an Allure report:

1. Install dependencies

```bash
cd typescript
npm install
npx playwright install
```

2. Run tests

```bash
npm run test
```


Run tests in headed Chrome (open browser window and see actions in real time):

```bash
npm run test -- --project=chrome
```

3. Generate Allure report (requires `allure-commandline` binary from the npm package above)

```bash
npm run allure:generate
npm run allure:open
```

Notes:
- The tests use Playwright and the Page Object Model under `pages/`.
- Screenshots are saved to `allure-results/` and attached to the test.
