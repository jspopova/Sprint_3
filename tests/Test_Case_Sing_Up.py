import Locators as lc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCaseSingUp:

    driver = webdriver.Chrome()
    link = "https://stellarburgers.nomoreparties.site/"
    locators = lc.Locator()

    def __init__(self):
        self

    def sign_up_with_correct_password(self):

        driver = self.driver
        link = self.link
        lct = self.locators
        driver.get(link)
        driver.find_element(By.XPATH, str(lct.get_locator("btnEnter2Acc"))).click()
        driver.find_element(By.XPATH, str(lct.get_locator("linkSingUp"))).click()  # Клинуть Зарегистрироваться
        driver.find_element(By.XPATH, lct.get_locator("lblUserName")).send_keys("Juls")  # Ввести Имя
        driver.find_element(By.XPATH, lct.get_locator("lblEmail")).send_keys("test_julsmail428@yandex.ru") #Ввести почту
        driver.find_element(By.XPATH, lct.get_locator("lblPwd")).send_keys("Password_123") #Ввести пароль
        driver.find_element(By.XPATH, lct.get_locator("btnSignUp")).click()
        driver.quit()


    def sign_up_with_password_less_6(self):

        driver = self.driver
        link = self.link
        lct = self.locators
        driver.get(link)
        driver.find_element(By.XPATH, str(lct.get_locator("btnEnter2Acc"))).click()
        driver.find_element(By.XPATH, str(lct.get_locator("linkSingUp"))).click()  # Клинуть Зарегистрироваться
        driver.find_element(By.XPATH, lct.get_locator("lblUserName")).send_keys("Julia Popova")  # Ввести Имя
        driver.find_element(By.XPATH, lct.get_locator("lblEmail")).send_keys("popova_julia_4_731@yandex.ru") #Ввести почту
        driver.find_element(By.XPATH, lct.get_locator("lblPwd")).send_keys("12345") #Ввести пароль
        driver.find_element(By.XPATH, lct.get_locator("btnSignUp")).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, lct.get_locator("MsgIncPwd"))))
        message_text = driver.find_element(By.XPATH, lct.get_locator("MsgIncPwd")).text

        assert message_text == 'Некорректный пароль'
        driver.quit()
