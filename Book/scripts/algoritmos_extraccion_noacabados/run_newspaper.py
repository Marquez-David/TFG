#!/usr/bin/env python3
import gzip
import json
from pathlib import Path

from newspaper import Article

def guardar_newspaper_json(output_text):
    '''almacena el texto obtenido de newspaper en un fichero json'''
    with open('./archivos_salida/newspaper.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_newspaper():
    '''extraccion de texto empleando newspaper'''
    output = {}
    
    url_by_item_id = {item_id: item['url'] for item_id, item in json.loads(Path('documento_base.json').read_text('utf8')).items()}

    '''
    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r') as file:
            html_to_string = file.read()

        article = Article(url_by_item_id[path.stem])
        article.set_html(html_to_string)
        article.parse()
        output[path.stem] = {'texto': article.text}

    guardar_newspaper_json(output)
    '''
    print(url_by_item_id)

run_newspaper()
