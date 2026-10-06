# Archivo 1: SOLO Selenium
# Acciones reutilizables sobre https://www.saucedemo.com/
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.saucedemo.com/"
USUARIO = "standard_user"
CLAVE = "secret_sauce"
PAUSA = 1.5  # Segundos entre acciones: súbelo para ir más lento, bájalo para ir más rápido

PRODUCTOS = [
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-bike-light",
    "add-to-cart-sauce-labs-fleece-jacket",
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-onesie",
    "add-to-cart-test.allthethings()-t-shirt-(red)",
]


def pausa():
    time.sleep(PAUSA)


def crear_driver(headless=False):
    """Crea el navegador Chrome. Selenium Manager descarga el driver solo."""
    opciones = Options()
    if headless:
        opciones.add_argument("--headless=new")  # Ejecutar sin abrir ventana
    opciones.add_argument("--window-size=1920,1080")
    opciones.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,  # Quita el aviso "Cambia tu contraseña"
    })
    return webdriver.Chrome(options=opciones)


def esperar(driver, segundos=10):
    return WebDriverWait(driver, segundos)


def abrir_pagina(driver):
    driver.get(URL)
    esperar(driver).until(EC.presence_of_element_located((By.ID, "login-button")))
    pausa()


def hacer_login(driver, usuario, clave):
    esperar(driver).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(usuario)
    pausa()
    driver.find_element(By.ID, "password").send_keys(clave)
    pausa()
    driver.find_element(By.ID, "login-button").click()
    pausa()


def esta_en_productos(driver):
    esperar(driver).until(EC.url_contains("inventory"))
    return "inventory" in driver.current_url


def obtener_error(driver):
    error = esperar(driver).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    return error.text


def agregar_productos(driver, cantidad):
    for producto in PRODUCTOS[:cantidad]:
        esperar(driver).until(EC.element_to_be_clickable((By.ID, producto))).click()
        pausa()


def cantidad_en_carrito(driver):
    return int(driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)


def ir_al_carrito_y_checkout(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    pausa()
    esperar(driver).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    pausa()


def llenar_formulario(driver, nombre, apellido, postal):
    esperar(driver).until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(nombre)
    driver.find_element(By.ID, "last-name").send_keys(apellido)
    driver.find_element(By.ID, "postal-code").send_keys(postal)
    pausa()
    driver.find_element(By.ID, "continue").click()
    esperar(driver).until(EC.url_contains("checkout-step-two"))
    pausa()


def contar_items_resumen(driver):
    return len(driver.find_elements(By.CLASS_NAME, "cart_item"))


def finalizar_compra(driver):
    esperar(driver).until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    pausa()


def obtener_mensaje_final(driver):
    mensaje = esperar(driver).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    return mensaje.text
