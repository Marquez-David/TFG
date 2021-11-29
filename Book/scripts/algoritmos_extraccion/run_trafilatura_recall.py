import json
from pathlib import Path

import trafilatura

def trafilatura_recall_json(output_text):
    '''almacena el texto obtenido de trafilatura en un fichero json'''
    with open('./archivos_salida/trafilatura_recall.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_trafilatura_recall():
    '''extraccion de texto empleando trafilatura'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()
            
        output[path.stem] = {'texto': trafilatura.extract(html_to_string, no_fallback=False, favor_recall=True, include_comments=False, include_tables=True, include_formatting=False)}

    return output

#Probador
output_text = run_trafilatura_recall()
trafilatura_recall_json(output_text)