#!/usr/bin/env python
# coding: utf-8

# # TABELA COMPARATIVA ENTRE O NÚMERO DE ACERTOS, NOTA MÍNIMA, MÉDIA E MÁXIMA NA PROVA DO ENEM 2019

# In[1]:


# importar as bibliotecas necessárias
import pandas as pd


# In[2]:


# caminho do arquivo onde serão extraídos os dados
caminho = 'C:/R/ENEM/2019/MICRODADOS/DADOS/MICRODADOS_ENEM_2019.csv'


# In[3]:


# colunas do arquivo a serem utilizadas
colunas = ["NU_INSCRICAO", "TP_PRESENCA_MT",
           "NU_NOTA_MT", "TX_RESPOSTAS_MT", "TX_GABARITO_MT"]


# In[4]:


# criar dataframe microdados
# este dataframe possui apenas dados a respeito da prova de matematica
dados = pd.read_csv(caminho, sep=';', usecols=colunas, encoding='ISO-8859-1')


# In[6]:


# visualizar as 5 primeiras linhas do dataframe criado
dados.head()


# In[7]:


# criar um novo dataframe apenas com os registros dos 
# estudantes presentes no segundo dia do enem 2019
dados1 = dados[dados['TP_PRESENCA_MT']==1].reset_index(drop=True)


# In[8]:


# visualizar as 5 primeiras linhas do dataframe criado
dados1.head()


# In[11]:


# Verificar as dimensões do dataframe criado.
# Ele possui 3.710.433 registros e 5 variáveis
dados1.shape


# In[14]:


# criar a variável 'n_linha' que recebe o número de linhas de 'microdados_mt'
n_linha = dados1.shape[0]

# exibir o valor da variável
display(n_linha)


# In[15]:


# criar uma lista com valores 0 e 1
# sendo 0 quando o estudante erra a questão e 1 quando ele acerta, comparado ao gabarito oficial de sua prova
n_acertos = [[1 if dados1['TX_RESPOSTAS_MT'][i][j] == dados1['TX_GABARITO_MT'][i][j] else 0 for j in range(45)] for i in range(n_linha)]


# In[19]:


# criar uma lista com o total de acertos de cada estudante
total_acertos = [sum(n_acertos[i]) for i in range(n_linha)]


# In[22]:


# criar um dataframe com a lista criada anteriormente
dados2 = pd.DataFrame({'NUM_ACERTOS': total_acertos, 'NOTA_MT':dados1['NU_NOTA_MT']})


# In[23]:


dados2


# In[28]:


# agrupar as notas pela quantidade de acertos e determinar a nota máxima para 
# cada acerto
gp_nota_max = dados2.groupby('NUM_ACERTOS').max().reset_index(drop=True)

# agrupar as notas pela quantidade de acertos e determinar a nota mínima para 
# cada acerto
gp_nota_min = dados2.groupby('NUM_ACERTOS').min().reset_index(drop=True)

# agrupar as notas pela quantidade de acertos e determinar a nota média para 
# cada acerto
gp_nota_med = dados2.groupby('NUM_ACERTOS').mean().reset_index(drop=True)

# criar lista com quantidades de erros de 0 a 45.
acertos = [n for n in range(46)]


# In[32]:


# criar dataframe a partir do numero de acerto, notas mínimas, médias e máximas para
# cada quantidade de acertos
tabela = pd.DataFrame({'NUM_ACERTOS':acertos, 'NOTA MÍNIMA': gp_nota_min['NOTA_MT'],
                       'NOTA MÉDIA': round(gp_nota_med['NOTA_MT'], 1), 'NOTA MÁXIMA': gp_nota_max['NOTA_MT']})


# In[33]:


#tabela final
tabela

