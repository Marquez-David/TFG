import os
from pathlib import Path

cont = 0
for path in Path('archivos_html').glob('*test.html'):
    if(cont<10):
        nuevo = "archivos_html/000" + str(cont) + "test.html"
    elif(cont<100):
        nuevo = "archivos_html/00" + str(cont) + "test.html"
    elif(cont<1000):
        nuevo = "archivos_html/0" + str(cont) + "test.html"
    cont = cont + 1
    os.rename(path, nuevo)


