import json
from pathlib import Path

import psutil
import time

from html2text import HTML2Text

def html2text_json(output_text, tiempo_init):
    '''almacena el texto y las estadisticas obtenidas de html2text en un fichero json'''
    output = {}

    with open('./archivos_salida/html2text.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)

    output['html2txt'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(4.4)}
    with open('./archivos_estadisticas/html2text_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_html2_text():
    '''extraccion de texto empleando html2_text'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        h = HTML2Text()
        h.ignore_links = True
        h.ignore_images = True

        output[path.stem] = {'texto': h.handle(html_to_string)}

    return output

#Probador
tiempo_init = time.time()
output_text = run_html2_text()
html2text_json(output_text, tiempo_init)
