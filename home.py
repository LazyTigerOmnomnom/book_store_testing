# 1. Откройте https://practice.automationtesting.in/
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
# 2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
selenium_ruby = driver.find_element_by_tag_name("[title='Selenium Ruby']")
selenium_ruby.click()
# 4. Нажмите на вкладку "REVIEWS"
reviews = driver.find_element_by_css_selector(".reviews_tab > a")
reviews.click()
# 5. Поставьте 5 звёзд
star = driver.find_element_by_css_selector('.stars >span>.star-5')
star.click()
# 6. Заполните поле "Review" сообщением: "Nice book!"
review = driver.find_element_by_id('comment')
review.send_keys('Nice book!')
# 7. Заполните поле "Name"
name = driver.find_element_by_id('author')
name.send_keys('Valeria')
# 8. Заполните "Email"
email = driver.find_element_by_id('email')
email.send_keys('yamada2014@yandex.ru')
# 9. Нажмите на кнопку "SUBMIT"
submit = driver.find_element_by_id('submit')
submit.click()
driver.quit()
