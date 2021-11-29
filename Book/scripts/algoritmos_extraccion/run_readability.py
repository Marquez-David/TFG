import json
from pathlib import Path

import html_text
from readability import Document

def readability_json(output_text):
    '''almacena el texto obtenido de readability en un fichero json'''
    with open('./archivos_salida/readability.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_readability():
    '''extraccion de texto empleando readability'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        output[path.stem] = {'texto': html_text.extract_text(Document(html_to_string).summary(html_partial=True))}
        
    return output

#Probador
output_text = run_readability()
readability_json(output_text)

