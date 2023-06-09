from googletrans import Translator


def translate_text_to_language(text,lang, source_lang = 'en'):
    try:
        translator = Translator(service_urls=['translate.google.com'])
        translation = translator.translate(text, dest=lang, src=source_lang)
        return translation.text
    except Exception as e:
        print(e)
        return None

print(translate_text_to_language("This plant is affected by a fungal disease called powdery mildew.", "hi", "en"))