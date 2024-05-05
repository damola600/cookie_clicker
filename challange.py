from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

firstname_input = driver.find_element(By.NAME, value="fName")
firstname_input.send_keys("Rukayat")

lastname_input = driver.find_element(By.NAME, value="lName")
lastname_input.send_keys("Jimoh")

email_input = driver.find_element(By.NAME, value="email")
email_input.send_keys("pythonsmtptest282@gmail.com")

submit_btn = driver.find_element(By.TAG_NAME, value="button")
submit_btn.click()