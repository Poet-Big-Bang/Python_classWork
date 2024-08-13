"""
dame uzivateli na vyber
1 - pro login
2 - pro sign upp


pokud zada 1
- pozadame jej o username a heslo
- zkontrolujeme zda existuje soubor pro uzivatele,
pokud ano tak jej otevreme a nacteme obsah souboru ve kterem je heslo
a porovname s tim heslem co zada uzivatel

pokud zada 2
- pozadame jej o username a heslo
- zkontrolujeme zda existuje soubor pro uzivatele,
pokud ano tak mu oznamime ze toto uzivatelske jmeno neklze pouzit
jinak me vytvorime soubor s uzivatelskym jmenem a zapiseme do nej heslo
"""


import os

def get_user_data():
    username = input('Zadejte uzivatelske jmeno: ')
    password = input('Zadejte heslo: ')
    return[username, password]


def get_user_filename(username):
    filename = username + '.txt'
    filename = os.path.join(user_folder, filename)

def do_user_exists(filename):
    return os.path.isfile(filename)

def login(filename, password):
        with open(filename) as file:
            content = file.read()
            
            if content == password:
                return True
def register():

user_folder = 'C:\\Users\\spart\\Desktop\\IT_step_school\\Python\\07.08\\hodina\\users'




volba = input('Pro prihlaseni zadejte 1 \n Pro registaci zadejte 2 \n:')

if volba == '1':
    print('Chcete se prihlasit')

    
    username, password = get_user_data()

    filename = get_user_filename(username)

    user_exists = do_user_exists(filename)
    succes = False
    

    if succes:
        print('Uspesne prihlaseni')
    else:
        print('Prihlaseni se nepodarilo')


elif volba == '2':
    print('Chcete se registrovat')

    username, password = get_user_data()
    filename = get_user_filename(username)


    user_exists = do_user_exists(filename)
    
    if user_exists:
        print('zvolte prosim jiny username')
    else:
        with open(filename, mode='w') as file:
            file.write(password)
            print('registrace uspesna')







else:
    print('Neplatna volba')