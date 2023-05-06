"""Module for tests"""
import unittest
import translator

class TestF2EMethod(unittest.TestCase):
    """Tests for french to english"""
    def test_translate_hello(self):
        """For the input Hello"""
        french_text = 'Bonjour'
        transated_text = translator.french_to_english(french_text)
        self.assertEqual(transated_text, 'Hello')

    def test_translate_null(self):
        """For Null Input"""
        french_text = ''
        with self.assertRaises(Exception):
            translator.french_to_english(french_text)

class TestE2FMethod(unittest.TestCase):
    """Tests for english to french"""
    def test_translate_hello(self):
        """For the input Hello"""
        french_text = 'Hello'
        transated_text = translator.english_to_french(french_text)
        self.assertEqual(transated_text, "Bonjour")

    def test_translate_null(self):
        """For Null Input"""
        french_text = ''
        with self.assertRaises(Exception):
            translator.english_to_french(french_text)

if __name__ == '__main__':
    unittest.main()
