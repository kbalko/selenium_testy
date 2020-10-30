from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from data_reader import data_reader
import unittest
from ddt import ddt, data, unpack
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(THIS_DIR, '..', 'data/invalid_emails_regist.csv')

@ddt
class RegistrationTest(BaseTest):

    @data(*data_reader.get_data(file_path))
    @unpack
    def test_incorrect_email(self, name, surname, country_code, phone, invalid_email, password, country, gender):
        hp = HomePage(self.driver)
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.click_register_btn()
        rp = RegisterPage(self.driver)
        rp.fill_name(name)
        rp.fill_surname(surname)
        rp.choose_gender(gender)
        rp.choose_country_code(country_code)
        rp.fill_telephone(phone)
        rp.fill_email(invalid_email)
        rp.fill_password(password)
        rp.choose_nationality(country)
        rp.accept_privacy_policy()
        rp.verify_visible_errors(1, ["Nieprawidłowy adres e-mail"])

if __name__=="__main__":
    unittest.main(verbosity=2)