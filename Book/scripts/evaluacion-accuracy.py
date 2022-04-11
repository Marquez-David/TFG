def calcular_accuracy(tp, fp, fn):
    '''mide la proporcion de predicciones correctas de texto extraido'''
    if tp == 0:
        return 0
    if tp == 0 and fp == 0 and fn == 0:
        return 1
    return tp / (tp + fp + fn)