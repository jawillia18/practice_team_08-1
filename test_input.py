import input
import unittest
from datetime import datetime

class Test_Input(unittest.TestCase):

# Test Username input
    def test_username_corrrect(self):
        self.assertTrue(input.get_username("name"))
    
    def test_username_empty(self):
        self.assertFalse(input.get_username(""))

    def test_username_number(self):
        self.assertFalse(input.get_username(1234))

    def test_username_contain_number(self):
        self.assertFalse(input.get_username("name123"))

    def test_contains_charector(self):
        self.assertFalse(input.get_username("??\/"))

# Test Date input in the format DD/MM/YYYY

    def test_date_correct(self):
        self.assertTrue(input.get_date("09/12/2020"))

    def test_date_no_input(self):
        self.assertFalse(input.get_date(""))

    def test_date_date_passed1(self):
        self.assertFalse(input.get_date("10/13/2021"))

    def test_date_date_passed2(self):
        self.assertFalse(input.get_date("08/8/2010"))

    def test_date_date_and_latters(self):
        self.assertFalse(input.get_date("jk/h/20f"))