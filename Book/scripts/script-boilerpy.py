def run_boilerpy():
    '''extraccion de texto empleando boilerpipe'''
    output = {}

    for path in Path('archivos_html').glob('*.html'):
        with open(path, 'r', encoding = "utf-8") as file:
            html_to_string = file.read()

        extractor = extractors.ArticleExtractor()
        output[path.stem] = {'texto': extractor.get_content(html_to_string)}

    return output