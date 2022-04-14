from turtle import color
import matplotlib.pyplot as plt


plt.ylim(0, 1)
 
## Declaramos valores para el eje x
eje_x = ['Accuracy', 'Precision', 'Recall', 'F1']
 
## Declaramos valores para el eje y
eje_y = [0.5105, 0.5107, 0.9804, 0.6715]
 
## Creamos Gráfica
plt.bar(eje_x, eje_y, color='orange')
 
## Legenda en el eje y
#plt.ylabel('Métricas independientes dle entorno')
 
## Legenda en el eje x
#plt.xlabel('Resultados de inscriptis')
 
## Título de Gráfica
#plt.title('Resultados de Beautiful Soup')
 
## Mostramos Gráfica
plt.show()

 
'''
# Los datos de entrada 
green_data = [47.0, 4.3]
blue_data = [38.1, 3.4]
red_data = [39.1, 3.4]
labels = ['Uso RAM', 'Uso CPU']
 
 # Establecer la posición y el ancho del gráfico de barras
pos = list(range(len(green_data)))
width = 0.3
 
 # Dibujar
fig, ax = plt.subplots(figsize=(8,6))
 
plt.barh(pos, green_data, width,
                 alpha=0.5,
                 color='g',
                 label=labels[0])
 
plt.barh([p + width for p in pos], blue_data, width,
                 alpha=0.5,
                 color='b',
                 label=labels[1])

plt.barh([p + width*2 for p in pos], red_data, width,
                 alpha=0.5,
                 color='r',
                 label=labels[1])


 # Establecer etiqueta y distancia
#ax.set_ylabel('y-value')
#ax.set_title('Grouped bar plot')
ax.set_yticks([p + 1.5 * width for p in pos])
ax.set_yticklabels(labels)
 
 # Establecer límites de los ejes x, y
plt.ylim(min(pos)-width, max(pos)+width*3)
plt.xlim([0, 100])
 
 # Dibujar
plt.legend(['html.parse', 'lxml', 'html5lib'], loc='upper right')
plt.show()
'''

