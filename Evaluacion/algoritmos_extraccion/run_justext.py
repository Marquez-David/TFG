import json
from pathlib import Path

import psutil
import time

import justext

def justText_json(output_text, tiempo_init):
    '''almacena el texto y las estadisticas obtenidas de justext en un fichero json'''
    output = {}

    with open('./archivos_salida/justext.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)

    output['justext'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(3)}
    with open('./archivos_estadisticas/justext_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)

def run_jusText():
    '''extraccion de texto empleando justext'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        paragraphs = justext.justext(html_to_string, justext.get_stoplist("English"), 50, 200, 0.1, 0.2, 0.2, 200, True)
        valid = [paragraph.text for paragraph in paragraphs if not paragraph.is_boilerplate]

        output[path.stem] = {'texto': ' '.join(valid)}

    return output

#Probador
tiempo_init = time.time()
output_test = run_jusText()
justText_json(output_test, tiempo_init)
