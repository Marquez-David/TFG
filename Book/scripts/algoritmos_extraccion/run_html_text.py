import json
from pathlib import Path

import html_text

def htmltext_json(output_text):
    '''almacena el texto obtenido de htmltext en un fichero json'''
    with open('./archivos_salida/html_text.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_html_text():
    '''extraccion de texto empleando html_text'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()
    
        output[path.stem] = {'texto': html_text.extract_text(html_to_string)}
        
    return output
   
#Probador
output_text = run_html_text()
htmltext_json(output_text)

