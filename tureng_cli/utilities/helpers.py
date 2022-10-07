from .constants import BASE_URL_TR, SENTENCE_URL_EN, SYNONYM_URL_EN


def get_turkish_translate_url(word):
    return BASE_URL_TR + word


def get_english_sentence_url(word):
    return SENTENCE_URL_EN + word


def get_english_synonym_url(word):
    return SYNONYM_URL_EN + word
