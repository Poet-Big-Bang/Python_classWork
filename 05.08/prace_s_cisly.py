uzivatelske_cisla = input('Zadejte libovolny cisla: ')
data = uzivatelske_cisla.split(' ')
data = list(map(int, data))

print('min', min(data))
print('max', max(data))
print('sum', sum(data))
print('prumer', sum(data) / len(data))