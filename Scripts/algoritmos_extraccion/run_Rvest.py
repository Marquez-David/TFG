import json

import psutil
import time

from rpy2.robjects import r

def rvest_json(tiempo_init):
    '''almacena las estadisticas obtenidas de rvest en un fichero json'''
    output = {}

    output['rvest'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(52.6)}
    with open('./archivos_estadisticas/rvest_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)

def run_rvest():
    '''ejecucion de rvest, codigo fuente disponible en ./algoritmos_extraccion/run_rvest.R'''
    r('source("./algoritmos_extraccion/run_rvest.R")')

#Probador
tiempo_init = time.time()
output_text = run_rvest()
rvest_json(tiempo_init)