import {test, expect} from "@playwright/test";
import {BarraSuperior} from "../pages/BarraSuperior";
import {ProductosPage} from "../pages/ProductosPage";

test.describe("Producto", () => {
    let productosPage: ProductosPage;
    let barraSuperior: BarraSuperior;

    test.beforeEach(async ({page}) => {
        productosPage = new ProductosPage(page);
        barraSuperior = new BarraSuperior(page);
        await productosPage.open();
    });
    test("Agregar Todos Carrito", async () => {
        await productosPage.agregarTodosItemsCarrito();
        await expect.soft(barraSuperior.contador).toHaveText("16");
    });
}); 