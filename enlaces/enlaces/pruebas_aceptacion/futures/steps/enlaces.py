from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://www.google.com')


cajaBusqueda = driver.find_element_by_name('q')
cajaBusqueda.send_keys('Google'+ Keys.RETURN)
time.sleep(2)

enlaces = driver.find_elements_by_class_name('r')

def encuentraEnlaces():
    i = 0
    for enlace in enlaces:
        if len(str(enlace.text)) > 0 and i < 5:
            inicioTitulo = str(enlace.get_attribute('innerHTML')).find("LC20lb DKV0Md")
            finTitulo = str(enlace.get_attribute('innerHTML')).find("</h3>")
            finEnlace = str(enlace.get_attribute('innerHTML')).find("ping")

            print("Titulo: {0}".format(str(enlace.get_attribute('innerHTML')[inicioTitulo+15 : finTitulo]) ))
            print("Enlace: {0} \n".format(str(enlace.get_attribute('innerHTML')[9 : finEnlace-2]) ))        
            i+=1

informacionPagina()