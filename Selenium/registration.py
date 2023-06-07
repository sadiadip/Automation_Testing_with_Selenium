from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://nxtgenaiacademy.com/demo-site/")
print(driver.title)

driver.find_element(By.NAME,"vfb-5").send_keys("Sadia Tamim")
driver.find_element(By.NAME,"vfb-7").send_keys("Dip")
driver.find_element(By.ID,"vfb-31-2").click()
driver.find_element(By.ID,"vfb-13-address").send_keys("Dhaka, Bangladesh")
driver.find_element(By.NAME,"vfb-13[address-2]").send_keys("Shukrabad")



driver.find_element(By.ID,"vfb-14").send_keys("xz@gmail.com")
time.sleep(5)

driver.find_element(By.NAME, "vfb-18").send_keys("06/1/2023")
driver.find_element(By.NAME, "vfb-18").send_keys(Keys.ENTER)

driver.find_element(By.XPATH, "//*[@id='item-vfb-16']/span[1]/span/span[1]/span/span[2]").click()
driver.find_element(By.XPATH, "/html/body/span[2]/span/span[1]/input").send_keys("10")
driver.find_element(By.XPATH, "/html/body/span[2]/span/span[1]/input").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.NAME,"vfb-19").send_keys("01555555555")
driver.find_element(By.ID,"vfb-20-0").click()
driver.find_element(By.ID,"vfb-20-4").click()
driver.find_element(By.ID,"vfb-20-5").click()
driver.find_element(By.ID,"vfb-23").send_keys("what is next?")
driver.find_element(By.ID,"vfb-3").send_keys("99")
driver.find_element(By.NAME,"vfb-submit").click()


time.sleep(5)