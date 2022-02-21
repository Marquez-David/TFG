def crear_ngramas(text, n):
    '''division del texto en ngramas donde cada ngrama contendra n tokens, 
    el resultado se devolvera como una tupla de ngramas'''
    tokens = tokenizar(text)
    ngramas = []
    for i in range(0, max(1, len(tokens) - n + 1)):
        #ngrama = tupla de 4 elementos, desde la posicion i hasta i + n
        ngrama = tuple(tokens[i: i + n]) 
        if ngrama: 
            ngramas.append(ngrama)
    return ngramas