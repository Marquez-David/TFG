import json

import psutil
import time

from rpy2.robjects import r

def htm2txt_json(tiempo_init):
    '''almacena las estadisticas obtenidas de htm2txt en un fichero json'''
    output = {}

    output['htm2txt'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(92.7)}
    with open('./archivos_estadisticas/htm2txt_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)

def run_htm2txt():
    '''ejecucion de htm2txt, codigo fuente disponible en ./algoritmos_extraccion/run_htm2txt.R'''
    r('source("./algoritmos_extraccion/run_htm2txt.R")')


#Probador
tiempo_init = time.time()
output_text = run_htm2txt()
htm2txt_json(tiempo_init)