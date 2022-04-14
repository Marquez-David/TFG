def calcular_specificity(tp, fp, fn, tn):
    '''mide la cantidad de predicciones negativas que en realidad son correctas'''
    if fp == 0 and fn == 0:
        return 1
    if tn == 0 and fp == 0:
        return 0
    return tp / (tn + fp)