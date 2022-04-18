from rpy2.robjects import r

def run_rvest():
    '''ejecucion de rvest, codigo fuente en ./run_rvest.R'''
    r('source("./algoritmos_extraccion/run_rvest.R")')