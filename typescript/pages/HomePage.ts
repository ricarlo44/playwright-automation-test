import { Page } from '@playwright/test';

export class HomePage {
  readonly page: Page;
  constructor(page: Page) {
    this.page = page;
  }

  async goto() {
    await this.page.goto('https://automationexercise.com/');
    await this.page.waitForLoadState('networkidle');
    // close any modal or overlay that may block interactions (e.g., ads)
    try {
      const closeBtn = this.page.locator('text=Close, button[aria-label="close"], .modal .close, .fancybox-close').first();
      if (await closeBtn.count() > 0) {
        await closeBtn.click({ timeout: 2000 }).catch(() => {});
        await this.page.waitForTimeout(500);
      }
    } catch (e) {
      // ignore if no modal present
    }
    // fallback: send Escape to close any modal
    try {
      await this.page.keyboard.press('Escape');
      await this.page.waitForTimeout(500);
    } catch (e) {}
  }

  async clickProductsMenu() {
    await this.page.locator('a:has-text("Products")').click({ timeout: 10000 });
    await this.page.waitForLoadState('networkidle');
  }

  async searchProduct(query: string) {
    // try a few common selectors for the search input and submit
    const input = this.page.locator('#search_product, input[placeholder*="Search"], input[name*="search"]').first();
    await input.fill(query, { timeout: 10000 });
    const submit = this.page.locator('#submit_search, button[type="submit"], button:has-text("Search")').first();
    await submit.click();
    await this.page.waitForLoadState('networkidle');
  }
}
