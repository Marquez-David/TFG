import json
from pathlib import Path

from goose3 import Goose

def goose3_json(output_text):
    '''almacena el texto obtenido de goose3 en un fichero json'''
    with open('./archivos_salida/goose3.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_goose3():
    '''extraccion de texto empleando goose3'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        article = Goose().extract(raw_html=html_to_string)
        output[path.stem] = {'texto': article.cleaned_text}

    return output

#Probador
output_text = run_goose3()
goose3_json(output_text)

