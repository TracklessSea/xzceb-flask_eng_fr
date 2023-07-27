"""
This module provides functions for translating text between English and French.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English text to French using MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='en-GB', target='fr-FR')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate French text to English using the MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='fr-FR', target='en-GB')
    english_text = translator.translate(french_text)
    return english_text
    