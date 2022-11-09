import Locators as lc
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCaseGoToPersAcc:

    driver = webdriver.Chrome()
    link = "https://stellarburgers.nomoreparties.site/"
    locators = lc.Locator()

    def __init__(self):
        self


    def go_to_pers_acc(self):

        driver = self.driver
        link = self.link
        lct = self.locators
        driver.get(link)
        driver.find_element(By.XPATH, str(lct.get_locator("btnEnter2Acc"))).click()  # Кликнуть Войти в аккаунт
        driver.find_element(By.XPATH, lct.get_locator("lblEmail")).send_keys("test_julsmail4@yandex.ru") #Ввести почту
        driver.find_element(By.XPATH, lct.get_locator("lblPwd")).send_keys("Password_123") #Ввести пароль
        driver.find_element(By.XPATH, lct.get_locator("btnSignIn")).click() #Нажать Войти
        driver.find_element(By.XPATH, str(lct.get_locator("link2lk"))).click()  # Кликнуть на Личный кабинет
        driver.quit()



    def go_from_pers_acc_to_logo(self):
        driver = self.driver
        link = self.link
        lct = self.locators
        driver.get(link)
        driver.find_element(By.XPATH, str(lct.get_locator("btnEnter2Acc"))).click()  # Кликнуть Войти в аккаунт
        driver.find_element(By.XPATH, lct.get_locator("lblEmail")).send_keys("test_julsmail4@yandex.ru") #Ввести почту
        driver.find_element(By.XPATH, lct.get_locator("lblPwd")).send_keys("Password_123") #Ввести пароль
        driver.find_element(By.XPATH, lct.get_locator("btnSignIn")).click() #Нажать Войти
        driver.find_element(By.XPATH, str(lct.get_locator("link2lk"))).click()  # Кликнуть на Личный кабинет
        driver.find_element(By.XPATH, str(lct.get_locator("Logo"))).click()

        driver.quit()



    def exit_from_pers_acc(self):
        driver = self.driver
        link = self.link
        lct = self.locators
        driver.get(link)
        driver.find_element(By.XPATH, str(lct.get_locator("btnEnter2Acc"))).click()  # Кликнуть Войти в аккаунт
        driver.find_element(By.XPATH, lct.get_locator("lblEmail")).send_keys("test_julsmail4@yandex.ru") #Ввести почту
        driver.find_element(By.XPATH, lct.get_locator("lblPwd")).send_keys("Password_123") #Ввести пароль
        driver.find_element(By.XPATH, lct.get_locator("btnSignIn")).click() #Нажать Войти
        driver.find_element(By.XPATH, str(lct.get_locator("link2lk"))).click()  # Кликнуть на Личный кабинет
        driver.find_element(By.XPATH, str(lct.get_locator("btnExit"))).click()  #Кликнуть на кнопку Выход
        driver.quit()



    def go_from_pers_acc_to_constructor(self):
        driver = self.driver
        link = self.link
        lct = self.locators
        driver.get(link)
        driver.find_element(By.XPATH, str(lct.get_locator("btnEnter2Acc"))).click()  # Кликнуть Войти в аккаунт
        driver.find_element(By.XPATH, lct.get_locator("lblEmail")).send_keys("test_julsmail4@yandex.ru") #Ввести почту
        driver.find_element(By.XPATH, lct.get_locator("lblPwd")).send_keys("Password_123") #Ввести пароль
        driver.find_element(By.XPATH, lct.get_locator("btnSignIn")).click() #Нажать Войти
        driver.find_element(By.XPATH, str(lct.get_locator("link2lk"))).click()  # Кликнуть на Личный кабинет
        driver.find_element(By.XPATH, str(lct.get_locator("builder"))).click() #Перейти в коснтруктор
        driver.quit()


    def go_to_tabs_from_constructor(self):
        driver = self.driver
        link = self.link
        lct = self.locators
        driver.get(link)
        driver.find_element(By.XPATH, str(lct.get_locator("btnEnter2Acc"))).click()  # Кликнуть Войти в аккаунт
        driver.find_element(By.XPATH, lct.get_locator("lblEmail")).send_keys("test_julsmail4@yandex.ru") #Ввести почту
        driver.find_element(By.XPATH, lct.get_locator("lblPwd")).send_keys("Password_123") #Ввести пароль
        driver.find_element(By.XPATH, lct.get_locator("btnSignIn")).click() #Нажать Войти
        driver.find_element(By.XPATH, str(lct.get_locator("link2lk"))).click()  # Кликнуть на Личный кабинет
        driver.find_element(By.XPATH, str(lct.get_locator("builder"))).click() #Перейти в конструктор
        driver.find_element(By.XPATH, str(lct.get_locator("spnSouce"))).click()  # Перейти на вкладку Соусы
        driver.find_element(By.XPATH, str(lct.get_locator("spnBread"))).click()  # Перейти на вкладку Булки
        driver.find_element(By.XPATH, str(lct.get_locator("spnFills"))).click()  # Перейти на вкладку Начинки
        driver.quit()
