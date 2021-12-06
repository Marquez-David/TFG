import json
from pathlib import Path

import psutil
import time

import trafilatura

def trafilatura_precision_json(output_text, tiempo_init):
    '''almacena el texto y las estadisticas obtenidas de trafilatura tipo precision en un fichero json'''
    output = {}

    with open('./archivos_salida/trafilatura_precision.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)

    output['trafilatura_precision'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(4.6)}
    with open('./archivos_estadisticas/trafilatura_precision_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_trafilatura_precision():
    '''extraccion de texto empleando trafilatura tipo precision'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()
            
        output[path.stem] = {'texto': trafilatura.extract(html_to_string, no_fallback=False, favor_precision=True, include_comments=False, include_tables=True, include_formatting=False)}

    return output

#Probador
tiempo_init = time.time()
output_text = run_trafilatura_precision()
trafilatura_precision_json(output_text, tiempo_init)