from html2text import HTML2Text

def run_html2_text():
    '''extraccion de texto empleando html2_text'''
    output = {} #diccionario salida

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        HTML2Text().ignore_links, HTML2Text().ignore_images = True
        output[path.stem] = {'texto': HTML2Text().handle(html_to_string)}

    return output