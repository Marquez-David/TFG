from rpy2.robjects import r

def run_rcrawler():
    '''ejecucion de rcrawler, codigo fuente en ./run_rcrawler.R'''
    r('source("./algoritmos_extraccion/run_rcrawler.R")')