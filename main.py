import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD":"parecido a un chiste",
            "BFF":"mejores amigos",
            "CRUSH":"enamorado/a de esa persona",
            "fail":"perder algo",
            "PC":"computador"
}
while True:
    time.sleep(1)
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        time.sleep(1)
        print("significa:",meme_dict[word])
    else:
        time.sleep(1)
        print("esa palabra no se encuentra,intenta con otra o usando mayusculas")
