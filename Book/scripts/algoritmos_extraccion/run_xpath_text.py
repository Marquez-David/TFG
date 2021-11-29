import json
from pathlib import Path

import lxml.html

def xpathText_json(output_text):
    '''almacena el texto obtenido de xpath-text en un fichero json'''
    with open('./archivos_salida/xpath_text.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)

def run_xpath_text():
    '''extraccion de texto empleando xpath_text'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as input_file:
            html_to_string = input_file.read()
        
        root = lxml.html.fromstring(html_to_string)
        bodies = root.xpath('//body')
        if bodies:
            root = bodies[0]

        output[path.stem] = {'texto': ' '.join(root.xpath('.//text()')).replace('\r','').replace('\n','').replace('\r','').replace('\t','')}

    return output

#Probador
output_text = run_xpath_text()
xpathText_json(output_text)

