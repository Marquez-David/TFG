def calcular__perfect_accuracy(texto_base, texto_extraido):
    '''mide la proporcion de predicciones perfectas de texto extraido'''
    return float(tokenizar(texto_base) == tokenizar(texto_extraido))