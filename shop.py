# 1. Откройте https://practice.automationtesting.in/
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
# 2. Залогиньтесь
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
email = driver.find_element_by_id('username')
email.send_keys('yamada2014@yandex.ru')
password = driver.find_element_by_id('password')
password.send_keys('Kirito123')
register = driver.find_element_by_name('login')
register.click()
# 3. Нажмите на вкладку "Shop"
shop = driver.find_element_by_id('menu-item-40')
shop.click()
# 4. Откройте книгу "HTML 5 Forms"
htm = driver.find_elements_by_css_selector('.woocommerce-LoopProduct-link')
html = driver.find_element_by_tag_name("[title='Mastering HTML5 Forms']")
html.click()
# 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
loading = driver.find_element_by_css_selector('.product_title.entry-title')
loading_text = loading.text # создали переменную, в которую поместим значение атрибута
assert 'HTML5 Forms' in loading_text
driver.quit()
# -----------------------------------------------
# 1. Откройте https://practice.automationtesting.in/
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
# 2. Залогиньтесь
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
email = driver.find_element_by_id('username')
email.send_keys('yamada2014@yandex.ru')
password = driver.find_element_by_id('password')
password.send_keys('Kirito123')
register = driver.find_element_by_name('login')
register.click()
# 3. Нажмите на вкладку "Shop"
shop = driver.find_element_by_id('menu-item-40')
shop.click()
# 4. Откройте категорию "HTML"
HTML = driver.find_element_by_css_selector('.cat-item.cat-item-19 >a')
HTML.click()
# 5. Добавьте тест, что отображается три товара
tovar = driver.find_elements_by_css_selector("ul.products>li")
if len(tovar) == 3:
    print("Отображается 3 товара")
else:
    print("Ошибка, отображается больше нужного!")
driver.quit()
# --------------------------------------------------------------
# 1. Откройте https://practice.automationtesting.in/
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
# 2. Залогиньтесь
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
email = driver.find_element_by_id('username')
email.send_keys('yamada2014@yandex.ru')
password = driver.find_element_by_id('password')
password.send_keys('Kirito123')
register = driver.find_element_by_name('login')
register.click()
# 3. Нажмите на вкладку "Shop"
shop = driver.find_element_by_id('menu-item-40')
shop.click()
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# • Используйте проверку по value
sortirovka = driver.find_element_by_name('orderby')
default_sorting = sortirovka.get_attribute('value')
if default_sorting == 'menu_order':
    print('Выбран вид сортировки Default sorting')
else:
    print('Выбран другой вид сортировки')
# 5. Отсортируйте товары по цене от большей к меньшей
# • в селекторах используйте класс Select
sort = driver.find_element_by_name('orderby').click()
sort_price = driver.find_element_by_css_selector("option:nth-child(6)").click()
# 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
sortirovka = driver.find_element_by_name('orderby')
# 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# • Используйте проверку по value
high_to_low = sortirovka.get_attribute('value')
if high_to_low == 'price-desc':
    print('Выбран вид сортировки  high to low')
else:
    print('Выбран другой вид сортировки')
driver.quit()
    # ----------------------------------------------------------------------------------------------------------------------

