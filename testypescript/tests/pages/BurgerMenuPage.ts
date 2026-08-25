import {Locator, Page} from "@playwright/test";
import {BasePage} from "./BasePage";
import {ProductosPage} from "./ProductosPage";
import {BarraSuperior} from "./BarraSuperior";

export class BurgerMenu extends BasePage {
    readonly botonLogout: Locator;

    constructor(page: Page) {
        super(page);
        this.botonLogout = page.getByRole("button", { name: "Logout" });
    }
    async open() {
        const productosPage = new ProductosPage(this.page);
        await productosPage.open();
        const barraSuperior = new BarraSuperior(this.page);
        await barraSuperior.abrirBurgerMenu();
    }
    async clickLogout() {
        await this.botonLogout.click();
    }
}