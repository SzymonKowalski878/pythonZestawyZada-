liczby = list(range(1,11))
print(liczby)
lista2= liczby[5:]
liczby=liczby[:5]
print(liczby)
print(lista2)

liczby = liczby+lista2
print(liczby)
liczby.insert(0,0)
print(liczby)
print(liczby[::-1])