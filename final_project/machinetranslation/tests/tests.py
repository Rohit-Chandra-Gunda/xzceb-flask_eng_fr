"""Module for tests"""
import unittest
import translator

class TestF2EMethod(unittest.TestCase):
    """Tests for french to english"""
    def test_assert_equals(self):
        """For the assert equals case"""
        french_text = 'Bonjour'
        transated_text = translator.french_to_english(french_text)
        print('Testing for french to english assert equals case')
        self.assertEqual(transated_text, 'Hello')

    def test_assert_not_equals(self):
        """For the assert not equals case"""
        french_text = 'Bonjour'
        transated_text = translator.french_to_english(french_text)
        print('Testing for french to english assert not equals case')
        self.assertNotEqual(transated_text, 'Good Bye')

    def test_translate_null(self):
        """For Null Input"""
        french_text = None
        print('Testing for french to english null input case')
        with self.assertRaises(Exception):
            translator.french_to_english(french_text)

class TestE2FMethod(unittest.TestCase):
    """Tests for english to french"""
    def test_assert_equals(self):
        """For the assert equals case"""
        french_text = 'Hello'
        transated_text = translator.english_to_french(french_text)
        print('Testing for english to french assert equals case')
        self.assertEqual(transated_text, "Bonjour")

    def test_assert_not_equals(self):
        """For the assert not equals case"""
        french_text = 'Hello'
        transated_text = translator.english_to_french(french_text)
        print('Testing for english to french asset not equals case')
        self.assertNotEqual(transated_text, 'Au revoir')

    def test_translate_null(self):
        """For Null Input"""
        french_text = None
        print('Testing for english to french null input case')
        with self.assertRaises(Exception):
            translator.english_to_french(french_text)

if __name__ == '__main__':
    unittest.main()
