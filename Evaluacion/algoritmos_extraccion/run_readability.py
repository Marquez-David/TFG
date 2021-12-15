import json
from pathlib import Path

import psutil
import time

import html_text
from readability import Document

def readability_json(output_text, tiempo_init):
    '''almacena el texto y las estadisticas obtenidas de readability en un fichero json'''
    output = {}

    with open('./archivos_salida/readability.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)

    output['readability'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(3.5)}
    with open('./archivos_estadisticas/readability_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_readability():
    '''extraccion de texto empleando readability'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        output[path.stem] = {'texto': html_text.extract_text(Document(html_to_string).summary(html_partial=True))}
        
    return output

#Probador
tiempo_init = time.time()
output_text = run_readability()
readability_json(output_text, tiempo_init)

