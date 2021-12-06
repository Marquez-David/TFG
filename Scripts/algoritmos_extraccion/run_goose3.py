import json
from pathlib import Path

import psutil
import time

from goose3 import Goose

def goose3_json(output_text, tiempo_init):
    '''almacena el texto obtenido de goose3 en un fichero json'''
    output = {}

    with open('./archivos_salida/goose3.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)

    output['goose3'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(11.8)}
    with open('./archivos_estadisticas/goose3_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_goose3():
    '''extraccion de texto empleando goose3'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        article = Goose().extract(raw_html=html_to_string)
        output[path.stem] = {'texto': article.cleaned_text}

    return output

#Probador
tiempo_init = time.time()
output_text = run_goose3()
goose3_json(output_text, tiempo_init)

