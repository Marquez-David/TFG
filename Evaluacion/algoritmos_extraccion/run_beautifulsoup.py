import json
from pathlib import Path

import psutil
import time

from bs4 import BeautifulSoup

def beautifulsoup_json(output_text, tiempo_init):
    '''almacena el texto y las estadisticas obtenidas de beautifulsoup en un fichero json'''
    output = {}

    with open('./archivos_salida/beautifulsoup.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)

    output['beautifulsoup'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(4)}
    with open('./archivos_estadisticas/beautifulsoup_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)

def run_beautifulsoup():
    '''extraccion de texto empleando beautifulsoup'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        bs = BeautifulSoup(html_to_string, 'lxml')
        output[path.stem] = {'texto': bs.get_text(separator=' ', strip=True)}

    return output

#Probador
tiempo_init = time.time()
output_text = run_beautifulsoup()
beautifulsoup_json(output_text, tiempo_init)
