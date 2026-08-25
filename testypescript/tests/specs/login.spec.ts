import {test, expect} from "@playwright/test";
import {LoginPage} from "../pages/LoginPage";

test.describe("Login", () => {
    let loginPage: LoginPage;
    test.beforeEach(async ({page}) => {
        loginPage = new LoginPage(page);
        loginPage.open();
    });
    test("Credenciales Erroneas", async ({page}) => {
        await loginPage.rellenarFormulario("blass", "academy");
        await expect.soft(loginPage.mensajeError).toBeVisible();
        await expect.soft(loginPage.mensajeError).toHaveText("Usuario y/o clave incorrectas");
    });
    test("Credenciales Bloqueadas", async ({page}) => {
        await loginPage.rellenarFormulario("blocked_user", "secret_blass_academy");
        await expect.soft(loginPage.mensajeError).toBeVisible();
        await expect.soft(loginPage.mensajeError).toHaveText("Este usuario ha sido bloqueado");
    });
    test("Login, compras", async ({page}) => {
        await loginPage.rellenarFormulario("standard_user", "secret_blass_academy");
        await expect.soft(loginPage.mensajeError).toBeVisible();
        await expect.soft(loginPage.mensajeError).toHaveText("Este usuario ha sido bloqueado");
    });
});