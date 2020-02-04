from selenium import webdriver
from excel_import import ExpressCreating

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

driver.get('https://passport.yandex.uz/auth?from=mail&origin=hostroot_homer_auth_uz&retpath=https%3A%2F%2Fmail.yandex.uz%2F&backpath=https%3A%2F%2Fmail.yandex.uz%3Fnoretpath%3D1')

if __name__ == '__main__':
    main()
