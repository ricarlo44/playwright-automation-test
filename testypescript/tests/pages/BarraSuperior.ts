import {Locator, Page} from "@playwright/test";

export class BarraSuperior {
    readonly contador: Locator;
    readonly botonBurgerMenu: Locator;
    readonly botonCarrito: Locator;

    constructor(page: Page) {
        this.contador = page.getByTestId("cart-count-badge");
        this.botonBurgerMenu = page.getByTestId("react-burger-menu-btn");
        this.botonCarrito = page.getByTestId("shopping-cart-link");
    }
    async abrirBurgerMenu() {
        await this.botonBurgerMenu.click();
    }
    async hacerCheckout() {
        await this.botonCarrito.click();
    }
}