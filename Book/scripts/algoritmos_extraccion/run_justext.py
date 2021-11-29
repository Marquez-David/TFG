#!/usr/bin/env python3
import gzip
import json
from pathlib import Path

import justext

def justText_json(output_text):
    '''almacena el texto obtenido de justext en un fichero json'''
    with open('./archivos_salida/justext.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)


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
output_test = run_jusText()
justText_json(output_test)
