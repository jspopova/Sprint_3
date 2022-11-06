from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click() #Нажать кнопку Войти в аккант
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("test_julsmail4@yandex.ru") #Ввести почту
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("Password_123") #Ввести пароль
driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click() #Нажать кнопку Войти
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/a[1]").click() #Кликнуть на  "Личный кабинет"
driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click() #Кликнуть на логотип
driver.quit()