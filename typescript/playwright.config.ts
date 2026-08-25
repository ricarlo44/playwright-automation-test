import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 120000,
  use: {
    actionTimeout: 30000,
    navigationTimeout: 60000,
    screenshot: 'only-on-failure'
  },
  projects: [
    {
      name: 'chrome',
      use: {
        browserName: 'chromium',
        channel: 'chrome',
        headless: false,
        launchOptions: { slowMo: 100 },
        viewport: { width: 1280, height: 800 }
      }
    }
  ],
  reporter: [['list'], ['allure-playwright']]
});
