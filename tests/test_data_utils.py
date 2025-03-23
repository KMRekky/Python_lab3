import unittest
from lib.data_utils import normalize_data

class TestDataUtils(unittest.TestCase):
    def test_normalize_data(self):
        data = [1, 2, 3, 4, 5]
        normalized = normalize_data(data)
        self.assertEqual(normalized, [0.0, 0.25, 0.5, 0.75, 1.0])
