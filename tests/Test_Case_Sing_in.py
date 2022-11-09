import Locators as lc 
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCaseSingIn:

    driver = webdriver.Chrome()
    link = "https://stellarburgers.nomoreparties.site/"
    locators = lc.Locator()

    def __init__(self):
        self

    def sign_in_by_btn_enter(self):

        driver = self.driver
        link = self.link
        lct = self.locators

        driver.get(link)
        driver.find_element(By.XPATH, str(lct.get_locator("btnEnter2Acc"))).click()
        driver.find_element(By.XPATH, lct.get_locator("lblEmail")).send_keys("test_julsmail4@yandex.ru") #Ввести почту
        driver.find_element(By.XPATH, lct.get_locator("lblPwd")).send_keys("Password_123") #Ввести пароль
        driver.find_element(By.XPATH, lct.get_locator("btnSignIn")).click()
        driver.quit() 

    




    def sign_in_by_registration_form(self):

        driver = self.driver
        link = self.link
        lct = self.locators

        driver.get(link)
        driver.find_element(By.XPATH, str(lct.get_locator("btnEnter2Acc"))).click() #Кликнуть Войти в аккаунт
        driver.find_element(By.XPATH, str(lct.get_locator("linkSingUp"))).click() #Клинуть Зарегистрироваться
        driver.find_element(By.XPATH, str(lct.get_locator("linkSingIn"))).click()  # Клинуть Войти
        driver.find_element(By.XPATH, lct.get_locator("lblEmail")).send_keys("test_julsmail4@yandex.ru") #Ввести почту
        driver.find_element(By.XPATH, lct.get_locator("lblPwd")).send_keys("Password_123") #Ввести пароль
        driver.find_element(By.XPATH, lct.get_locator("btnSignIn")).click()
        driver.quit()


    def sign_in_by_recover_password(self):

        driver = self.driver
        link = self.link
        lct = self.locators

        driver.get(link)
        driver.find_element(By.XPATH, str(lct.get_locator("btnEnter2Acc"))).click() #Кликнуть Войти в аккаунт
        driver.find_element(By.XPATH, str(lct.get_locator("linkRcwPwd"))).click() #Клинуть Восстановить пароль
        driver.find_element(By.XPATH, str(lct.get_locator("linkSingIn"))).click()  # Клинуть Войти
        driver.find_element(By.XPATH, lct.get_locator("lblEmail")).send_keys("test_julsmail4@yandex.ru") #Ввести почту
        driver.find_element(By.XPATH, lct.get_locator("lblPwd")).send_keys("Password_123") #Ввести пароль
        driver.find_element(By.XPATH, lct.get_locator("btnSignIn")).click()
        driver.quit()


    def sign_in_from_personal_account(self):

        driver = self.driver
        link = self.link
        lct = self.locators

        driver.get(link)
        driver.find_element(By.XPATH, str(lct.get_locator("link2lk"))).click()  # Кликнуть на Личный кабинет
        driver.find_element(By.XPATH, lct.get_locator("lblEmail")).send_keys("test_julsmail4@yandex.ru") #Ввести почту
        driver.find_element(By.XPATH, lct.get_locator("lblPwd")).send_keys("Password_123") #Ввести пароль
        driver.find_element(By.XPATH, lct.get_locator("btnSignIn")).click()
        driver.quit()

