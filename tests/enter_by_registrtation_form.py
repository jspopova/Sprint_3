from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click() #Кликнуть Зарегистироваться
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("test_julsmail4@yandex.ru") #Ввести почту
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("Password_123") #Ввести пароль
driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click() #Нажать Войти
driver.quit()