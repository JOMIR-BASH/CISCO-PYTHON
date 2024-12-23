def no_espace(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = no_espace(texto)
    texto_al_reves = reverse(texto)
    return texto.lower == texto_al_reves.lower


es_palindromo("amo la paloma")
