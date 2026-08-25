import {test, expect} from "@playwright/test";
import {SusDatosPage} from "../pages/SusDatosPage";
import { BarraTitulo } from "../pages/BarraTitulo";

test.describe("Sus Datos", () => {
    let susDatosPage: SusDatosPage;
    let barraTitulo: BarraTitulo;

    test.beforeEach(async ({page}) => {
        susDatosPage = new SusDatosPage(page);
        barraTitulo = new BarraTitulo(page);
        await susDatosPage.open();
    });
    test("Navegacion Productos", async () => {
        await susDatosPage.clickBotonCancelar();
        await expect(barraTitulo.titulo).toHaveText("Productos");
    });
}); 