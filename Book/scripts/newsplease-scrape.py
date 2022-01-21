 def from_html(html, url=None, download_date=None, fetch_images=True):
    '''Extracts relevant information from an HTML page given as a string.'''
    extractor = article_extractor.Extractor(
        (['newspaper_extractor']
            if fetch_images
            else [("newspaper_extractor_no_images", "NewspaperExtractorNoImages")]
        ) + ['readability_extractor', 'date_extractor', 'lang_detect_extractor'])

    item = NewscrawlerItem()
    item['spider_response'] = DotMap()
    item['spider_response'].body = html
    ...
    item['modified_date'] = None
    item = extractor.extract(item)

    tmp_article = ExtractedInformationStorage.extract_relevant_info(item)
    final_article = ExtractedInformationStorage.convert_to_class(tmp_article)
    return final_article