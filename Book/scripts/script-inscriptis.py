from inscriptis import get_text

def run_inscriptis():
    '''extraccion de texto empleando inscriptis'''
    output = {} #diccionario salida

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        output[path.stem] = {'texto': get_text(html_to_string)}

    return output