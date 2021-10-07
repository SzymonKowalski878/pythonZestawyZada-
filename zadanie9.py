studenci = [
  (151517,"Szymon Kowalski"),
  (123456,"Andrzej Barszcz"),
  (654321,"Piotr Nowak")
]

print(studenci)

dct = dict((x,y) for x,y in studenci)

print(dct)
dct['age']=24
dct['email']="test@wp.pl"
dct['birthyear']=1990
dct['address']= 'Olsztyn'
print(dct)