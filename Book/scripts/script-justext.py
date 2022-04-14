import justext

def run_jusText():
    '''extraccion de texto empleando justext'''
    output = {} #diccionario salida

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        pargphs = justext.justext(html_to_string, justext.get_stoplist("English"))
        valid = [pargph.text for pargph in pargphs if not pargph.is_boilerplate]
        output[path.stem] = {'texto': ' '.join(valid)}

    return output