# 1. Откройте https://practice.automationtesting.in/
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
# 2. Залогиньтесь
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
email = driver.find_element_by_id('username')
email.send_keys('yamada2014@yandex.ru')
password = driver.find_element_by_id('password')
password.send_keys('Kirito123')
register = driver.find_element_by_name('login')
register.click()
# 3. Нажмите на вкладку "Shop"
shop = driver.find_element_by_id('menu-item-40')
shop.click()
# 4. Откройте книгу "Android Quick Start Guide"
# htm = driver.find_elements_by_css_selector('.woocommerce-LoopProduct-link')
Android = driver.find_element_by_tag_name("[title='Android Quick Start Guide']")
Android.click()
# 5. Добавьте тест, что содержимое старой цены = "₹600.00"
book_old_price = driver.find_element_by_css_selector('.price > del > span')
book_old_price_text = book_old_price.text
assert book_old_price_text == "₹600.00"
# 6. Добавьте тест, что содержимое новой цены = "₹450.00"
book_new_price = driver.find_element_by_css_selector('.price > ins > span')
book_new_price = book_new_price.text
assert book_new_price == "₹450.00"
# 7. Добавьте явное ожидание и нажмите на обложку книги
# • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
Cover = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
Cover.click()
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
close = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
close.click()
driver.quit()
# --------------------------------------------------------------------------------------------------------------------
# 1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
# 2. Нажмите на вкладку "Shop"
shop = driver.find_element_by_id('menu-item-40')
shop.click()
# 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
HTML5 = driver.find_element_by_css_selector("[data-product_id='182']")
HTML5.click()
time.sleep(3)
# 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# • Используйте для проверки assert
shopping = driver.find_element_by_css_selector('.wpmenucart-contents>span.cartcontents')
shopping_text = shopping.text
assert shopping_text == "1 Item"
price = driver.find_element_by_css_selector('.wpmenucart-contents > span.amount')
price_text = price.text
assert price_text == "₹180.00"
# 5. Перейдите в корзину
shopping_btn = driver.find_element_by_class_name('cartcontents')
shopping_btn.click()
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
Subtotal = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal'] .woocommerce-Price-amount"), "₹180.00"))
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
Total = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total  [data-title='Total'] .woocommerce-Price-amount"), "₹183.60"))
driver.quit()
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
# 2. Нажмите на вкладку "Shop"
shop = driver.find_element_by_id('menu-item-40')
shop.click()
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
driver.execute_script("window.scrollBy(0, 300);")
HTML5 = driver.find_element_by_css_selector("[data-product_id='182']")
HTML5.click()
time.sleep(3)
JS_Data = driver.find_element_by_css_selector("[data-product_id='180']")
JS_Data.click()
time.sleep(3)
# 4. Перейдите в корзину
shopping_btn = driver.find_element_by_class_name('cartcontents')
shopping_btn.click()
# 5. Удалите первую книгу
# • Перед удалением добавьте sleep
time.sleep(3)
delete = driver.find_element_by_css_selector(".product-remove>[data-product_id='182']")
delete.click()
# 6. Нажмите на Undo (отмена удаления)
time.sleep(3)
undo = driver.find_element_by_css_selector('.woocommerce-message > a')
undo.click()
# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# • Предварительно очистите поле с помощью локатор_поля.clear()
clear = driver.find_element_by_css_selector(":nth-child(1)>:nth-child(5) input")
clear.clear()
three = driver.find_element_by_css_selector(":nth-child(1)>:nth-child(5) input")
three.send_keys("3")
# 8. Нажмите на кнопку "UPDATE BASKET"
update_basket = driver.find_element_by_name('update_cart')
update_basket.click()
time.sleep(3)
# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
price = driver.find_element_by_css_selector(':nth-child(1)>:nth-child(5) input')
price_3= driver.find_element_by_tag_name("[value='3']")
price_text = price_3.get_attribute("value")
assert price_text == '3'
# 10. Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
time.sleep(3)
apply_coupon = driver.find_element_by_css_selector(".coupon>:nth-child(3)")
apply_coupon.click()
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
alert = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code."))
driver.quit()
# -----------------------------------------------------------------------------------------------------
# 1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
HTML5 = driver.find_element_by_css_selector("[data-product_id='182']")
HTML5.click()
time.sleep(3)
# 4. Перейдите в корзину
shopping_btn = driver.find_element_by_class_name('cartcontents')
shopping_btn.click()
# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
proceed_to_checkout = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a")))
proceed_to_checkout.click()
# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
first_name = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Valeria")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Yamada")
email = driver.find_element_by_id("billing_email")
email.send_keys("yamada2014@yandex.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89115586698")
country = driver.find_element_by_css_selector(".select2-arrow>b")
country.click()
time.sleep(3)
search = driver.find_element_by_id("s2id_autogen1_search")
search.send_keys("Russia")
time.sleep(3)
country_click = driver.find_element_by_css_selector(".select2-match")
country_click.click()
address = driver.find_element_by_tag_name("[placeholder='Street address']")
address.send_keys("Primorskaya 28")
city = driver.find_element_by_tag_name("[autocomplete='address-level2']")
city.send_keys("Severodvinsk")
state = driver.find_element_by_tag_name("[name='billing_state']")
state.send_keys("Severodvinsk")
zip = driver.find_element_by_tag_name("[name='billing_postcode']")
zip.send_keys("123456")
# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()
# 8. Нажмите PLACE ORDER
place_order = driver.find_element_by_id("place_order")
place_order.click()
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
text = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce>:nth-child(1)'), 'Thank you. Your order has been received.'))
# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
payment_method = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-thankyou-order-details>.method>strong'), 'Check Payments'))
driver.quit()