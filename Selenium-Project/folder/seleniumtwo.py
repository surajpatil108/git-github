import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chromedriver_path = "/usr/local/bin/chromedriver"



driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.maximize_window()

# driver.get("https://testautomationpractice.blogspot.com/")
driver.get("https://www.facebook.com/")

# driver.execute_script("window.scrollTo(0, 1000)")

username = driver.find_element(By.XPATH, "//input[@id='email']")
username.click()
username.send_keys("wretewrgthg")

password = driver.find_element(By.XPATH, "//*[@type='password']")
password.click()
password.send_keys("1234578")

submit = driver.find_element(By.XPATH, '//*[@type="submit"]')
submit.click()


# driver.switch_to_frame(0)
# driver.switch_to.frame(0)
driver.switch_to.frame(0)

