import urllib.request
from inscriptis import get_annotated_text, ParserConfig

html = urllib.request.urlopen(url).read().decode('utf-8')

rules = {'h1': ['heading', 'h1'],
         'h2': ['heading', 'h2'],
         'b': ['emphasis'],
         'table': ['table']}

output = get_annotated_text(html, ParserConfig(annotation_rules=rules)