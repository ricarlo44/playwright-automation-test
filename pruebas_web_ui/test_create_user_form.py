import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:8080"

class TestUserRegister:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(BASE_URL)
        self.wait = WebDriverWait(self.driver, 5)
        yield
        self.driver.quit()

    def test_page_title(self):
        assert "Registro" in self.driver.title

    def test_create_user(self):
        username = self.driver.find_element(By.ID, "username")
        email = self.driver.find_element(By.ID, "email")
        button = self.driver.find_element(By.ID, "btn-save")

        username.send_keys("ricardo")
        email.send_keys("ricardo@test.com")
        button.click()

        response = self.wait.until(EC.visibility_of_element_located((By.ID, "message")))

        assert response.text == "Usuario creado exitosamente"
