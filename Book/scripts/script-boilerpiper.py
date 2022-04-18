from rpy2.robjects import r

def run_boilerpipeR():
    '''ejecucion de boilerpipeR, codigo fuente en ./run_boilerpipeR.R'''
    r('source("./algoritmos_extraccion/run_boilerpipeR.R")')