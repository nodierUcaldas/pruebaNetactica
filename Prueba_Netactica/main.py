from selenium import webdriver
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


WebDriverWait(driver, 5)
content = driver.find_element_by_css_selector('span.icon-hotel hoteles'.replace(' ','.'))
content.click()


'''
if __name__ == '__main__':
    S=Source("http/",["info1","info2","info3"],[])
    print(S.build_urls(S.domain,S.articles))
'''


