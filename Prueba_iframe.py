from selenium import webdriver
from wsgiref.handlers import format_date_time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#Instaciamos el navegador
driver = webdriver.Chrome()

#ingreamos en la pagina web
driver.get("https://practice-automation.com/iframes/")
driver.maximize_window()


#Se agrega esta funcion de javacript para que haga scroll en la pag
driver.execute_script("window.scrollBy(0, 500);")

#ingresamos dentro del iframe
iframe_selenium = driver.find_element(By.ID, "frame1")
driver.switch_to.frame(iframe_selenium)

time.sleep(5)


#interactuamos con un elemento dentro del iframe
btn_idioma = driver.find_element(By.XPATH,'//*[@id="main_navbar"]/ul/li[7]/div/a')
btn_idioma.click()
time.sleep(5)
btn_idioma.send_keys("Português"+Keys.ARROW_DOWN+Keys.ENTER)

#Se agrega esta funcion de javacript para que haga scroll en la pag
driver.execute_script("window.scrollBy(0, 700);")


time.sleep(10)

driver.quit()
