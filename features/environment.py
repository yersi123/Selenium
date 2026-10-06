# Archivo 3b: SOLO behave (hooks, equivalentes a @Before / @After de Cucumber)
import os
import sys

# Permite importar selenium_acciones.py desde la carpeta raíz del proyecto
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import selenium_acciones as acc


def before_scenario(context, scenario):
    context.driver = acc.crear_driver()


def after_scenario(context, scenario):
    context.driver.quit()
