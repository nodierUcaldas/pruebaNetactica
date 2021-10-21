from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#import pandas as pd

#opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\nodierjose\\Documents\\GitHub\\pruebaNetactica\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)


#acomodar a la pantalla
'''
driver.set_window_position(2000,0)
driver.maximize_window()
time.sleep(1)
'''

driver.get('https://www.viajesexito.com/')

#seleccion de la opcion hoteles
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.icon-hotel hoteles'.replace(' ','.'))))\
    .click()

#llenar campo "lugar" busqueda hotel
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#CityPredictive_netactica_hotel')))\
    .send_keys('Miami')

#selecciono el resultado de la busqueda para "miami (USA)"
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/ul[15]/li[1]/a/table/tbody/tr/td[2]')))\
    .click()

#selecciono input "fecha salida"
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#DateFrom_netactica_hotel')))\
    .click()

#selecciono la fecha 16 de noviembre del 2021
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[17]/div[2]/table/tbody/tr[3]/td[2]/a')))\
    .click()

#selecciono la fecha 18 de noviembre del 2021
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[17]/div[1]/table/tbody/tr[3]/td[4]/a')))\
    .click()

#selecciono input "numero pasajeros"
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#txtNumPassengersHoteles')))\
    .click()

#limpio la casilla de pasajeros adultos
casillaVacia = driver.find_element_by_css_selector('input#ddlHotelNumberAdults')
casillaVacia.send_keys(Keys.CONTROL, 'a')
casillaVacia.send_keys(Keys.DELETE)

#adiciono 1 pasajero a 1 habitacion
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#ddlHotelNumberAdults')))\
    .send_keys(1)

#selecciono boton "estamos completos"
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/article[1]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[1]/button')))\
    .click()

#selecciono boton "buscar hotel y reserva"
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/article[1]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[4]/a')))\
    .click()

#selecciono el primer hotel
WebDriverWait(driver, 10)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[7]/div[1]/div[2]/div/div/button')))\
    .click()

#reservo el hotel (varia el id en cada iteracion)
WebDriverWait(driver, 15)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[3]/div[2]/div/div/div[3]/div[2]/div/div[1]/input')))\
    .click()

#rechazo renta de autos y actividades
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[3]/div/div/div[2]/a')))\
    .click()

WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[3]/div/div/div[2]/a')))\
    .click()

#selecciono genero
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/select/option[2]')))\
    .click()

#selecciono nombre del pasajero
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#Travelers_0__FirstName')))\
    .send_keys('Nodier Jose')

#selecciono apellido del pasajero
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#Travelers_0__LastName')))\
    .send_keys('Pineda Villa')

#selecciono numero documento del pasajero
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#Travelers_0__DucumentNumber')))\
    .send_keys('1053771509')

#selecciono dia de nacimiento
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[5]/div[1]/div[1]/select/option[29]')))\
    .click()

#selecciono mes de nacimiento
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[5]/div[1]/div[2]/select/option[10]')))\
    .click()

#selecciono año de nacimiento
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/select/option[67]')))\
    .click()

#selecciono correo
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#ContactEmail')))\
    .send_keys('nodierjose@gmail.com')

#selecciono telefono
WebDriverWait(driver, 5)\
   .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#ContactPhone')))\
    .send_keys('3108664411')

'''
if __name__ == '__main__':
    S=Source("http/",["info1","info2","info3"],[])
    print(S.build_urls(S.domain,S.articles))
'''


