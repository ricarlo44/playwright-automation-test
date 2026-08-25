import {test, expect} from "@playwright/test";
import {LoginPage} from "../pages/LoginPage";   
import {BurgerMenu} from "../pages/BurgerMenuPage";

test.describe("Burger Menu", () => {
    let burgerMenu: BurgerMenu;
    let loginPage: LoginPage;

    test.beforeEach(async ({page}) => {
        burgerMenu = new BurgerMenu(page);
        loginPage = new LoginPage(page);
        await burgerMenu.open();
    });
    test("Logout", async () => {
        await burgerMenu.clickLogout();
        await expect(loginPage.botonLogin).toBeVisible();
    });
}); 