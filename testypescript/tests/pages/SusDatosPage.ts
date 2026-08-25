import {BasePage} from "./BasePage";
import {Locator, Page} from "@playwright/test";
import {ProductosPage} from "./ProductosPage";

export class SusDatosPage extends BasePage{
    readonly botonCancelar: Locator;
    
    constructor(page: Page) {
        super(page);
        this.botonCancelar = page.getByRole("button", { name: "Cancelar" });
    }
    async open(){
        const productosPage = new ProductosPage(this.page);
        await productosPage.open();
        await super.open("your-data");
    }

    async clickBotonCancelar(){
        await this.botonCancelar.click();
    }
}
