# language: es
Característica: Compras en SauceDemo

  Escenario: Login correcto
    Dado que abro SauceDemo
    Cuando inicio sesión con "standard_user" y "secret_sauce"
    Entonces veo la página de productos

  Escenario: Login con contraseña incorrecta
    Dado que abro SauceDemo
    Cuando inicio sesión con "standard_user" y "clave_mala"
    Entonces veo un mensaje de error que contiene "do not match"

  Escenario: Comprar tres productos
    Dado que abro SauceDemo
    Cuando inicio sesión con "standard_user" y "secret_sauce"
    Y agrego 3 productos al carrito
    Y completo el formulario con "Juan", "Perez" y "12345"
    Y finalizo la compra
    Entonces veo el mensaje "Thank you for your order"
