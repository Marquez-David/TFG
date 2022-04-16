import html_text
from readability import Document

def run_readability():
    '''extraccion de texto empleando readability'''
    output = {} #diccionario salida

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        doc = Document(html_to_string).summary(html_partial=True)
        output[path.stem] = {'texto': html_text.extract_text(doc)}
        
    return output