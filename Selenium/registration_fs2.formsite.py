from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="Webdriver/chromedriver.exe")

driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
print(driver.title)

driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Sadia Tamim")
driver.find_element(By.NAME, "RESULT_TextField-2").send_keys("Dip")
driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-3']").send_keys("01xxxxxxxxx")
driver.find_element(By.NAME, "RESULT_TextField-4").send_keys("Bangladesh")
driver.find_element(By.NAME, "RESULT_TextField-5").send_keys("Dhaka")
driver.find_element(By.NAME, "RESULT_TextField-6").send_keys("xxx@gmail.com")

driver.find_element(By.XPATH, "//*[@id='q26']/table/tbody/tr[2]/td/label").click()
driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[1]/td/label").click()

dropdown = Select(driver.find_element(By.ID, "RESULT_RadioButton-9"))
dropdown.select_by_index(1)

driver.find_element(By.NAME, "RESULT_FileUpload-10").send_keys("G:\\abc.PNG")

driver.find_element(By.ID, "FSsubmit").click()

time.sleep(5)




