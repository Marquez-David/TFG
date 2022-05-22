from distutils.log import WARN
from turtle import color
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
'''
X = [43.9, 32.2, 44.6, 42.0] #ram
Y = [1.9, 6.1, 1.8, 1.2] #cpu

Z = [45.0, 44.9, 45.1, 45.3, 45.9] #ram
W = [0.2, 0.5, 0.5, 1.6, 1.4] #cpu

A = [44.1, 46.7, 47.9, 44.4] #ram
B = [8.9, 3.4, 2.6, 2.0] #cpu

annot1=["Boilerpy","Goose3","html2text","Beautiful Soup"]
annot2=["inscriptis","html_text","jusText", "Readability", "Trafilatura"]
annot3=["rvest","Rcrawler","boilerpipeR","xPath"]

plt.figure(figsize=(8,6))
plt.scatter(Y,X,s=100,color="black", alpha=.5)
plt.scatter(W,Z,s=100,color="black", alpha=.5)
plt.scatter(B,A,s=100,color="black", alpha=.5)

for i, label in enumerate(annot1):
    plt.annotate(label, (Y[i], X[i]))

for i, label in enumerate(annot2):
    plt.annotate(label, (W[i], Z[i]))

for i, label in enumerate(annot3):
    plt.annotate(label, (B[i], A[i]))   

plt.xlabel("Uso de RAM (%)")
plt.ylabel("Uso de CPU (%)")
plt.ylim(0, 100)
plt.xlim(0, 10)
plt.legend(loc="upper left")
plt.show()
'''

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
a = [0.5165, 0.5129, 0.9928, 0.6764]
b = [0.1347, 0.1371, 0.8974, 0.2378]

labels = ['accuracy', 'precision', 'recall', 'f1']
 
 # Establecer la posición y el ancho del gráfico de barras
pos = list(range(len(a)))
width = 0.3
 
# Dibujar
fig, ax = plt.subplots(figsize=(8,6))
 
plt.bar(pos, a, width,
                 alpha=0.5,
                 color='g',
                 label=labels[0])
 
plt.bar([p + width for p in pos], b, width,
                 alpha=0.5,
                 color='b',
                 label=labels[1])

plt.bar([p + width*2 for p in pos], c, width,
                 alpha=0.5,
                 color='r',
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
plt.xlim(min(pos)-width, max(pos)+width*2)
plt.ylim([0, 1])
 
 # Dibujar
plt.legend(['Beautiful Soup', 'rvest'], loc='best')
plt.show()
'''

# Los datos de entrada 
green_data = [4.4590, 3.5952, 25.9731, 2.5412, 2.9546, 39.9543, 2.1009, 1.1800, 3.1778, 4.4020, 158.0663, 0.7476, 60.3245]
labels = ['Trafilatura', 'Readability', 'Goose3', 'Boilerpy', 'jusText', 'boilerpipeR', 'inscriptis', 'html_text', 'Beau. Soup', 'html2text', 'Rcrawler', 'xPath', 'rvest']
 
 # Establecer la posición y el ancho del gráfico de barras
pos = list(range(len(green_data)))
width = 0.7
 
 # Dibujar
fig, ax = plt.subplots(figsize=(8,5))
 
plt.barh(pos, green_data, width,
                 alpha=0.5,
                 color='black',
                 label=labels[0])

#plt.barh([p + width*2 for p in pos], red_data, width,
                 #alpha=0.5,
                 #color='r',
                 #label=labels[1])


 # Establecer etiqueta y distancia
ax.set_xlabel('Tiempo de ejecución')
#ax.set_title('Grouped bar plot')
ax.set_yticks([p + 0.1 * width for p in pos])
ax.set_yticklabels(labels)
 
 # Establecer límites de los ejes x, y
plt.ylim(min(pos)-width, max(pos)+width)
#plt.xlim([0, 100])
 
 # Dibujar
plt.show()


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
'''
df = pd.DataFrame({
'group': ['html.parser','lxml','XML/xml2'],
'accuracy': [0.6718, 0.6902, 0.4570],
'precision': [0.7013, 0.7109, 0.4828],
'recall': [0.9362, 0.9600, 0.8993],
'f1': [0.7810, 0.7966, 0.5716]
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
ax.plot(angles, values, 'o-', color='red', linewidth=1, label='html.parse')
ax.fill(angles, values, 'red', alpha=0.1)

# Ind2
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, 'o-', color='green', linewidth=1, label='lxml')
ax.fill(angles, values, 'green', alpha=0.2)

# Ind3
values=df.loc[2].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, 'o-', color='blue', linewidth=1, label='XML/xml2')
ax.fill(angles, values, 'blue', alpha=0.1)

ax.legend(loc='best', bbox_to_anchor=(0.9, 0.2))

# Show the graph
plt.show()
'''