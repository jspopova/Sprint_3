from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click() #Кликнуть на "Зарегистрироваться"
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("Julia Popova") #Ввести Имя
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("popova_julia_4_731@yandex.ru") #Ввести почту
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys("12345") #Ввести пароль
driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/p[1]")))
message_text = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/p[1]").text

assert message_text == 'Некорректный пароль'

driver.quit()