# Sele-Cucum-JUnit

## Descripción del proyecto

Proyecto de **pruebas automatizadas con Python** sobre el sitio de práctica [https://www.saucedemo.com/](https://www.saucedemo.com/).

Se automatiza el **login** y la **compra de productos** de tres maneras distintas, para mostrar que el mismo flujo se puede resolver con tres herramientas diferentes:

1. **Selenium puro** (`selenium_acciones.py`): acciones reutilizables.
2. **pytest** (`test_junit_pytest.py`): el equivalente a JUnit en Python.
3. **behave** (`features/`): el equivalente a Cucumber en Python.

Además, `test_online.py` ejecuta la prueba completa de extremo a extremo e imprime un resultado legible.

## Herramientas utilizadas

| Herramienta | Versión / detalle | Uso en el proyecto |
|---|---|---|
| Python | 3.10 o superior | Lenguaje del proyecto |
| Selenium | 4 (con **Selenium Manager**) | Controla Google Chrome y descarga el driver automáticamente |
| pytest | última | Ejecuta las pruebas con `assert` (equivalente a **JUnit**) |
| behave | última | Ejecuta los escenarios Gherkin (equivalente a **Cucumber**) |
| Google Chrome | instalado | Navegador que se automatiza |
| Visual Studio Code | instalado | Editor del proyecto |
| Git | instalado | Subir el proyecto a GitHub |

> **Nota:** **Cucumber** y **JUnit** son herramientas de **Java**. En este proyecto no se usan directamente, sino sus **equivalentes en Python**: `behave` (para Cucumber) y `pytest` (para JUnit).

## Estructura de carpetas

```
Sele-Cucum-JUnit/
├── README.md                        # Este archivo
├── requirements.txt                 # Dependencias: selenium, pytest, behave
├── selenium_acciones.py             # Acciones reutilizables con Selenium puro
├── test_junit_pytest.py             # 4 pruebas con assert (pytest / JUnit)
├── test_online.py                   # Prueba en línea de extremo a extremo
└── features/
    ├── compra.feature               # 3 escenarios en Gherkin (Cucumber)
    ├── environment.py               # Pasos previos/posteriores de behave
    └── steps/
        └── cucumber_behave_steps.py # Definición de los pasos Gherkin
```

## Requisitos previos

- **Python 3.10 o superior** instalado (`python --version`).
- **Google Chrome** instalado.
- **Conexión a internet** (para acceder a saucedemo.com y para que Selenium Manager descargue el driver la primera vez).
- Opcional: **Git**, **VS Code**.

## Instalación (PowerShell, Windows)

```powershell
git clone https://github.com/yersi123/Selenium.git   # Clona el repositorio
cd Selenium                                           # Entra a la carpeta del proyecto
python -m venv venv                                   # Crea el entorno virtual
.\venv\Scripts\Activate.ps1                           # Activa el entorno (aparece "(venv)")
pip install -r requirements.txt                       # Instala selenium, pytest y behave
```

> **Si PowerShell bloquea la activación** con un mensaje de *"running scripts is disabled"*:
>
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
>
> Después vuelve a ejecutar `.\venv\Scripts\Activate.ps1`.

## Ejecución

Con el entorno virtual **activado** (`(venv)` visible en la línea de comandos):

```powershell
python test_online.py                   # Prueba en línea: muestra APROBADO o FALLIDO
pytest test_junit_pytest.py -v -s       # pytest (JUnit): 4 pruebas con assert
behave                                  # behave (Cucumber): 3 escenarios de features/compra.feature
```

## Resultado esperado de cada comando

| Comando | Resultado esperado |
|---|---|
| `python test_online.py` | `RESULTADO: APROBADO` |
| `pytest test_junit_pytest.py -v -s` | `4 passed` |
| `behave` | `3 scenarios passed` |

## Qué se prueba

- **Login correcto** con un usuario válido.
- **Login incorrecto** con una contraseña errónea.
- **Usuario bloqueado** (`locked_out_user`).
- **Compra completa** agregando **3 productos** al carrito y finalizando la orden.

## Datos de prueba

| Campo | Valor |
|---|---|
| Usuario estándar | `standard_user` |
| Contraseña | `secret_sauce` |
| Usuario bloqueado | `locked_out_user` |

> Estas credenciales son **públicas** y las provee el sitio [SauceDemo](https://www.saucedemo.com/) únicamente para practicar automatización. La "compra" es **solo de práctica**: no se realiza ninguna transacción real ni se ingresan datos de pago reales.

## Configuración

- **`PAUSA`** en `selenium_acciones.py`: controla la **velocidad** de la ejecución (segundos de espera entre acciones). Aumenta el valor si quieres ver el navegador más despacio.
- **`crear_driver(headless=True)`**: ejecuta Chrome **sin ventana** (modo headless), útil para correr las pruebas en segundo plano o en un servidor.

## Problemas frecuentes

| Problema | Causa / Solución |
|---|---|
| `behave` lanza `FileNotFoundError` | Falta la carpeta `features/` o `features/steps/`. Verifica que exista `features/compra.feature`, `features/environment.py` y `features/steps/cucumber_behave_steps.py`. |
| `source ./venv/bin/activate` no funciona | Ese comando es de **Linux/Mac**. En **Windows (PowerShell)** usa `.\venv\Scripts\Activate.ps1`. |
| `ModuleNotFoundError: No module named 'selenium'` (o `pytest`/`behave`) | El **entorno virtual no está activo**. Ejecuta `.\venv\Scripts\Activate.ps1` y verifica que aparezca `(venv)` al inicio de la línea. |
| El script se queda **esperando** sin hacer nada | **Selenium Manager** está descargando el driver de Chrome la primera vez (necesita internet). Espera unos segundos; en conexiones lentas puede tardar más. |
