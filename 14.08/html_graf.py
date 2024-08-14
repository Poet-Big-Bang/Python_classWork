def create_graf(data: list, filename: str):
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write('<style>div{height:10px;background:red;margin:10px;}</style>')

        for value in data:
            div = f'<div style="width:{value}px;"></div>'
            file.write(div)



create_graf([10,20,30,40,50], 'my-graf.html')