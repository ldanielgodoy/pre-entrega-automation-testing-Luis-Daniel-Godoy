import pytest




@pytest.fixture

def test_driver():
    # Configuracion para cosultar a selenium web driver

def test_login():
    # assert

    # logeo de usuario con username y password
    # Click al boton de login
    # Navegar a la página de login de saucedemo.com
    # Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
    # Validar login exitoso verificando que se haya redirigido a la página de inventario
    # Verificar que el título de la página de inventario sea correcto (ventana)

def test_catalogo():

    # logeo de usuario con username y password
    # Click al boton de login
    # Verificar el titulo del htmal
    # Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno) mediante la funcion len()
    # Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

def test_carrito():

    # logeo de usuario con username y password
     # Click al boton de login
    # Añadir un producto al carrito haciendo clic en el botón correspondiente
    # Verificar que el contador del carrito se incremente correctamente
    # Navegar al carrito de compras
    # Comprobar que el producto añadido aparezca correctamente en el carrito