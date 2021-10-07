tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

print(tekst)

imie = "Szymon"
Nazwisko = "Kowalski"

litera1 = imie[1]
litera2= Nazwisko[2]

print(tekst.count(litera1))
print(tekst.count(litera2))
print(f"W tekście jest {tekst.count(litera1)} liter {litera1} oraz {tekst.count(litera2)} liter {litera2}")