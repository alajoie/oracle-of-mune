import unittest
import unittest.mock

from unittest.mock import patch
from src.acolyte import Acolyte

class TestAcolyte(unittest.TestCase):
    def test_interprets_2_as_No(self):
        self.assertEqual(Acolyte().interpret(2), "No.")

    def test_interprets_5_as_Yes(self):
        self.assertEqual(Acolyte().interpret(5), "Yes.")

    def test_forced_decisive_yes(self):
        with patch.object(Acolyte, 'get_assertive_counter', return_value = 3) as mock_counter:
            self.assertEqual(Acolyte().interpret(4), "Yes.")

if __name__ == '__main__':
    unittest.main()
