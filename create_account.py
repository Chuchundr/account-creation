import time
from selenium import webdriver
from excel_import import ExpressCreating
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

driver.get('https://connect.yandex.com/portal/admin')

login = driver.find_element_by_name('login')
login.send_keys('ffazildjanov@texnomart.uz')
submit1 = driver.find_element_by_xpath("//button[@class='control button2 button2_view_classic button2_size_l button2_theme_action button2_width_max button2_type_submit passp-form-button']")
submit1.click()
time.sleep(1)

passwd = driver.find_element_by_id('passp-field-passwd')
passwd.send_keys('123qwe!@#')
submit2 = driver.find_element_by_xpath("//button[@class='control button2 button2_view_classic button2_size_l button2_theme_action button2_width_max button2_type_submit passp-form-button']")
submit2.click()
time.sleep(5)

add = driver.find_element_by_xpath("//button[@class='ui-flat-button ui-flat-button__width_available plus-button']")
add.click()

add_user = driver.find_element_by_class_name('menu-item menu-item_theme_islands i-bem menu-item_js_inited')


if __name__ == '__main__':
    main()
