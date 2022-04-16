from turtle import color
import matplotlib.pyplot as plt

'''
plt.ylim(0, 1)
 
## Declaramos valores para el eje x
eje_x = ['Accuracy', 'Precision', 'Recall', 'F1']
 
## Declaramos valores para el eje y
eje_y = [0.9188, 0.9287, 0.9776, 0.9525]
 
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
'''
# Los datos de entrada 
green_data = [0.9124, 0.9196, 0.9707, 0.9444]
blue_data = [0.9129, 0.9208, 0.9699, 0.9447]
red_data = [0.9188, 0.9287, 0.9776, 0.9525]
labels = ['Accuracy', 'Precision', 'Recall', 'F1']
 
 # Establecer la posición y el ancho del gráfico de barras
pos = list(range(len(green_data)))
width = 0.2
 
 # Dibujar
fig, ax = plt.subplots(figsize=(8,6))
 
plt.bar(pos, green_data, width,
                 alpha=0.5,
                 color='g',
                 label=labels[0])
 
plt.bar([p + width for p in pos], blue_data, width,
                 alpha=0.5,
                 color='b',
                 label=labels[1])

plt.bar([p + width*2 for p in pos], red_data, width,
                 alpha=0.5,
                 color='r',
                 label=labels[2])


 # Establecer etiqueta y distancia
#ax.set_ylabel('y-value')
#ax.set_title('Grouped bar plot')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(labels)
 
 # Establecer límites de los ejes x, y
plt.xlim(min(pos)-width, max(pos)+width*3)
plt.ylim([0, 1])
 
 # Dibujar
plt.legend(['Trafilatura', 'Trafilatura precision', 'Trafilatura recall'], loc='upper right')
plt.show()
'''

# Los datos de entrada 
green_data = [45.7, 1.4]
blue_data = [45.9, 1.4]
red_data = [46.3, 0.5]
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
plt.legend(['Trafilatura', 'Trafilatura precision', 'Trafilatura recall'], loc='upper right')
plt.show()



