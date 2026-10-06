# Archivo 3a: SOLO behave (pasos de los escenarios, equivalentes a las step definitions de Cucumber)
from behave import given, when, then

import selenium_acciones as acc


@given('que abro SauceDemo')
def paso_abrir(context):
    acc.abrir_pagina(context.driver)


@when('inicio sesión con "{usuario}" y "{clave}"')
def paso_login(context, usuario, clave):
    acc.hacer_login(context.driver, usuario, clave)


@when('agrego {cantidad:d} productos al carrito')
def paso_agregar(context, cantidad):
    acc.agregar_productos(context.driver, cantidad)
    acc.ir_al_carrito_y_checkout(context.driver)


@when('completo el formulario con "{nombre}", "{apellido}" y "{postal}"')
def paso_formulario(context, nombre, apellido, postal):
    acc.llenar_formulario(context.driver, nombre, apellido, postal)


@when('finalizo la compra')
def paso_finalizar(context):
    acc.finalizar_compra(context.driver)


@then('veo la página de productos')
def paso_ver_productos(context):
    assert acc.esta_en_productos(context.driver)


@then('veo un mensaje de error que contiene "{texto}"')
def paso_ver_error(context, texto):
    assert texto in acc.obtener_error(context.driver)


@then('veo el mensaje "{texto}"')
def paso_ver_mensaje(context, texto):
    assert texto in acc.obtener_mensaje_final(context.driver)
