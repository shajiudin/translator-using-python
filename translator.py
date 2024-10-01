from translate import Translator
from requests.exceptions import RequestException

languages = {
    1: "en",
    2: "es",
    3: "pt",
    4: "zh",
}

def user_input():
    return input("Enter the text to translate (or 'exit' to quit): ")

def display_languages():
    print("Available languages:")
    for index, language in languages.items():
        print(f"{index}: {language.capitalize()}")

def target_language():
    while True:
        try:
            selected_lang = int(input("Select a target language (1-4): "))
            if selected_lang not in languages:
                print("Invalid option")
                continue
            return languages[selected_lang]
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def translate_text(text, target_lang):
    try:
        translator = Translator(to_lang=target_lang)
        translation = translator.translate(text)
        print(f"Translated text ({target_lang}): {translation}")
    except RequestException as e:
        print(f"Failed translation request: {str(e)}")
    except Exception as e:
        print(f"Translation failed with error: {str(e)}")

def main():
    while True:
        text_to_translate = user_input()
        if text_to_translate.lower() == "exit":
            print("Exiting the translator.")
            break
        display_languages()
        target_lang = target_language()
        translate_text(text_to_translate, target_lang)

if __name__ == "__main__":
    main()



    


    
