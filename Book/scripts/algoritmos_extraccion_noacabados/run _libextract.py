import json
from pathlib import Path

from libextract.api import extract

def guardar_libextract_json(output_text):
    '''almacena el texto obtenido de libextract en un fichero json'''
    with open('./archivos_salida/libextract.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_libextract():
    '''extraccion de texto empleando libextract'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r') as file:
            html_to_string = file.read()

        textnodes = list(extract(html_to_string))
        
        output[path.stem] = {'texto': textnodes[0].text_content()}

    guardar_libextract_json(output)

run_libextract()