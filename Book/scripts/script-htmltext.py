import html_text

def run_html_text():
    '''extraccion de texto empleando html_text'''
    output = {} #diccionario salida

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()
    
        output[path.stem] = {'texto': html_text.extract_text(html_to_string)}
        
    return output