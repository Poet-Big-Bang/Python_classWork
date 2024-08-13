import requests




def download_page(url, filename):
    response = requests.get(url)

    if response.status_code == 200:


        with open(f"C:\\Users\\spart\\Desktop\\IT_step_school\\Python\\10.08\\{filename}.html", mode="w", encoding="utf-8") as file:
            file.write(response.text)

    else:
        print('stranka vratila stav', response.status_code)

download_page('https://app.dayswaps.com', 'dayswaps')
