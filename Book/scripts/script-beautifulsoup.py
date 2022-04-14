from bs4 import BeautifulSoup

def run_beautifulsoup():
    '''extraccion de texto empleando beautifulsoup'''
    output = {} #diccionario salida

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        bs = BeautifulSoup(html_to_string, 'html.parser')
        output[path.stem] = {'texto': bs.get_text(separator=' ', strip=True)}

    return output