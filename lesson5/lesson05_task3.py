from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")


text_field = driver.find_element(By.CSS_SELECTOR, "input")

text_field.send_keys("100")
text_field.clear()
text_field.send_keys("200")


driver.quit()
