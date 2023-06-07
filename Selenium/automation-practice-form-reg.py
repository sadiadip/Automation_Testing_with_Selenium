from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="Webdriver/chromedriver.exe")
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
print(driver.title)

driver.find_element(By.ID,"firstName").send_keys("Sadia")
time.sleep(1)
driver.find_element(By.ID,"lastName").send_keys("Dip")
time.sleep(1)
driver.find_element(By.ID,"userEmail").send_keys("wzy@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='genterWrapper']/div[2]/div[2]/label").click()
time.sleep(1)
driver.find_element(By.ID,"userNumber").send_keys("0111111111")
driver.find_element(By.ID,"dateOfBirthInput").send_keys("4 May 2023")
driver.find_element(By.ID,"dateOfBirthInput").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='subjectsContainer']/div/div[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='hobbiesWrapper']/div[2]/div[2]/label").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='hobbiesWrapper']/div[2]/div[3]/label").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='uploadPicture']").send_keys("G:\\abc.PNG")
time.sleep(1)
driver.find_element(By.ID,"currentAddress").send_keys("Bangladesh")
time.sleep(1)

time.sleep(5)