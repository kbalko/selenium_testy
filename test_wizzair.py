from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# TestCase01: rejestracja uzytkownika za pomoca blednego adresu e-email

firstname = 'Kris'
lastname = 'Nowak'
gender = 'male'
kod = '+48'
telefon = "777112123"
email = 'xxxpl,dd'
haslo = 'Aa123x123'
kraj = "Polska"


class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl#/')


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def testWrongEmail(self):

        driver = self.driver
        wait = WebDriverWait(driver, 60)
        # kliknij zaloguj
        zaloguj_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()
        # kliknij rejestracja
        rejestracja = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Rejestracja "]')))
        rejestracja.click()
        # imie
        fn = wait.until(EC.element_to_be_clickable((By.NAME, 'firstName')))
        fn.send_keys(firstname)
        # nazwisko
        wait.until(EC.element_to_be_clickable((By.NAME, 'lastName'))).send_keys(lastname)
        # plec
        if gender == 'male':
            plec = driver.find_element_by_xpath('//label[@data-test="register-gendermale"]')
            fn.click()
            plec.click()
        else:
            driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]').click()
        # kraj
        driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]').click()
        driver.find_element_by_xpath('//input[@name="phone-number-country-code"]').send_keys(kod)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-test='PL']"))).click()
        # numer telefonu
        driver.find_element_by_xpath('/html/body/div[2]/span/article/div/div/div/form/div[4]/div[2]/div/div[1]/div/label/input').send_keys(telefon)
        # bledny e-mail
        driver.find_element_by_xpath('//input[@data-test="booking-register-email"]').send_keys(email)
        # haslo
        driver.find_element_by_xpath('//input[@data-test="booking-register-password"]').send_keys(haslo)
        # narodowosc
        driver.find_element_by_xpath('//input[@data-test="booking-register-country"]').click()
        # Wyszukaj kraje
        wybor_kraju = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        kraje = wybor_kraju.find_elements_by_tag_name("label")
                # Iteruj po kazdym elemencie w liscie "countries"
        for label in kraje:
            # Wewnatrz "label" znajdz element "strong"
            option = label.find_element_by_tag_name('strong')
            # Jesli tekst elementu jest taki jak zadany w valid_country
            if option.get_attribute("innerText") == kraj:
                option.location_once_scrolled_into_view
                option.click()
                break
        # kliknij akceptacje
        driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"]').click()
        # zarejestruj
        driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]').click()



if __name__ == '__main__':
    unittest.main(verbosity=2)
