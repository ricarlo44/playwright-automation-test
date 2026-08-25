import {test, expect} from "@playwright/test";
import {BarraTitulo} from "../pages/BarraTitulo";
import {DetalleProductoPage} from "../pages/DetalleProductoPage";
import {BarraSuperior} from "../pages/BarraSuperior";

test.describe("Detalle Producto", () => {
    let detalleProductoPage: DetalleProductoPage;
    let barraTitulo: BarraTitulo;
    let barraSuperior: BarraSuperior;

    test.beforeEach(async ({page}) => {
        detalleProductoPage = new DetalleProductoPage(page);
        barraTitulo = new BarraTitulo(page);
        barraSuperior = new BarraSuperior(page);
        await detalleProductoPage.open("1");
    });
    test("Navegacion Productos", async () => {
        await detalleProductoPage.clickBotonAtras();
        await expect(barraTitulo.titulo).toHaveText("Productos");
    });
    test("Agregar Carrito", async () => {
        await detalleProductoPage.clickAgregarCarrito();
        await expect(barraSuperior.botonCarrito).toHaveText("1");
    });
});