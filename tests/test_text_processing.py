import unittest
from lib.text_processing import to_uppercase, word_count

class TestTextProcessing(unittest.TestCase):
    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("cześć"), "CZEŚĆ")

    def test_word_count(self):
        self.assertEqual(word_count("Ten tekst to test"), 4)
