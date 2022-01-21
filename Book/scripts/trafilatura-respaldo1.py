def try_readability(htmlinput, url):
    '''Safety net: try with the generic algorithm readability'''
    try:
        doc = LXMLDocument(htmlinput, url, min_text_length=25, retry_length=250)
        return html.fromstring(doc.summary(html_partial=True), parser=HTML_PARSER)
    except (etree.SerialisationError, Unparseable):
        return etree.Element('div')