from urllib.request import urlretrieve
import requests

def download_image2(url, filename = None):
    names = url.split('/')
    filename = filename or names[-1]
    
    response = requests.get(url)
    with open('test.png', mode = 'wb') as file:
        file.write(response.content)


def download_image(url, filename = None):
    urlretrieve(url, filename = 'muj=obrazek.png')
    print('tvuj obrazek byl ulozen')

url = 'https://www.python.org/static/img/python-logo@2x.png'

download_image2(url)