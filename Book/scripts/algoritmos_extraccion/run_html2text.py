import json
from pathlib import Path

from html2text import HTML2Text

def html2text_json(output_text):
    '''almacena el texto obtenido de html2text en un fichero json'''
    with open('./archivos_salida/html2text.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_html2_text():
    '''extraccion de texto empleando html2_text'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        h = HTML2Text()
        h.ignore_links = True
        h.ignore_images = True

        output[path.stem] = {'texto': h.handle(html_to_string)}

    return output

#Probador
output_text = run_html2_text()
html2text_json(output_text)
