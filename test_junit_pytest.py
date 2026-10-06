# Archivo 2: SOLO pytest (equivalente a JUnit)
# Ejecutar:  pytest test_junit_pytest.py -v -s
import pytest

import selenium_acciones as acc


@pytest.fixture
def driver():
    """Abre el navegador antes de cada prueba y lo cierra al terminar (@BeforeEach / @AfterEach)."""
    driver = acc.crear_driver()
    acc.abrir_pagina(driver)
    yield driver
    driver.quit()


def test_login_correcto(driver):
    acc.hacer_login(driver, acc.USUARIO, acc.CLAVE)
    assert acc.esta_en_productos(driver)


def test_login_incorrecto(driver):
    acc.hacer_login(driver, acc.USUARIO, "clave_mala")
    assert "do not match" in acc.obtener_error(driver)


def test_usuario_bloqueado(driver):
    acc.hacer_login(driver, "locked_out_user", acc.CLAVE)
    assert "locked out" in acc.obtener_error(driver)


def test_compra_completa(driver):
    acc.hacer_login(driver, acc.USUARIO, acc.CLAVE)
    acc.agregar_productos(driver, 3)
    assert acc.cantidad_en_carrito(driver) == 3

    acc.ir_al_carrito_y_checkout(driver)
    acc.llenar_formulario(driver, "Juan", "Perez", "12345")
    assert acc.contar_items_resumen(driver) == 3

    acc.finalizar_compra(driver)
    assert "Thank you for your order" in acc.obtener_mensaje_final(driver)
