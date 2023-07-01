from langdetect import detect
from langcodes import Language

text = input("enter text:")
language_code = detect(text)
language = Language.get(language_code)
language_full_name = language.display_name()

print("Detected language: ", language_full_name)
