Integrantes:Natalia Santofimio -Cristian Gonzalez


# pagPelicula -Pruebas automaticas 
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# ------------------- Configuración de rutas -------------------
base_directory = r"C:\Users\Natalia Santofimio\Documents\Natalia tercer semestre\PRUEBAS DE SOFTWARE\Entregables proyecto final\capturasP"
screenshots_directory = os.path.join(base_directory, "screenshots")
os.makedirs(screenshots_directory, exist_ok=True)

# ------------------- Inicializar el navegador -------------------
# Si no necesitas configuraciones especiales, puedes usar Chrome directamente
driver = webdriver.Chrome()

# ------------------- Función para tomar capturas -------------------
def tomar_captura(driver, nombre_paso):
    ruta_captura = os.path.join(screenshots_directory, f"{nombre_paso}.jpg")
    driver.save_screenshot(ruta_captura)
    print(f"Captura guardada en: {ruta_captura}")

# ------------------- Flujo principal de prueba -------------------
try:
    # Abrir la página
    driver.get("https://nataliasc27.github.io/pagPelicula/")
    time.sleep(2)  # Espera para asegurar que la página cargue

    # Llenar el formulario -sin agregar correo
    driver.find_element(By.ID, "userName").send_keys("Juan")
    driver.find_element(By.ID, "userLastName").send_keys("Perez")
    driver.find_element(By.ID, "userAge").send_keys("22")
    #Esperar para evidenciar que datos se agregaron
    time.sleep(3)
    # Tomar captura sobre que datos estan 
    tomar_captura(driver, "formulario_semilleno")

    # Hacer clic en el botón "Ingresar"
    boton_ingresar = driver.find_element(By.XPATH, "//button[text()='Ingresar']")
    boton_ingresar.click()


    # Esperar para ver resultado de la acción y tomas captura a mensaje de campo de correo vacio 
    time.sleep(4)
    tomar_captura(driver, "mensaje para completar campos ")

    driver.find_element(By.ID, "userEmail").send_keys("juan@gmail.com")
    time.sleep(2)
    boton_ingresar = driver.find_element(By.XPATH, "//button[text()='Ingresar']")
    boton_ingresar.click()
    time.sleep(2)
    tomar_captura(driver, "despues_click_ingresar")
    boton_infantil = driver.find_element(By.ID, "btn-infantil")
    boton_infantil.click()
    time.sleep(2)

    # Desplazarse hacia abajo 700px
    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(2)  # espera para que el desplazamiento se note

    # Tomar captura después de desplazarse
    tomar_captura(driver, "pagina_scroll")
    boton = driver.find_element(By.XPATH, "//button[@class='btn btn-success add-to-cart-btn' and @data-title='shrek']")
    boton.click()
    print(f"se agrego pelicula al carrito")
    time.sleep(3)
    
    boton.click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())

    # Capturar y cerrar la alerta
    alert = driver.switch_to.alert
    print(f"Alerta: {alert.text}")

    time.sleep(3)
    # CIERRA LA ALERTA
    alert.accept()  
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2400);")
    time.sleep
    tomar_captura(driver, "pelicula en el carrito")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    # Espera a que el botón sea visible y clickeable
    boton_comedia = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "btn-comedia"))
    )
    boton_comedia.click()
    driver.execute_script("window.scrollTo(0, 700);")
    time.sleep(2)
    boton_dolittle = driver.find_element(By.XPATH, "//button[@class='btn btn-success add-to-cart-btn' and @data-title='Dr Dolittle']")
    boton_dolittle.click()
    print(f"se agrego pelicula al carrito")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 2400);")
    time.sleep(2)
    tomar_captura(driver, "Otra pelicula agregada al carrito")
    time.sleep(4)

    ##Elimina las peliculas 
    vaciar_carrito = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "clearCartBtn"))
    )

    # Hacer clic en el botón "Vaciar carrito"
    vaciar_carrito.click()
    print("Carrito vaciado.")
    tomar_captura(driver, "Carrito vacio")
    time.sleep(2)


    driver.execute_script("window.scrollTo(0, 1900);")
    time.sleep(3)

     # Rellenar campos del formulario
    
    driver.find_element(By.ID, "emailContacto").send_keys("juan@gmail.com")
    driver.find_element(By.ID, "mensajeContacto").send_keys("Muy ineteresante la pagina.")
    #HAcer clic en enviar

    boton_enviar = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary[type="submit"]')
    boton_enviar.click()
    tomar_captura(driver, "mensaje advertencia")
    time.sleep(1)
    

    print("Formulario de contacto incompleto.")
    time.sleep(2)
    #Agrega el nombre

    driver.find_element(By.ID, "nombreContacto").send_keys("Juan Perez")
    time.sleep(1)
    boton_enviar.click()
    print("Formulario enviado .")
   
except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    input("Presiona ENTER para cerrar el navegador...")
    driver.quit()
