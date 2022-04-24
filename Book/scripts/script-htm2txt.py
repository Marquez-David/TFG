from rpy2.robjects import r

def run_htm2txt():
    '''ejecucion de htm2txt, codigo fuente en ./run_htm2txt.R'''
    r('source("./algoritmos_extraccion/run_htm2txt.R")')