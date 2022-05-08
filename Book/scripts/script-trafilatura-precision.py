import trafilatura

def run_trafilatura_precision():
    '''extraccion de texto empleando trafilatura tipo precision'''
    output = {} #diccionario salida

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()
            
        output[path.stem] = {'texto': trafilatura.extract(html_to_string, 
            no_fallback = False, 
            favor_precision = True)}

    return output