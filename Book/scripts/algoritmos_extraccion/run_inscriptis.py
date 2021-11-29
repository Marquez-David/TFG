import json
from pathlib import Path

from inscriptis import get_text

def inscriptis_json(output_text):
    '''almacena el texto obtenido de inscriptis en un fichero json'''
    with open('./archivos_salida/inscriptis.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)

def run_inscriptis():
    '''extraccion de texto empleando inscriptis'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        output[path.stem] = {'texto': get_text(html_to_string)}

    return output

#Probador
output_text = run_inscriptis()
inscriptis_json(output_text)
