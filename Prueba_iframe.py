from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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
btn_lenguage= driver.find_element(By.XPATH,'//*[@id="main_navbar"]/ul/li[7]/div/a')
btn_lenguage.click()
time.sleep(5)
btn_lenguage.send_keys("Português"+Keys.TAB+Keys.ENTER)


#Se agrega esta funcion de javacript para que haga scroll en la pag
driver.execute_script("window.scrollBy(0, 700);")
time.sleep(3)

#Vuelve al contexto anteior 
driver.switch_to.default_content()

#Hacer scroll hacia arriba
scroll_up = driver.find_element(By.XPATH, "//*[@id='to-top']").click()

#ingresa en  el iframe 2
iframe_national = driver.find_element(By.ID, "frame2")
driver.switch_to.frame(iframe_national)

time.sleep(4)
#cierra la ventana pop-up
close_window =driver.find_element(By.CLASS_NAME, "ab-close-button")
close_window.click()

#interactua con elementos dentro del iframe 
btn_menu = driver.find_element(By.XPATH, "//*[@id='fitt-analytics']/div[2]/div/div/div/div/nav/ul/li[5]/div/button")
btn_menu.click()





time.sleep(10)
driver.quit()
