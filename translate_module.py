translations = {
    'en': {
        "Вы успешно зарегистрировались!" : "You have registered successfully!",
        "Добро пожаловать!" : "Welcome!",
    }
}

def t(text, lang="ru"):
    if lang == "ru":
        return text
    elif lang == "en":
        global translations
        try:
            return translations[lang][text]
        except:
            return text


