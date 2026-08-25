import {BasePage} from "./BasePage";
import {Locator, Page} from "@playwright/test";
import {ProductosPage} from "./ProductosPage";

export class DetalleProductoPage extends BasePage {
    readonly botonAtras: Locator;
    readonly botonAgregarCarrito: Locator;

    constructor(page: Page) {
        super(page);
        this.botonAtras = page.getByTestId("back-to-products");
        this.botonAgregarCarrito = page.getByTestId("add-to-cart-button");
    }
    async open(index: string) {
        const productosPage = new ProductosPage(this.page);
        await productosPage.open();
        await super.open(`product/${index}`);
    }
    async clickBotonAtras() {
        await this.botonAtras.click();
    }
    async clickAgregarCarrito() {
        await this.botonAgregarCarrito.click();
    }
}