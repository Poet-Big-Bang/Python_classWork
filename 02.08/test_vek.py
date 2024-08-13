#testvek.py

vek = input('Zadej svuj vek: ')
vek = int(vek)

print('Zadal jsi:', vek)

if vek < 18:
    print('jsi mladej')
elif vek == 18:
    print('Jsi cerstve dospely')
else:
    print('jsi dospely')



print(type(vek))

