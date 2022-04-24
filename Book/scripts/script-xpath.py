import lxml.html

def run_xpath_text():
    '''extraccion de texto empleando xpath_text'''
    output = {} #diccionario salida

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as input_file:
            html_to_string = input_file.read()
        
        root = lxml.html.fromstring(html_to_string)
        bodies = root.xpath('//body')
        if bodies: root = bodies[0]

        output[path.stem] = {'texto': ' '.join(root.xpath('.//text()'))
                            .replace('\r','').replace('\n','')
                            .replace('\r','').replace('\t','')}

    return output