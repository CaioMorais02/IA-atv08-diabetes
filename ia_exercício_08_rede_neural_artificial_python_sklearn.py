# -*- coding: utf-8 -*-
"""IA - Exercício - 08 - Rede Neural Artificial - Python - SkLearn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kJVYPxyRbO_YkNOnuJOK2QVJqBvYr-lS

# Treinamento

### Carregando Arquivo de Treinamento (.csv)
"""

import pandas as pd
# Carregando dados do arquivo CSV
url = 'https://raw.githubusercontent.com/alcidesbenicasa/IA---2020.1---Exerc-cio---06---Rede-Neural-Artificial/main/dados_pacientes_treinamento.csv'
base_Treinamento = pd.read_csv(url,sep=';', encoding = 'latin1').values
print("---------------------------------")
print("Dados dos Pacientes - TREINAMENTO")
print("---------------------------------")
print(base_Treinamento)
print("---------------------------------")

# Extração dos Atributos a serem utilizadas pela rede
print("Atributos de Entrada")
print("---------------------------------")
print(base_Treinamento[:, 1:5])

print("----------------------------")
print("Classificação Supervisionada")
print("----------------------------")
print(base_Treinamento[:, 5])

"""### Pré-processamento de Dados"""

import numpy as np
from sklearn import preprocessing

# Binarizador de rótulo
lb = preprocessing.LabelBinarizer()

#A saída da transformação é também conhecido como codificação 1-de-n
#Transforma valores categóricos equidistantes em valores binários equidistantes.
#Atributos categóricos com valores sim e não
lb.fit(['sim', 'não'])
febre = lb.transform(base_Treinamento[:,1])
enjoo = lb.transform(base_Treinamento[:,2])
dores = lb.transform(base_Treinamento[:,4])

#Atributos categóricos com valores pequenas e grandes
lb.fit(['grandes', 'pequenas'])
manchas = lb.transform(base_Treinamento[:,3])

#Atributos categóricos com valores saudável e doente
lb.fit(['saudável', 'doente'])
classes = lb.transform(base_Treinamento[:,5])

#Concatenação de Atributos (Colunas)
atributos_norm = np.column_stack((febre,enjoo,manchas,dores))
print("--------------------------------")
print("Atributos de Entrada - Numéricos")
print("--------------------------------")
print(atributos_norm)

print("----------------------------------------")
print("Classificação Supervisionada - Numéricos")
print("----------------------------------------")
diagnostico_norm = np.hstack((classes))
print(diagnostico_norm)

"""### Treinamento do Neurônio Perceptron"""

from sklearn.linear_model import Perceptron
# Treinamento do Perceptron a partir dos atributos de entrada e classificações
modelo = Perceptron()
modelo.fit(atributos_norm, diagnostico_norm)

# Acurácia do modelo, que é : 1 - (predições erradas / total de predições)
# Acurácia do modelo: indica uma performance geral do modelo.
# Dentre todas as classificações, quantas o modelo classificou corretamente;
# (VP+VN)/N
print('Acurácia: %.3f' % modelo.score(atributos_norm, diagnostico_norm))

"""### ----------------------------------------------------------------------------

# Validação do Aprendizado

### Predição Simples
"""

Luiz = [[0,0,1,1]]
print("Luiz", modelo.predict(Luiz))
Laura = [[1,1,0,1]]
print("Laura", modelo.predict(Laura))

"""### Predição a partir de base de dados (.csv)"""

import pandas as pd
# Carregando dados do arquivo CSV
url = 'https://raw.githubusercontent.com/alcidesbenicasa/IA---2020.1---Exerc-cio---06---Rede-Neural-Artificial/main/dados_pacientes_teste.csv'
base_Testes = pd.read_csv(url,sep=';', encoding = 'latin1').values
print("----------------------------")
print("Dados dos Pacientes - TESTES")
print("----------------------------")
print(base_Testes)
print("---------------------------------")

# Extração dos Atributos a serem utilizadas pela rede
print("Atributos de Entrada")
print("---------------------------------")
print(base_Testes[:, 1:5])

"""### Pré-processamento de Dados"""

import numpy as np
from sklearn import preprocessing

# Binarizador de rótulo
lb = preprocessing.LabelBinarizer()

#A saída da transformação é também conhecido como codificação 1-de-n
#Transforma valores categóricos equidistantes em valores binários equidistantes.
#Atributos categóricos com valores sim e não
lb.fit(['sim', 'não'])
febre = lb.transform(base_Testes[:,1])
enjoo = lb.transform(base_Testes[:,2])
dores = lb.transform(base_Testes[:,4])

#Atributos categóricos com valores pequenas e grandes
lb.fit(['grandes', 'pequenas'])
manchas = lb.transform(base_Testes[:,3])

#Concatenação de Atributos (Colunas)
atributos_norm = np.column_stack((febre,enjoo,manchas,dores))
print("--------------------------------")
print("Atributos de Entrada - Numéricos")
print("--------------------------------")
print(atributos_norm)

"""### Predição da Base"""

base_Predicao = modelo.predict((atributos_norm))
print("Classificações: ", base_Predicao)

"""### Retorno aos valores Categóricos"""

import numpy as np
from sklearn import preprocessing

# Binarizador de rótulo
lb = preprocessing.LabelBinarizer()

#A saída da transformação é também conhecido como codificação 1-de-n
#Transforma valores categóricos equidistantes em valores binários equidistantes.
#Atributos categóricos com valores sim e não
lb.fit(['sim', 'não'])
febre = lb.inverse_transform(atributos_norm[:,0])
enjoo = lb.inverse_transform(atributos_norm[:,1])
dores = lb.inverse_transform(atributos_norm[:,3])

#Atributos categóricos com valores pequenas e grandes
lb.fit(['grandes', 'pequenas'])
manchas = lb.inverse_transform(atributos_norm[:,2])

#Atributos categóricos com valores saudável e doente
lb.fit(['saudável', 'doente'])
predicao = lb.inverse_transform(base_Predicao)

#Concatenação de Atributos (Colunas)
atributos_cat = np.column_stack((base_Testes[:,0],febre,enjoo,manchas,dores,predicao))
print("--------------------------------")
print("Atributos de Entrada - Numéricos")
print("--------------------------------")
print(atributos_cat)