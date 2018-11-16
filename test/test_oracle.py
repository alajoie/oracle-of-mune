import unittest
import unittest.mock

from unittest.mock import patch
from src.oracle import Oracle

class TestOracle(unittest.TestCase):

    def test_roll_with_advantage(self):
        with patch.object(Oracle, '_Oracle__roll', side_effect = [1,6]) as mock_roll:
            self.assertEqual(Oracle().ask("Advantage"), 6)

    def test_roll_with_disadvantage(self):
        with patch.object(Oracle, '_Oracle__roll', side_effect = [2,5]) as mock_roll:
            self.assertEqual(Oracle().ask("Disadvantage"), 2)
    def test_roll_normal(self):
        with patch.object(Oracle, '_Oracle__roll', side_effect = [3,4]) as mock_roll:
            Oracle().ask("")
            mock_roll.assert_called_once()

if __name__ == '__main__':
    unittest.main()
    



