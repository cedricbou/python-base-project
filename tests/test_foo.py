"""Check test build process test case"""
from unittest import TestCase

class TestFoo(TestCase):
    "Dummy test case"

    def test_is_string(self):
        "assert always true"
        self.assertTrue(1 == 1)
