import json
from pathlib import Path

import psutil
import time

from boilerpy3 import extractors

def boilerpy_json(output_text, tiempo_init):
    '''almacena el texto y las estadisticas obtenidas de boilerpy en un fichero json'''
    output= {}

    with open('./archivos_salida/boilerpy.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)

    output['boilerpy'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(2.5)}
    with open('./archivos_estadisticas/boilerpy_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_boilerpy():
    '''extraccion de texto empleando boilerpipe'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        output[path.stem] = {'texto': extractors.ArticleExtractor().get_content(html_to_string)}

    return output

#Probador
tiempo_init = time.time()
output_text = run_boilerpy()
boilerpy_json(output_text, tiempo_init)
