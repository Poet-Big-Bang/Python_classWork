uzivatelske_cislo = input('Zadejte jednu stranu ctvrce: ')

je_cislo = uzivatelske_cislo.isdecimal()

if je_cislo:
    integer = int(uzivatelske_cislo)

    if integer > 0:
        print(integer * 4)
        print(integer * integer)
    else: 
        print("Neplatna hodnota, zadejte kladne cislo")
else: 
    print("Neplatna hodnota, zadejte kladne cislo")




