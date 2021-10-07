lista = [
  {1:"halo",2:"Hej"},
  {"haha":"aha"},
  {"tururu":"wonsz"}
]

output = ""

for i in lista:
  for k in i:
    output=output+" "+str(k)+" "+i[k]+" "

print(output)