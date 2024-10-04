meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "CRINGE": "algo raro o embarazoso"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print("El significado de la palabra", word, "es", meme_dict[word])
else:
    print("Esta palabra no esta en nuestro diccionario")
