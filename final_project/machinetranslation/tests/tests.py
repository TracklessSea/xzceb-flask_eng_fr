import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french_hello(self):
        # Test translation of the word 'Hello' from English to French
        english_text = "Hello"
        expected_french_text = "Bonjour"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_french_text)

    def test_english_to_french_bonjour(self):
        # Test translation of the word 'Bonjour' from English to French
        english_text = "Hello"
        expected_french_text = "Hi"  # 'Hi' should fail this test as the result should be 'Bonjour'
        translated_text = english_to_french(english_text)
        self.assertNotEqual(translated_text, expected_french_text)

    def test_french_to_english_bonjour(self):
        # Test translation of the word 'Bonjour' from French to English
        french_text = "Bonjour"
        expected_english_text = "Hello"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_english_text)

    def test_french_to_english_hello(self):
        # Test translation of the word 'Bonjour' from French to English
        french_text = "Bonjour"
        expected_english_text = "Bon"  # 'Bon' should fail this test as the result should be 'Hello'
        translated_text = french_to_english(french_text)
        self.assertNotEqual(translated_text, expected_english_text)

if __name__ == "__main__":
    unittest.main()
    