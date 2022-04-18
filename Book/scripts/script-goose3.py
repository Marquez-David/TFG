from goose3 import Goose

def run_goose3():
    '''extraccion de texto empleando goose3'''
    output = {} #diccionario salida

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        g = Goose()
        article = g.extract(raw_html = html_to_string)
        
        output[path.stem] = {'texto': article.cleaned_text}

    return output