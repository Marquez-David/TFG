def justext_rescue(tree, url, target_language, postbody, len_text, text):
    '''Try to use justext algorithm as a second fallback'''
    result_bool = False
    temppost_algo = try_justext(tree, url, target_language)
    if temppost_algo is not None:
        temp_text = trim(' '.join(temppost_algo.itertext()))
        len_algo = len(temp_text)
        if len_algo > len_text:
            postbody, text, len_text = temppost_algo, temp_text, len_algo
            result_bool = True
    return postbody, text, len_text, result_bool