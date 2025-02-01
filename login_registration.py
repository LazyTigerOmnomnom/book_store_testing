# 1. Откройте https://practice.automationtesting.in/
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
# 2. Нажмите на вкладку "My Account"
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
# 3. В разделе "Register", введите email для регистрации
email = driver.find_element_by_id('reg_email')
email.send_keys('yamada2014@yandex.ru')
# 4. В разделе "Register", введите пароль для регистрации
password = driver.find_element_by_id('reg_password')
password.send_keys('Kirito123')
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
# 5. Нажмите на кнопку "Register"
register = driver.find_element_by_css_selector('.woocomerce-FormRow.form-row >.woocommerce-Button.button')
register.click()
driver.quit()
# --------------------------

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
# 2. Нажмите на вкладку "My Account"
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
# 3. В разделе "Login", введите email для логина
email = driver.find_element_by_id('username')
email.send_keys('yamada2014@yandex.ru')
# 4. В разделе "Login", введите пароль для логина
password = driver.find_element_by_id('password')
password.send_keys('Kirito123')
# 5. Нажмите на кнопку "Login"
register = driver.find_element_by_name('login')
register.click()
# Добавьте проверку, что на странице есть элемент "Logout"
btn_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout"), "Logout"))
driver.quit()