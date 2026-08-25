import { test, expect } from '@playwright/test';
import { HomePage } from '../pages/HomePage';
import { ProductsPage } from '../pages/ProductsPage';
import { CartPage } from '../pages/CartPage';
import path from 'path';

const PRODUCT_NAME = 'GRAPHIC DESIGN MEN T SHIRT - BLUE';

test('search, add to cart, view and remove product (POM)', async ({ page }, testInfo) => {
  const home = new HomePage(page);
  const products = new ProductsPage(page);
  const cart = new CartPage(page);

  await home.goto();
  await home.clickProductsMenu();

  // apply a suitable wait and perform search
  await home.searchProduct(PRODUCT_NAME);

  // confirm that the item appears in results
  const visible = await products.confirmProductVisible(PRODUCT_NAME);
  expect(visible).toBeTruthy();

  // add matching item to cart
  await products.addMatchingItemToCart(PRODUCT_NAME);

  // click view cart and confirm item is present
  await products.clickViewCart();
  const inCart = await cart.confirmItemInCart(PRODUCT_NAME);
  expect(inCart).toBeTruthy();

  // take screenshot after adding
  const screenshot1 = path.join('allure-results', `added-${Date.now()}.png`);
  await cart.takeScreenshot(screenshot1);
  testInfo.attach('screenshot-after-add', { path: screenshot1, contentType: 'image/png' });

  // delete the item and take another screenshot
  await cart.deleteFirstItem();
  const screenshot2 = path.join('allure-results', `deleted-${Date.now()}.png`);
  await cart.takeScreenshot(screenshot2);
  testInfo.attach('screenshot-after-delete', { path: screenshot2, contentType: 'image/png' });
});
