def tokenizar(text):
    '''se separa el texto en tokens/palabras y lo devuelve como una lista'''
    token = re.compile(r'\w+', re.UNICODE| re.MULTILINE| re.IGNORECASE| re.DOTALL)
    return token.findall(text or '')