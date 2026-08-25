import { BasePage } from "./BasePage";
import { Locator, Page } from "@playwright/test";
import { LoginPage } from "./LoginPage";

export class ProductosPage extends BasePage {
    readonly botonProducto: Locator;  //array
    readonly imagenProducto: Locator; //array

    constructor(page: Page) {
        super(page);
        this.botonProducto = page.getByTestId("inventory_item_button");
        this.imagenProducto = page.getByTestId("inventory_item_img");
    }
    async open(){
        await super.open("");
        const loginPage = new LoginPage(this.page);
        await loginPage.rellenarFormulario("standard_user", "secret_blass_academy");
    }
    async agregarTodosItemsCarrito() {
        for(const botonProducto of await this.botonProducto.all()) {
            await botonProducto.click();
        }
    }
    async irDetalleProducto(index: number) {
        await this.imagenProducto.nth(index).click();
    }
}