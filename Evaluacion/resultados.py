from turtle import color
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

'''
plt.ylim(0, 1)
 
## Declaramos valores para el eje x
#eje_x = ['rvest', 'Rcrawler', 'xPath']
 
## Declaramos valores para el eje y
#eje_y = [0.1347, 0.4540, 0.2421]
 
## Creamos Gráfica
plt.bar('rvest', 0.8974, color='dimgrey')
plt.bar('Rcrawler', 0.9310, color='dimgrey')
plt.bar('xPath', 0.9915, color='dimgrey')
#plt.bar('f1', 0.3866, color='dimgrey')
 
## Legenda en el eje y
#plt.ylabel('Métricas independientes dle entorno')
 
## Legenda en el eje x
#plt.xlabel('Resultados de inscriptis')
 
## Título de Gráfica
#plt.title('Resultados de la variable recall')
 
## Mostramos Gráfica
plt.show()
'''
'''
# Los datos de entrada 
a = [0.1347, 0.1371, 0.8974, 0.2378]
b = [0.4540, 0.4628, 0.9310, 0.6181]
c = [0.7830, 0.8486, 0.8696, 0.8590]

labels = ['accuracy', 'precision', 'recall', 'f1']
 
 # Establecer la posición y el ancho del gráfico de barras
pos = list(range(len(a)))
width = 0.3
 
# Dibujar
fig, ax = plt.subplots(figsize=(8,6))
 
plt.bar(pos, a, width,
                 alpha=0.5,
                 color='r',
                 label=labels[0])
 
plt.bar([p + width for p in pos], b, width,
                 alpha=0.5,
                 color='g',
                 label=labels[1])

plt.bar([p + width*2 for p in pos], c, width,
                 alpha=0.5,
                 color='b',
                 label=labels[2])

plt.bar([p + width*3 for p in pos], d, width,
                 alpha=0.5,
                 color='y',
                 label=labels[3])
    
plt.bar([p + width*4 for p in pos], e, width,
                 alpha=0.5,
                 color='grey',
                 label=labels[3])

plt.bar([p + width*5 for p in pos], f, width,
                 alpha=0.5,
                 color='purple',
                 label=labels[3])

# Establecer etiqueta y distancia
#ax.set_ylabel('y-value')
#ax.set_title('Grouped bar plot')
ax.set_xticks([p + 1 * width for p in pos])
ax.set_xticklabels(labels)
 
 # Establecer límites de los ejes x, y
plt.xlim(min(pos)-width, max(pos)+width*3)
plt.ylim([0, 1])
 
 # Dibujar
plt.legend(['rvest', 'Rcrawler', 'boilerpipeR'], loc='best')
plt.show()
'''

'''
# Los datos de entrada 
green_data = [43.9, 1.9]
blue_data = [47.9, 2.6]
#red_data = [46.3, 0.5]
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

#plt.barh([p + width*2 for p in pos], red_data, width,
                 #alpha=0.5,
                 #color='r',
                 #label=labels[1])


 # Establecer etiqueta y distancia
#ax.set_ylabel('y-value')
#ax.set_title('Grouped bar plot')
ax.set_yticks([p + 1.5 * width for p in pos])
ax.set_yticklabels(labels)
 
 # Establecer límites de los ejes x, y
plt.ylim(min(pos)-width, max(pos)+width*3)
plt.xlim([0, 100])
 
 # Dibujar
plt.legend(['Boilerpy', 'BoilerpipeR'], loc='upper right')
plt.show()
'''
'''
#relacion entre precision y recall, es decir, exclusion de contenido boilerplate y captacion de contenido principal
plt.ylim(0.8, 1)
plt.xlim(0, 1)


plt.plot(0.1371, 0.8974, "o", color = "orange")
plt.plot(0.4628, 0.9310, "o", color = "green")
plt.plot(0.2401, 0.9915, "o", color = "blue")
plt.xlabel("Precision")
plt.ylabel("Recall")
plt.legend(['rvest', 'Rcrawler', 'xPath'], loc='upper right')
plt.show()
'''

df = pd.DataFrame({
'group': ['rvest','Rcrawler','xPath'],
'accuracy': [0.1347, 0.4540, 0.2421],
'precision': [0.1371, 0.4628, 0.2401],
'recall': [0.8974, 0.9310, 0.9915],
'f1': [0.2378, 0.6181, 0.3866]
})
 
# number of variable
categories=list(df)[1:]
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([0.20,0.40,0.60,0.80], ["0.20","0.40","0.60","0.80"], color="grey", size=7)
plt.ylim(0,1)
 
# Ind1
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, 'o-', color='red', linewidth=1, label='rvest')
ax.fill(angles, values, 'red', alpha=0.1)

# Ind2
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, 'o-', color='green', linewidth=1, label='Rcrawler')
ax.fill(angles, values, 'green', alpha=0.2)

# Ind3
values=df.loc[2].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, 'o-', color='blue', linewidth=1, label='xPath')
ax.fill(angles, values, 'blue', alpha=0.1)

ax.legend(loc='best', bbox_to_anchor=(0.9, 0.2))

# Show the graph
plt.show()
