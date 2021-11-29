import json
from pathlib import Path

from boilerpy3 import extractors

def boilerpy_json(output_text):
    '''almacena el texto obtenido de boilerpy en un fichero json'''
    with open('./archivos_salida/boilerpy.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)



def run_boilerpy():
    '''extraccion de texto empleando boilerpipe'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        output[path.stem] = {'texto': extractors.ArticleExtractor().get_content(html_to_string)}

    return output

#Probador
output_text = run_boilerpy()
boilerpy_json(output_text)
