def calcular_fn(contador_base, contador_extraido):
    '''Numero de ngramas que aparecen en el texto base pero no en el extraido'''
    return max(0, contador_base - contador_extraido)