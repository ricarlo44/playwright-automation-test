import {test, expect} from '@playwright/test';

test.describe("navegacion", () => {
    test("primer test", async ({ page }) => {
        await page.goto("");
        const urlActual = await page.url();
        await expect(page).toHaveURL(urlActual);
    });
    test("login example", async ({ page }) => {
        await page.goto("login");
        await page.getByRole("textbox", {name: 'usuario'}).fill('ricardo');
        await page.getByRole("textbox", {name: 'clave'}).fill('clave');
        await page.getByRole("button", {name:'ingresar'}).click();
        await expect.soft(page.getByText('Usuario o clave incorrectos.')).toBeVisible();
        await expect.soft(page.getByText('Usuario o clave incorrectos.')).toHaveText("Usuario o clave incorrectos. Intente de nuevo.");
    });
});