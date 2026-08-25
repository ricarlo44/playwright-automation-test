import {Locator} from "@playwright/test";
import {Page} from "@playwright/test";

export class BarraTitulo {
    readonly titulo: Locator;

    constructor(page: Page){
        this.titulo = page.getByTestId("title");

    }
}