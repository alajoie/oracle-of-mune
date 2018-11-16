import unittest
import unittest.mock

from unittest.mock import patch
from src.acolyte import Acolyte

class TestAcolyte(unittest.TestCase):
    def test_interprets_1_as_No_and(self):
        self.assertEqual(Acolyte().interpret(1), "No, and...")

    def test_interprets_2_as_No(self):
        self.assertEqual(Acolyte().interpret(2), "No.")

    def test_interprets_3_as_No_but(self):
        self.assertEqual(Acolyte().interpret(3), "No, but...")

    def test_interprest_4_as_Yes_but(self):
        self.assertEqual(Acolyte().interpret(4), "Yes, but...")

    def test_interprets_5_as_Yes(self):
        self.assertEqual(Acolyte().interpret(5), "Yes.")

    def test_interprets_6_as_Yes_and(self):
        self.assertEqual(Acolyte().interpret(6), "Yes, and...")

    def test_forced_decisive_yes(self):
        with patch.object(Acolyte, 'get_assertive_counter', return_value = 3) as mock_counter:
            self.assertEqual(Acolyte().interpret(4), "Yes.")

    def test_forced_decisive_no(self):
        with patch.object(Acolyte, 'get_assertive_counter', return_value = 3) as mock_counter:
            self.assertEqual(Acolyte().interpret(3), "No.")

if __name__ == '__main__':
    unittest.main()
