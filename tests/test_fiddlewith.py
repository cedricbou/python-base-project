"""Unit Testing for Fiddlewith"""
from unittest import TestCase
from fiddlewith.calc import Calculator

class TestCalculator(TestCase):
    "Unit Testing class for FiddleWith"

    def test_add(self):
        "test for add"
        calc = Calculator()
        self.assertTrue(calc.add(3, 2) == 5)
