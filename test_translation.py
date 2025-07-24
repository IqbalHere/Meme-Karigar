from translator import translate_text

text = "This is a test. I want to go to school."
translated = translate_text(text, tgt_lang="tel_Telu")  # Telugu

print("Translated:", translated)
