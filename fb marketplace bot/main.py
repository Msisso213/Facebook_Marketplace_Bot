import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

ua = UserAgent()

opts = Options()
opts.add_argument("user-agent="+ua.random)
chrome_options = ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = Chrome(options=chrome_options)
try:
    driver.get("https://www.facebook.com/")
    username = driver.find_element("name", "email")
    username.send_keys("aymenzebentout@outlook.com")
    user = driver.find_element("name", "pass")
    user.send_keys("Silver.213")
    login_boutton = driver.find_element("name", "login")
    login_boutton.send_keys(Keys.ENTER)
    marketplace_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Marketplace"]')))
    marketplace_button.click()
    sleep(5)
    vehicles_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "x1i10hfl")))
    driver.execute_script("arguments[0].scrollIntoView();", vehicles_button)
    vehicles_button.click()
    vehicles_button = driver.find_element(By.CLASS_NAME, "x1i10hfl")
    actions = ActionChains(driver)
    actions.move_to_element(vehicles_button).perform()
    driver.execute_script('arguments[0].style.opacity = 0; arguments[0].style.visibility = "hidden";', driver.find_element(By.CLASS_NAME, "x9f619"),)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "x9f619")))
    vehicles_button.click()
    vehicles_button = driver.find_elements(By.CLASS_NAME, "x1i10hfl")

    if vehicles_button:
        vehicles_button[0].click()
    vehicules_boutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "x1i10hfl")))
    vehicules_boutton.click()
    #try:
        #for i in range(len(vehicule_boutton)):
            #vehicule_boutton[i].click
            #sleep(3)
            #print(i)
    #except:
        #print(i, "n<a pas fonctionne")
    #sleep(5)
    
finally:
    driver.quit()
