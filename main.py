from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://staging-unified.leena.ai/bots/5c25fe9530521e0027a14779/itAutomation/softwares")

time.sleep(8)
driver.quit()

