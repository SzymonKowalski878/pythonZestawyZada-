tekst1 = "tralala"
tekst2= "dsadsadsa"

nowyTekst1 = '{:16.4}'.format(tekst2)+tekst1

print(nowyTekst1)

data={'first':tekst1,'last':nowyTekst1}

print('{first[1]} {last}'.format(**data))

print('{:>16}'.format(tekst1))

print('{:^20}'.format('halo halo'))

p=21.369534324
n=2
print('{number:.{digits}f}'.format(number=p, digits=n))