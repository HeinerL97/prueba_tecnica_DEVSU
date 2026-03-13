import allure

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.purchase_page import PurchasePage

from utils.screenshot import take_screenshot


#@allure.feature("Compra Demoblaze")
#@allure.epic("Ecommerce Automation")
@allure.title("Flujo completo de compra Demoblaze")
def test_purchase_flow(driver):

    driver.get("https://www.demoblaze.com")

    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    purchase = PurchasePage(driver)

    with allure.step("Seleccionar primer producto"):
        home.select_phone()
        take_screenshot(driver, "Producto seleccionado")

    with allure.step("Agregar producto al carrito"):
        product.add_product()
        take_screenshot(driver, "Producto agregado")

    with allure.step("Volver al home"):
        product.return_home()
        take_screenshot(driver, "Volver al home")

    with allure.step("Seleccionar laptop"):
        home.select_laptop()
        take_screenshot(driver, "Laptop seleccionada")

    with allure.step("Agregar laptop"):
        product.add_product()
        take_screenshot(driver, "Laptop agregada")

    with allure.step("Abrir carrito"):
        cart.open_cart()
        take_screenshot(driver, "Carrito abierto")

    with allure.step("Realizar orden"):
        cart.place_order()
        take_screenshot(driver, "Formulario de compra")

    with allure.step("Completar compra"):
        purchase.confirm_purchase()
        take_screenshot(driver, "Compra completada")