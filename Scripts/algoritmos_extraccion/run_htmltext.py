import json
from pathlib import Path

import psutil
import time

import html_text

def htmltext_json(output_text, tiempo_init):
    '''almacena el texto y las estadisticas obtenidas de htmltext en un fichero json'''
    output = {}

    with open('./archivos_salida/htmltext.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)

    output['html_text'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(1.2)}
    with open('./archivos_estadisticas/htmltext_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_html_text():
    '''extraccion de texto empleando html_text'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()
    
        output[path.stem] = {'texto': html_text.extract_text(html_to_string)}
        
    return output
   
#Probador
tiempo_init = time.time()
output_text = run_html_text()
htmltext_json(output_text, tiempo_init)

