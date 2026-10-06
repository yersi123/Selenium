# Archivo 4: prueba en línea de extremo a extremo contra https://www.saucedemo.com/
# Ejecutar:  python test_online.py
import sys

import selenium_acciones as acc


def verificar(condicion, mensaje):
    if not condicion:
        raise AssertionError(mensaje)


def main():
    driver = acc.crear_driver()
    try:
        print("1. Abriendo", acc.URL)
        acc.abrir_pagina(driver)

        print("2. Iniciando sesión con", acc.USUARIO)
        acc.hacer_login(driver, acc.USUARIO, acc.CLAVE)
        verificar(acc.esta_en_productos(driver), "No llegó a la página de productos")

        print("3. Agregando 3 productos al carrito")
        acc.agregar_productos(driver, 3)
        verificar(acc.cantidad_en_carrito(driver) == 3, "El carrito no tiene 3 productos")

        print("4. Yendo al carrito y al checkout")
        acc.ir_al_carrito_y_checkout(driver)

        print("5. Llenando el formulario")
        acc.llenar_formulario(driver, "Juan", "Perez", "12345")
        verificar(acc.contar_items_resumen(driver) == 3, "El resumen no muestra 3 productos")

        print("6. Finalizando la compra")
        acc.finalizar_compra(driver)
        verificar("Thank you for your order" in acc.obtener_mensaje_final(driver),
                  "No apareció el mensaje de compra exitosa")

        print("\nRESULTADO: APROBADO")
        return 0
    except Exception as error:
        print("\nRESULTADO: FALLIDO ->", error)
        return 1
    finally:
        driver.quit()


if __name__ == "__main__":
    sys.exit(main())
