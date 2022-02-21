def calcular_fp(contador_base, contador_extraido):
    '''Numero de ngramas que aparecen en el texto extraido pero no en el base'''
    return max(0, contador_extraido - contador_base)