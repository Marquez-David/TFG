def calcular_precision(tp, fp, fn):
    '''mide la eficacia de como los algoritmos excluyen contenido boilerplate'''
    if fp == 0 and fn == 0:
        return 1
    if tp == 0 and fp == 0:
        return 0
    return tp / (tp + fp)