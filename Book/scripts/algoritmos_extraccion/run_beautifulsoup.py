import json
from pathlib import Path

from bs4 import BeautifulSoup

def beautifulsoup_json(output_text):
    '''almacena el texto obtenido de beautifulsoup en un fichero json'''
    with open('./archivos_salida/beautifulsoup.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_beautifulsoup():
    '''extraccion de texto empleando beautifulsoup'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        bs = BeautifulSoup(html_to_string, 'html.parser')
        output[path.stem] = {'texto': bs.get_text(separator=' ', strip=True)}

    return output

#Probador
output_text = run_beautifulsoup()
beautifulsoup_json(output_text)
