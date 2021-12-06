import json

import psutil
import time

from rpy2.robjects import r

def boilerpipeR_json(tiempo_init):
    '''almacena las estadisticas obtenidas de boilerpipeR en un fichero json'''
    output = {}

    output['boilerpipeR'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(70.1)}
    with open('./archivos_estadisticas/boilerpipeR_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)

def run_boilerpipeR():
    '''ejecucion de boilerpipeR, codigo fuente disponible en ./algoritmos_extraccion/run_boilerpipeR.R'''
    r('source("./algoritmos_extraccion/run_boilerpipeR.R")')

#Probador
tiempo_init = time.time()
output_text = run_boilerpipeR()
boilerpipeR_json(tiempo_init)