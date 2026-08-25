import {Locator} from "@playwright/test";
import {BasePage} from "./BasePage";
import {Page} from "@playwright/test";

export class LoginPage extends BasePage {
    readonly inputUsuario: Locator;
    readonly inputClave: Locator;
    readonly botonLogin: Locator;
    readonly mensajeError: Locator;

    constructor(page: Page) {
        super(page);
        this.inputUsuario = page.getByRole("textbox", {name: "Username"});
        this.inputClave = page.getByRole("textbox", {name: "Password"});
        this.botonLogin = page.getByRole("button", {name: "Login"});
        this.mensajeError = page.getByRole("heading", {level: 3});
    }
    async open(){
        await super.open("");
    }

    async rellenarFormulario(usuario: string, clave: string) {
        await this.inputUsuario.fill(usuario);
        await this.inputClave.fill(clave);
        await this.botonLogin.click();
    }
}