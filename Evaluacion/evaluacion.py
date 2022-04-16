from collections import Counter
import json
from pathlib import Path
import re
import statistics
from prettytable import PrettyTable
import time
import psutil


from bs4 import BeautifulSoup
from boilerpy3 import extractors
from goose3 import Goose
import html_text
from html2text import HTML2Text
from inscriptis import get_text
import justext
from readability import Document
import trafilatura
import lxml.html

def mostrar_tabla_metricas():
    '''se muestra pro pantalla la tabla de metricas de cada algoritmo'''
    tabla_metricas = PrettyTable(['N. del paquete', 'Accuracy', 'Precision', 'Recall', 'F1', 'RAM Usage(%)', 'CPU Usage(%)', 'Execution Time'])

    '''
    #ejecucion de todos los algoritmos de extraccion programados en python
    for path in Path('algoritmos_extraccion').glob('*.py'):
        print("Ejecutando: ", path.stem)
        exec(open(path).read())
    '''
    
    documento_base = cargar_json(Path('documento_base.json'))
    for path in Path('archivos_salida').glob('*.json'):
        documento_extraido = cargar_json(path)
        estadisticas = cargar_json('./archivos_estadisticas/' + str(path.stem) + '_stats.json')
        metricas = evaluar_algoritmo(documento_base, documento_extraido)
        tabla_metricas.add_row([path.stem, metricas['accuracy'], metricas['precision'], metricas['recall'], metricas['f1'],
                                estadisticas[path.stem].get('RAM % Usage'), estadisticas[path.stem].get('CPU % Usage'), estadisticas[path.stem].get('Execution time')])
                               
    print(tabla_metricas[14])
    
def evaluar_algoritmo(documento_base, documento_extraido):
    '''evaluacion de cada algoritmo a partir de su documento de extraccion'''
    #las claves entre json no coinciden, falta algun json, o la clave correspondiente al texto no coincide
    if documento_base.keys() != documento_extraido.keys():
        raise ValueError('No hay coincidencia entre claves')
        
    tp_fp_fns = []
    #accuracies = []
    for key in documento_base.keys():
        texto_base = get_texto(documento_base, key)
        texto_extraido = get_texto(documento_extraido, key)

        tp_fp_fns.append(comparacion_ngramas(texto_base, texto_extraido))
        #accuracies.append(calcular_accuracy(texto_base, texto_extraido))

    metricas = calcular_puntuacion_metricas(tp_fp_fns)
    metricas['tp_fp_fns'] = tp_fp_fns
    #metricas['accuracy'] = statistics.mean(accuracies)

    return metricas

def calcular_puntuacion_metricas(tp_fp_fns):
    '''calcula la media de las puntuaciones obtenidas a partir de la metricas dadas'''
    precision = statistics.mean([calcular_precision(tp, fp, fn) for tp, fp, fn in tp_fp_fns if tp + fp > 0])
    recall = statistics.mean([calcular_recall(tp, fp, fn) for tp, fp, fn in tp_fp_fns if tp + fn > 0])
    accuracy = statistics.mean([calcular_accuracy(tp, fp, fn) for tp, fp, fn in tp_fp_fns if tp + fn > 0])
    f1 = 2 * precision * recall / (precision + recall)
    return {'f1': round(f1, 4), 'precision': round(precision, 4), 'recall': round(recall, 4), 'accuracy': round(accuracy, 4)}

def calcular_precision(tp, fp, fn):
    '''mide la eficacia de como los algoritmos excluyen las partes no deseadas del documento html'''
    if fp == 0 and fn == 0:
        return 1
    if tp == 0 and fp == 0:
        return 0
    return tp / (tp + fp)

def calcular_recall(tp, fp, fn):
    '''mide la eficacia de como el algoritmo capta las partes deseadas del documento html'''
    if fp == 0 and fn == 0:
        return 1
    if tp == 0 and fn == 0:
        return 0
    return tp / (tp + fn)

def calcular_accuracy(tp, fp, fn):
    '''mide la proporción de predicciones perfectas de texto extraido con respecto al texto base'''
    if tp == 0:
        return 0
    if tp == 0 and fp == 0 and fn == 0:
        return 1
    return tp / (tp + fp + fn)

def comparacion_ngramas(texto_base, texto_extraido, num_ngramas = 4):
    ''' recorre los ngramas de texto base y texto extraido, y devuelve una tupla de metricas obtenidas, [tp, fp, fn]/tp+fp+fn '''
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
        #division de cada metrica por el numero de metricas totales, [tp: 167.0, fp: 1277.0, fn: 12.0] / 1456.0 = [0.114, 0.877, 0.008]
        tp_fp_fn = [metrica / sumatorio for metrica in tp_fp_fn]

    return tuple(tp_fp_fn)

def calcular_tp(contador_base, contador_extraido):
    '''retorna el numero de ngramas que coinciden en el texto base y en el texto extraido'''
    return min(contador_base, contador_extraido)

def calcular_fp(contador_base, contador_extraido):
    '''retorna el numero de ngramas que aparecen en el texto extraido pero no en el texto base'''
    return max(0, contador_extraido - contador_base)

def calcular_fn(contador_base, contador_extraido):
    '''retorna el numero de ngramas que aparecen en el texto base pero no en el texto extraido'''
    return max(0, contador_base - contador_extraido)

def get_diccionario_ngramas(text, ngram_n):
    '''devuelve un diccionario de ngramas a partir de text'''
    return dict(Counter(crear_ngramas(text, ngram_n)))

def tokenizar(text):
    '''se separa el texto en tokens/palabras y lo devuelve como una lista'''
    #Compila un patrón de expresión regular en un objeto de expresión regular, que puede ser usado para hacer coincidencias
    token_expresion_regular = re.compile(r'\w+', re.UNICODE | re.MULTILINE | re.IGNORECASE | re.DOTALL)
    return token_expresion_regular.findall(text or '')

def crear_ngramas(text, n):
    '''division del texto en ngramas donde cada ngrama contendrá n tokens, el resultado se devolvera como una tupla de ngramas'''
    tokens = tokenizar(text)
    ngramas = []
    for i in range(0, max(1, len(tokens) - n + 1)):
        ngrama = tuple(tokens[i: i + n]) #ngrama = tupla de 4 elementos, desde la posicion i hasta i + n
        if ngrama: 
            ngramas.append(ngrama) #si el ngrama existe se añade a la lista de ngramas
    return ngramas

def cargar_json(path: Path):
    '''carga un determinado json dado por parametro'''
    with open(path, 'rt', encoding='utf8') as file:
        return json.load(file)

def get_texto(documento, key):
    '''se selecciona el texto de un documento determinado dada su clave'''
    return documento[key].get('texto', '')

#Probador
mostrar_tabla_metricas()


