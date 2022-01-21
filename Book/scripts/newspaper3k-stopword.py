def candidate_words(self, stripped_input):
    import nltk
    s = nltk.stem.isri.ISRIStemmer()
    words = []
    for word in nltk.tokenize.wordpunct_tokenize(stripped_input):
        words.append(s.stem(word))
    return words