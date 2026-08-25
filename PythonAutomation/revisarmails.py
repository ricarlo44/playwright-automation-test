from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=".auth/storage_state.json")

    page= context.new_page()
    page.goto("https://gmail.com")

    new_emails = []
    emails = page.locator("div.UI table tr")

    for email in emails.all():
        is_new_email = email.locator("td li[data-tooltip='Marcar como leído']").count() == 1

        if is_new_email: 
            sender = email.locator("td span[email]:visible").inner_text()
            title = email.locator("td span[data-thread-id]:visible").inner_text()

            new_emails.append([sender, title])
    if len(new_emails) == 0:
        print("No new emails📨!")

    else:
        print(f"{len(new_emails)} new emails📨!")
        print("-"*20)

        for new_email in new_emails:
            print(new_email[0], new_email[1])
            print("-"*20)

    context.close()
    
    
    
    
    #--------------------------------------------------------------------------------
    #table= page.locator("div.UI table")
    #emails = table.locator("tr")
    #first_email = emails.first
    #first_email.locator("td span[email]:visible").inner_text() #buscar un correo por lo que dice en el en el destinatario
    #first_email.locator("td span[data-thread-id]:visible")
    #first_email.locator("li[data-tooltip='Mark as read']") localizar los no leidos
    #second_email = emails.last
    #second_email.locator("li[data-tooltip='Mark as unread']") localizar los correos leidos
    #contar los correos que estan leidos y cuales no
    #second_email.locator("li[data-tooltip='Mark as read']").count() contar los correos leidos
    #first_email.locator("li[data-tooltip='Mark as read']").count() contar los correos no leidos
    #table = page.locator("div.UI table tr")
    #page.pause()


    #este codigo es como me logueo a la pagina de accounts en google con mi usuario y contraseña para almacenar el logueo en un .json
    # Increase timeout and wait for element to be visible
    #page.set_default_timeout(60000)  # 60 seconds
    
    #enter el mail
    #email_input = page.get_by_label("Correo electrónico o teléfono")
    #email_input.wait_for(state="visible", timeout=60000)
    #email_input.fill("ricarlo44@gmail.com")

    #page.get_by_role("button", name="Siguiente").click()
   # page.wait_for_load_state("networkidle", timeout=60000)

    #enter password
    #password_input = page.get_by_label("Ingresa tu contraseña")
    #password_input.wait_for(state="visible", timeout=60000)
    #password_input.fill("a3349812*")

    #page.get_by_role("button", name="Siguiente").click()
    #page.wait_for_load_state("networkidle", timeout=60000)

    #page.pause()

    # Create directory if it doesn't exist
    #auth_dir = "QA_AUTOMATION_TEST/venv/.auth"
    #os.makedirs(auth_dir, exist_ok=True)
    
    #context.storage_state(path=".auth/storage_state.json")



