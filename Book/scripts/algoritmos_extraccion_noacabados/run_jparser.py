import json
from pathlib import Path
from jparser import PageModel

def guardar_jparser_json(output_text):
    '''almacena el texto obtenido de jparser en un fichero json'''
    with open('./archivos_salida/jparser.json', 'w', encoding='utf8') as file:
        json.dump(output_text, file, sort_keys=True, ensure_ascii=False, indent=4)


def run_jparser():
    '''extraccion de texto empleando jparser'''
    output = {}
    url = {item_id: item['url'] for item_id, item in json.loads(Path('prueba.json').read_text('utf8')).items()}
    print(url)

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r') as file:
            html_to_string = file.read()
            #html_to_string = urllib2.urlopen(url[path.stem]).read().decode('gb18030')
        
        pm = PageModel(html_to_string)
        #article = Goose().extract(raw_html=html_to_string)
        #output[path.stem] = {'text': article.cleaned_text}

    #guardar_jparser_json(output)

run_jparser()
'''
def prueba(htmlstring):
    try:
        pm = PageModel(htmlstring)
    except (TypeError, ValueError):
        return ''
    result = pm.extract()
    # old
    mylist = list()
    for x in result['content']:
        if x['type'] in ('text', 'html'):
            mylist.append(str(x['data']))

    returnstring = ' '.join(mylist)
    returnstring = re.sub(r'\s+(p{P}+)', '\1', returnstring)
    return sanitize(returnstring)
'''