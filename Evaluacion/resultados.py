from distutils.log import WARN
from turtle import color
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

X = [0.8544, 0.9273, 0.5107, 0.5129] #precision
Y = [0.8803, 0.8913, 0.9804, 0.9928] #recall

Z = [0.5404, 0.5130, 0.8649, 0.9101, 0.9208] #precision
W = [0.9875, 0.9928, 0.8573, 0.9370, 0.9699] #recall

A = [0.1371, 0.4628, 0.8486, 0.2401, 0.4714] #precision
B = [0.8974, 0.9310, 0.8696, 0.9915, 0.8885] #recall

annot1=["Boilerpy","Goose3","html2text","Beautiful Soup"]
annot2=["inscriptis","html_text","jusText", "Readability", "Trafilatura"]
annot3=["rvest","Rcrawler","boilerpipeR","XPath", "htm2txt"]


plt.figure(figsize=(8,6))
plt.scatter(X,Y,s=100,color="black", alpha=.5)
plt.scatter(Z,W,s=100,color="black", alpha=.5)
plt.scatter(A,B,s=100,color="black", alpha=.5)


for i, label in enumerate(annot1):
    plt.annotate(label, (X[i], Y[i]))

for i, label in enumerate(annot2):
    plt.annotate(label, (Z[i], W[i]))

for i, label in enumerate(annot3):
    plt.annotate(label, (A[i], B[i]))   

plt.xlabel("precision")
plt.ylabel("recall")
plt.ylim(0.8, 1)
plt.xlim(0, 1)
plt.show()


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
a = [0.1347, 0.1371, 0.8974, 0.2378] #rvest
b = [0.4540, 0.4628, 0.9310, 0.6181] #rcrawler
c = [0.4547, 0.4714, 0.8885, 0.6160] #htm2txt
d = [0.2421, 0.2401, 0.9915, 0.3866] #xpath

labels = ['accuracy', 'precision', 'recall', 'f1']
 
 # Establecer la posición y el ancho del gráfico de barras
pos = list(range(len(a)))
width = 0.2
 
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

# Establecer etiqueta y distancia
#ax.set_ylabel('y-value')
#ax.set_title('Grouped bar plot')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(labels)
 
 # Establecer límites de los ejes x, y
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, 1])
 
 # Dibujar
plt.legend(['rvest', 'Rcrawler', 'htm2txt', 'XPath'], loc='best')
plt.show()
'''

'''
# Los datos de entrada 
green_data = [4.4590, 3.5952, 25.9731, 2.5412, 2.9546, 39.9543, 2.1009, 1.1800, 3.1778, 4.4020, 158.0663, 80.5288, 0.7476, 60.3245]
labels = ['Trafilatura', 'Readability', 'Goose3', 'Boilerpy', 'jusText', 'boilerpipeR', 'inscriptis', 'html_text', 'Beau. Soup', 'html2text', 'Rcrawler', 'htm2txt', 'xPath', 'rvest']
 
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

'''
df = pd.DataFrame({
'group': ['rvest','Rcrawler','htm2txt', 'XPath'],
'accuracy': [0.1347, 0.4540, 0.4547, 0.2421],
'precision': [0.1371, 0.4628, 0.4714, 0.2401],
'recall': [0.8974, 0.9310, 0.8885, 0.9915],
'f1': [0.2378, 0.6181, 0.6160, 0.3866]
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
ax.plot(angles, values, 'o-', color='green', linewidth=1, label='rvest')
ax.fill(angles, values, 'green', alpha=0.1)

# Ind2
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, 'o-', color='blue', linewidth=1, label='Rcrawler')
ax.fill(angles, values, 'blue', alpha=0.2)

# Ind3
values=df.loc[2].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, 'o-', color='red', linewidth=1, label='htm2txt')
ax.fill(angles, values, 'red', alpha=0.1)

# Ind4
values=df.loc[3].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, 'o-', color='yellow', linewidth=1, label='XPath')
ax.fill(angles, values, 'yellow', alpha=0.1)

ax.legend(loc='best', bbox_to_anchor=(0.9, 0.2))

# Show the graph
plt.show()
'''