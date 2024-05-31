import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/"
           "viewform?usp=send_form")

driver.find_element(By.XPATH, "//input[@aria-label='Email or phone']").send_keys("temp.pycache@gmail.com")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "div .Svhjgc").click()
time.sleep(10)
next_btn = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span')
next_btn.click()
time.sleep(3)
driver.find_element(By.NAME, "Passwd").send_keys("temp.pycache__")
next_btn = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button')
next_btn.click()

time.sleep(6)

time.sleep(3)
driver.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf' and @aria-labelledby='i1']").send_keys("Shubham Sharma")
driver.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf' and @aria-labelledby='i5']").send_keys("7018365818")
driver.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf' and @aria-labelledby='i9']").send_keys("shubham160r@gmail.com")
driver.find_element(By.XPATH, "//textarea[@class='KHxj8b tL9Q4c' and @aria-labelledby='i13']").send_keys("1164, Valencia Tower, Mahagun Mascot, Crossings Republik, UP")
driver.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf' and @aria-labelledby='i17']").send_keys("201016")
driver.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf' and @aria-labelledby='i31']").send_keys("Male")
driver.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf' and @aria-labelledby='i35']").send_keys("GNFPYC")

driver.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf' and @aria-labelledby='i30']").send_keys("31-03-2002")
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()='Add file']").click()
time.sleep(5)

iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'docs.google.com/picker')]")
driver.switch_to.frame(iframe)
time.sleep(3)

driver.find_element(By.ID, "1").click()
time.sleep(3)
file_div = driver.find_element(By.CSS_SELECTOR, ".eizQhe-ObfsIf-mJRMzd-PFprWc.HiaYvf-SfQLQb-jAb3A-AHe6Kc")
file_div.click()
time.sleep(3)
file_div.click()
time.sleep(3)

button = driver.find_element(By.XPATH, "//button[.//span[text()='Insert']]")
button.click()

time.sleep(4)

driver.switch_to.default_content()

time.sleep(2)

submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
submit_button.click()

time.sleep(5)

driver.save_screenshot("confirmation_page.png")

driver.quit()



