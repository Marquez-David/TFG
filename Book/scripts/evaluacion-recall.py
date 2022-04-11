def calcular_recall(tp, fp, fn):
    '''mide la eficacia de como el algoritmo capta contenido principal'''
    if fp == 0 and fn == 0:
        return 1
    if tp == 0 and fn == 0:
        return 0
    return tp / (tp + fn)