from selenium import webdriver
import selenium # pip install selenium
#chrome driver downloaded and added to path below

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https//techwithtim.net")



