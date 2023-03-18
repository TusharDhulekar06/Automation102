from webbrowser import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj=Service("E:\SoftwareTesting\Driver\LatestDriver\chromedriver_win32\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.policybazaar.com/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"sign-in").click()
