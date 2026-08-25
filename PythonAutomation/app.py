from playwright.sync_api import sync_playwright
from time import perf_counter


with sync_playwright() as playwright:
    #launch the browser
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)# headless=False to see the browser window, is true by default
    #create a new page
    page = browser.new_page()
    #Visit the playwright website
    print("Page loading...")
    start = perf_counter()
    page.goto("https://playwright.dev/python", wait_until='load')
    
    time_taken = perf_counter() -start
    print(f"... Page loaded in {round(time_taken, 2)}s")
    #locate link element with "Docs" text and click on it
    #page.get_by_label es para buscar o seleccionar partes de la pagina por el label .la accion highlight or click 
    #page.get_by_placeholder toma por el valor que tiene el elemento o definicion que tiene
    #page.get_by_text es seleccionar por el texto que tiene el elemento o el titulo o entre otros, texto de la pagina se coloca , exact=false asi selecciona toda la linea asi coloque uno solo un pedazo del texto no todo
    #page.get_by_alt_text para tomar las imagenes seleccionarlas para esto se debe colocar todo el texto que tiene la imagen
    #page.get_by_tittle para tomar titulos por su tipo hay del tipo attribute 
    #CSS selector page.locator("css=h1").highlight()  page.locator("button.btn-outline-success") name of the class button
    #page.locator("button#btnGroupDrop1") es una busqueda de elementos por el ID
    #page.locator("input[readonly]") para la busqueda de elementos de solo lectura input[value='name of value field']
    
    #docs_button = page.get_by_role('link', name='Get started') #este es mejor para botones o links
    #docs_button.click()
    #Get the URL 
    #print("Docs:",page.url)
    #page.screenshot(path="screenshot.png")
    browser.close()