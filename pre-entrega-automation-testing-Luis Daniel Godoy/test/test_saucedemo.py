import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import login_saucedemo, get_driver

@pytest.fixture
def driver():
    # configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver ):
    # Logeo de usuario con username y password
    # Click al boton de login
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo  = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'
    driver.save_screenshot('C:/Users/Luis Daniel Godoy/Desktop/pre-entrega-automation-testing-Luis Daniel Godoy/screenshots/test_login.png')
    
def test_catalago( driver ):
    login_saucedemo( driver )

    #verifixar el titulo de la pagina(ventanita)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0
    driver.save_screenshot('C:/Users/Luis Daniel Godoy/Desktop/pre-entrega-automation-testing-Luis Daniel Godoy/screenshots/test_catalago.png')

def test_carrito( driver ):
    login_saucedemo(driver)

    # verificar el titulo pero del html
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0
    
    products[0].find_element(By.TAG_NAME, 'button').click()

    #Comprobar si existen productos en la pagina visibles (len())
    #Verificar elementos importantes de la pagina.
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == "1" 
    driver.save_screenshot('C:/Users/Luis Daniel Godoy/Desktop/pre-entrega-automation-testing-Luis Daniel Godoy/screenshots/test_carrito.png') 

