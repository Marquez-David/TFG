def calcular_tp(contador_base, contador_extraido):
    '''Numero de ngramas que coinciden en el texto base y en el extraido'''
    return min(contador_base, contador_extraido)