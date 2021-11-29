import json
from pathlib import Path

import trafilatura

def trafilatura_json(output_text):
    '''almacena el texto obtenido de trafilatura en un fichero json'''
    with open('./archivos_salida/trafilatura.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_trafilatura():
    '''extraccion de texto empleando trafilatura'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()
            
        output[path.stem] = {'texto': trafilatura.extract(html_to_string, include_comments=False)}

    return output

#Probador
output_text = run_trafilatura()
trafilatura_json(output_text)


