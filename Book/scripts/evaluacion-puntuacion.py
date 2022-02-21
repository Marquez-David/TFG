def calculo_puntuacion(texto_base, texto_extraido, num_ngramas = 4):
    ''' recorre los ngramas de texto base y texto extraido, y devuelve una 
    tupla de metricas obtenidas, [tp, fp, fn]/tp+fp+fn '''
    ngramas_texto_base = get_diccionario_ngramas(texto_base, num_ngramas)
    ngramas_texto_extraido = get_diccionario_ngramas(texto_extraido, num_ngramas)

    tp = 0 #true positives
    fp = 0 #false positives
    fn = 0 #false negatives
    for key in (set(ngramas_texto_base) | set(ngramas_texto_extraido)):
        contador_base = ngramas_texto_base.get(key, 0)
        contador_extraido = ngramas_texto_extraido.get(key, 0)
        
        tp += calcular_tp(contador_base, contador_extraido)
        fp += calcular_fp(contador_base, contador_extraido)
        fn += calcular_fn (contador_base, contador_extraido)

    tp_fp_fn = [tp, fp, fn]
    sumatorio = sum(tp_fp_fn)

    if sumatorio > 0:

        tp_fp_fn = [metrica / sumatorio for metrica in tp_fp_fn]

    return tuple(tp_fp_fn)