import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://staging-web.leena.ai/v2?clientId=-0S-Ym2PgPz9bKeNP7uoy")
time.sleep(5)
text_field = driver.find_element(By.XPATH, "//textarea[@placeholder='Type a message...']")
driver.implicitly_wait(5)
ActionChains(driver).move_to_element(text_field).click(text_field).perform()
driver.execute_script("""
let wf = document.createElement('script');
wf.src = 'https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js';
wf.type = 'text/javascript';
wf.async = true;
wf.onload = () => {
    WebFont.load({
        google: {
            families: ['Bokor'] // Replace with desired font
        }
    });
    let style = document.createElement('style');
    style.innerHTML = `
        body, * {
            font-family: 'Bokor' !important;
            font-size: 30px !important;
            font-weight: bold !important;
        }
    `;
    document.head.appendChild(style);
};
document.head.appendChild(wf);
""")
time.sleep(10)
text_field.send_keys("Hi Leena, How Are You?")
send_button = driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M8.46154 1')]")
send_button.click()
time.sleep(5)
text_field.send_keys("Hi Leena, How Are You?")
time.sleep(1)
send_button = driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M8.46154 1')]")
send_button.click()
time.sleep(5)
text_field.send_keys("Hi Leena, How Are You?")
time.sleep(1)
send_button = driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M8.46154 1')]")
send_button.click()
time.sleep(5)
text_field.send_keys("Hi Leena, How Are You?")
time.sleep(1)
send_button = driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M8.46154 1')]")
send_button.click()
time.sleep(5)
text_field.send_keys("Hi Leena, How Are You?")
time.sleep(1)
send_button = driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M8.46154 1')]")
send_button.click()
time.sleep(5)
text_field.send_keys("Hi Leena, How Are You?")
time.sleep(1)
send_button = driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M8.46154 1')]")
send_button.click()
time.sleep(5)
"""login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Log In']")  # Adjust XPath as needed
login_button.click()
time.sleep(2)
side_menu = driver.find_element(By.XPATH,"//div[contains(@class,'mainHeader')]//i[contains(@class,'button')]")
side_menu.click()
time.sleep(2)
eventFiringWebdriver = driver.execute_script("document.querySelector('.DrawerNavigation__DrawerStyles-sc-19285hk-0.AMXxv').scrollTop=500")
time.sleep(2)
itautomation = driver.find_element(By.XPATH, "//a[contains(@class,'itAutomation')]//div[contains(@class,'dashboardListItem')]")
itautomation.click()
time.sleep(5)
add_software = driver.find_element(By.XPATH, "//button[normalize-space()='Add software']")
add_software.click()
time.sleep(2)
software_name_field = driver.find_element(By.NAME, "name")
software_name_field.send_keys("New Selenium Test")
software_version_field = driver.find_element(By.NAME, "version")
software_version_field.send_keys("v4.1.0")
operating_system_dropdown = driver.find_element(By.XPATH,"//div[contains(@class,'MuiAutocomplete-root MuiAutocomplete-hasPopupIcon css-pg0de9')]//i[contains(@class,'ph ph-caret-down css-1duve67')]")
operating_system_dropdown.click()
time.sleep(3)
os_option = driver.find_element(By.XPATH,"//input[@id=':r7k:']")
os_option.click()
time.sleep(5)"""
driver.close()


