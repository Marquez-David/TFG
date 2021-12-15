import json

import psutil
import time

from rpy2.robjects import r

def rcrawler_json(tiempo_init):
    '''almacena las estadisticas obtenidas de rcrawler en un fichero json'''
    output = {}

    output['rcrawler'] = {'RAM % Usage': psutil.virtual_memory()[2], 'Execution time': time.time() - tiempo_init, 'CPU % Usage': psutil.cpu_percent(189.9)}
    with open('./archivos_estadisticas/rcrawler_stats.json', 'w', encoding='utf8') as file:
        json.dump(output, file, sort_keys=True, ensure_ascii=False, indent=4)

def run_rcrawler():
    '''ejecucion de rcrawler, codigo fuente disponible en ./algoritmos_extraccion/run_rcrawler.R'''
    r('source("./algoritmos_extraccion/run_rcrawler.R")')

#Probador
tiempo_init = time.time()
output_text = run_rcrawler()
rcrawler_json(tiempo_init)