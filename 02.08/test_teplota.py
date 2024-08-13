# test_teplota.py



teplota = input('Zadej venkovni teplotu:')
teplota = int(teplota)

if teplota > 30:
    print('Je teplo')
elif teplota < 10:
    print('Je zima')
else:
    print('Mirna teplota')

