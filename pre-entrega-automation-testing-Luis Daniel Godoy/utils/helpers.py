from selenium import webdriver
from selenium.webdriver.common.by import By #LLAMAR A LOS SELECTORES
#from selenium.webdriver.common.keys import Keys #PASAR DATOS
#from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():

    #options  = Options()
    #options.add_argument('--start-maximized')

    #instalacion de driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.implicitly_wait(7)
    #time.sleep(7)

    return driver

def login_saucedemo( driver ):

    driver.get(URL)
    
    #INGRESAR LAS CREDENCIALES
    WebDriverWait(driver, 0).until(Ec.element_to_be_clickable((By.NAME,'user-name' ))).send_keys(USERNAME)

    #driver.find_element(By.NAME,'user-name').send_keys(USERNAME)
    driver.find_element(By.NAME,'password').send_keys(PASSWORD)
    driver.find_element(By.ID,'login-button').click()

    #time.sleep(10)