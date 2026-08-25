import { Page } from '@playwright/test';

export class CartPage {
  readonly page: Page;
  constructor(page: Page) {
    this.page = page;
  }

  async confirmItemInCart(name: string) {
    const row = this.page.locator('table.cart, table#cart, .cart_info').locator(`text=${name}`);
    await row.first().waitFor({ state: 'visible', timeout: 10000 });
    return await row.first().isVisible();
  }

  async takeScreenshot(path: string) {
    await this.page.screenshot({ path, fullPage: true });
  }

  async deleteFirstItem() {
    const deleteBtn = this.page.locator('a.cart_quantity_delete, a:has-text("Delete"), .cart_delete').first();
    await deleteBtn.click({ timeout: 10000 });
    // wait a bit for the row to be removed
    await this.page.waitForTimeout(1500);
  }
}
