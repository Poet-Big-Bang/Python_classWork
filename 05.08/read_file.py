'''
mode r = read(defolt)
mode w = write
moden a = append
'''



cesta = 'Python/05.08/test_file.txt'
with open(cesta) as file:
    print(file.read())


with open(cesta, mode = 'a') as file:
    file.write('\nHELLO FROM PYTHON')
    