import trafilatura as tf

def run_trafilatura_recall():
    '''extraccion de texto empleando trafilatura tipo recall'''
    output = {} #diccionario salida

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()
            
        output[path.stem] = {'texto': tf.extract(html_to_string, 
            no_fallback = False, favor_recall = True)}

    return output