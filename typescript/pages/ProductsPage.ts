import { Page } from '@playwright/test';

export class ProductsPage {
  readonly page: Page;
  constructor(page: Page) {
    this.page = page;
  }

  async confirmProductVisible(name: string) {
    const locator = this.page.locator(`text=${name}`);
    await locator.first().waitFor({ state: 'visible', timeout: 10000 });
    return await locator.first().isVisible();
  }

  async addMatchingItemToCart(name: string) {
    // Find a product card that contains the product name and click its Add to cart button
    const productCard = this.page.locator(`.productinfo, .single-products, div:has-text("${name}")`).filter({ has: this.page.locator(`text=${name}`) }).first();
    if ((await productCard.count()) === 0) {
      throw new Error('Product card not found for: ' + name);
    }
    await productCard.scrollIntoViewIfNeeded();
    await productCard.hover();
    const addBtn = productCard.locator('a:has-text("Add to cart"), button:has-text("Add to cart")').first();
    await addBtn.click({ timeout: 10000 });
    // wait for the modal or view cart button to appear
    await this.page.locator('a:has-text("View Cart"), a:has-text("Cart"), button:has-text("View Cart")').first().waitFor({ state: 'visible', timeout: 10000 });
  }

  async clickViewCart() {
    await this.page.locator('a:has-text("View Cart")').first().click({ timeout: 10000 });
    await this.page.waitForLoadState('networkidle');
  }
}
