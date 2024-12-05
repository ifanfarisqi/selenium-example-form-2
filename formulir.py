from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

try: 
    driver.get('https://www.techlistic.com/p/selenium-practice-form.html')

    # driver.maximize_window()

    driver.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input').send_keys('Ifan Muhammad')
    driver.find_element(By.CSS_SELECTOR, '#post-body-3077692503353518311 > div:nth-child(1) > div > div > h2:nth-child(2) > div:nth-child(1) > div > div:nth-child(5) > input[type=text]').send_keys('Farisqi')
    driver.find_element(By.ID, 'sex-0').click()
    driver.find_element(By.ID, 'exp-0').click()
    driver.find_element(By.ID, 'datepicker').send_keys('13 Desember 1998')
    driver.find_element(By.ID, 'profession-1').click()
    driver.find_element(By.ID, 'tool-1').click()
    selectBenua = driver.find_element(By.ID, "continents")
    selectBenua.click()
    europe_option = driver.find_element(By.XPATH, "//option[text()='Europe']")
    europe_option.click()
    # driver.find_element(By.ID, 'continents').send_keys('Afrika', Keys.RETURN)
    driver.find_element(By.XPATH, '//*[@id="selenium_commands"]/option[3]').click()
    driver.find_element(By.ID, 'photo').send_keys('/Users/ifanmuhammad/selenium-example-form-2/pict-1.jpg')
    driver.find_element(By.ID, 'submit').click()
    
finally:
    #driver.quit()
    time.sleep(10)