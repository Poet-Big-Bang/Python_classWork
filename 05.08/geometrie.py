# vypocet obvodu trouhelniku

hodnoty = input('Zadejte hodnoty trouhelnika:')
data = hodnoty.split(' ')
a,b,c = data
print(int(a) + int(b) + int(c)) #первый вариант
list(map(int, data))