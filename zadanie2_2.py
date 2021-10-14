text = "Pies na smyczy"


def fuuuun(data):
    dictionary = {
        "length": len(data),
        "letters": list(data),
        "big_letters": data.upper(),
        "small_letters": data.lower(),
    }
    return dictionary


print(fuuuun(text))