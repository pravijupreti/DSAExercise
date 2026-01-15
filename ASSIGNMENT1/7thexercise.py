def custom_encoder(word):
    word_position = []
    for ch in word:
        ch = ch.lower()
        if "a" <= ch <="z":
            word_position.append(ord(ch) - ord("a"))
        else:
            word_position.append(-1)
    return word_position

custom_encoder("aabaaaacz@")