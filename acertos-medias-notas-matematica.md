# TABELA COMPARATIVA ENTRE O NÚMERO DE ACERTOS, NOTA MÍNIMA, MÉDIA E MÁXIMA NA PROVA DO ENEM 2019


```python
# importar as bibliotecas necessárias
import pandas as pd
```


```python
# caminho do arquivo onde serão extraídos os dados
caminho = 'C:/R/ENEM/2019/MICRODADOS/DADOS/MICRODADOS_ENEM_2019.csv'
```


```python
# colunas do arquivo a serem utilizadas
colunas = ["NU_INSCRICAO", "TP_PRESENCA_MT",
           "NU_NOTA_MT", "TX_RESPOSTAS_MT", "TX_GABARITO_MT"]
```


```python
# criar dataframe microdados
# este dataframe possui apenas dados a respeito da prova de matematica
dados = pd.read_csv(caminho, sep=';', usecols=colunas, encoding='ISO-8859-1')
```


```python
# visualizar as 5 primeiras linhas do dataframe criado
dados.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NU_INSCRICAO</th>
      <th>TP_PRESENCA_MT</th>
      <th>NU_NOTA_MT</th>
      <th>TX_RESPOSTAS_MT</th>
      <th>TX_GABARITO_MT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>190001004627</td>
      <td>1</td>
      <td>369.1</td>
      <td>ADBBDEDCABCEDCACBECDCCEBCCDBEBDCEDDBCDBCCDECC</td>
      <td>BEDEEEAADBEBACABCDBABECECACADCBDCCEDCDABECDDD</td>
    </tr>
    <tr>
      <th>1</th>
      <td>190001004628</td>
      <td>1</td>
      <td>416.5</td>
      <td>DACCCBDCCCBACCCCEEEBBBEACCAABDBACDCAECABCCDBE</td>
      <td>AADDDBEEEBEDDBEBACABCDBABECECACAECDCBDCCEDCDA</td>
    </tr>
    <tr>
      <th>2</th>
      <td>190001004629</td>
      <td>1</td>
      <td>571.5</td>
      <td>DECCABCBCDBBBEAECBDBBCDDAADEBCBCACBBEDADDEEAC</td>
      <td>DBEBACABCDBABECEEEDCBDCCEDCDABEDAADDDECACAECB</td>
    </tr>
    <tr>
      <th>3</th>
      <td>190001004630</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>190001004631</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# criar um novo dataframe apenas com os registros dos 
# estudantes presentes no segundo dia do enem 2019
dados1 = dados[dados['TP_PRESENCA_MT']==1].reset_index(drop=True)
```


```python
# visualizar as 5 primeiras linhas do dataframe criado
dados1.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NU_INSCRICAO</th>
      <th>TP_PRESENCA_MT</th>
      <th>NU_NOTA_MT</th>
      <th>TX_RESPOSTAS_MT</th>
      <th>TX_GABARITO_MT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>190001004627</td>
      <td>1</td>
      <td>369.1</td>
      <td>ADBBDEDCABCEDCACBECDCCEBCCDBEBDCEDDBCDBCCDECC</td>
      <td>BEDEEEAADBEBACABCDBABECECACADCBDCCEDCDABECDDD</td>
    </tr>
    <tr>
      <th>1</th>
      <td>190001004628</td>
      <td>1</td>
      <td>416.5</td>
      <td>DACCCBDCCCBACCCCEEEBBBEACCAABDBACDCAECABCCDBE</td>
      <td>AADDDBEEEBEDDBEBACABCDBABECECACAECDCBDCCEDCDA</td>
    </tr>
    <tr>
      <th>2</th>
      <td>190001004629</td>
      <td>1</td>
      <td>571.5</td>
      <td>DECCABCBCDBBBEAECBDBBCDDAADEBCBCACBBEDADDEEAC</td>
      <td>DBEBACABCDBABECEEEDCBDCCEDCDABEDAADDDECACAECB</td>
    </tr>
    <tr>
      <th>3</th>
      <td>190001004632</td>
      <td>1</td>
      <td>605.3</td>
      <td>AAECDAEBBDCAAEDBACCBADDCBEAEACCCAEDBAEEAADDEB</td>
      <td>AADDDBEEEBEDDBEBACABCDBABECECACAECDCBDCCEDCDA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>190001004633</td>
      <td>1</td>
      <td>581.5</td>
      <td>DCAEDAAADEBEACDBADEACDECEACDACDCBEBAECBEEDABC</td>
      <td>BEDEEEAADBEBACABCDBABECECACADCBDCCEDCDABECDDD</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Verificar as dimensões do dataframe criado.
# Ele possui 3.710.433 registros e 5 variáveis
dados1.shape
```




    (3710433, 5)




```python
# criar a variável 'n_linha' que recebe o número de linhas de 'microdados_mt'
n_linha = dados1.shape[0]

# exibir o valor da variável
display(n_linha)
```


    3710433



```python
# criar uma lista com valores 0 e 1
# sendo 0 quando o estudante erra a questão e 1 quando ele acerta, comparado ao gabarito oficial de sua prova
n_acertos = [[1 if dados1['TX_RESPOSTAS_MT'][i][j] == dados1['TX_GABARITO_MT'][i][j] else 0 for j in range(45)] for i in range(n_linha)]
```


```python
# criar uma lista com o total de acertos de cada estudante
total_acertos = [sum(n_acertos[i]) for i in range(n_linha)]
```


```python
# criar um dataframe com a lista criada anteriormente
dados2 = pd.DataFrame({'NUM_ACERTOS': total_acertos, 'NOTA_MT':dados1['NU_NOTA_MT']})
```


```python
dados2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NUM_ACERTOS</th>
      <th>NOTA_MT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>369.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>416.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
      <td>571.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>605.3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13</td>
      <td>581.5</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3710428</th>
      <td>10</td>
      <td>488.5</td>
    </tr>
    <tr>
      <th>3710429</th>
      <td>15</td>
      <td>504.7</td>
    </tr>
    <tr>
      <th>3710430</th>
      <td>10</td>
      <td>552.0</td>
    </tr>
    <tr>
      <th>3710431</th>
      <td>7</td>
      <td>396.7</td>
    </tr>
    <tr>
      <th>3710432</th>
      <td>7</td>
      <td>470.2</td>
    </tr>
  </tbody>
</table>
<p>3710433 rows × 2 columns</p>
</div>




```python
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
```


```python
# criar dataframe a partir do numero de acerto, notas mínimas, médias e máximas para
# cada quantidade de acertos
tabela = pd.DataFrame({'NUM_ACERTOS':acertos, 'NOTA MÍNIMA': gp_nota_min['NOTA_MT'],
                       'NOTA MÉDIA': round(gp_nota_med['NOTA_MT'], 1), 'NOTA MÁXIMA': gp_nota_max['NOTA_MT']})
```


```python
#tabela final
tabela
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NUM_ACERTOS</th>
      <th>NOTA MÍNIMA</th>
      <th>NOTA MÉDIA</th>
      <th>NOTA MÁXIMA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0.0</td>
      <td>102.1</td>
      <td>359.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>359.0</td>
      <td>367.9</td>
      <td>396.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>359.0</td>
      <td>375.6</td>
      <td>436.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>359.0</td>
      <td>384.8</td>
      <td>477.6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>359.0</td>
      <td>395.2</td>
      <td>518.4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>359.0</td>
      <td>406.3</td>
      <td>544.6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>359.1</td>
      <td>419.0</td>
      <td>567.7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>359.2</td>
      <td>433.0</td>
      <td>586.4</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>359.4</td>
      <td>449.1</td>
      <td>610.1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>360.1</td>
      <td>466.8</td>
      <td>624.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>361.0</td>
      <td>486.7</td>
      <td>637.8</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>361.2</td>
      <td>508.9</td>
      <td>652.6</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>362.6</td>
      <td>532.7</td>
      <td>667.4</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>363.9</td>
      <td>557.5</td>
      <td>672.9</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>364.1</td>
      <td>583.2</td>
      <td>685.4</td>
    </tr>
    <tr>
      <th>15</th>
      <td>15</td>
      <td>373.1</td>
      <td>607.5</td>
      <td>693.6</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>379.1</td>
      <td>629.3</td>
      <td>703.1</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>388.0</td>
      <td>648.8</td>
      <td>712.7</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>416.0</td>
      <td>665.5</td>
      <td>723.1</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19</td>
      <td>382.0</td>
      <td>679.8</td>
      <td>730.2</td>
    </tr>
    <tr>
      <th>20</th>
      <td>20</td>
      <td>491.3</td>
      <td>692.6</td>
      <td>739.2</td>
    </tr>
    <tr>
      <th>21</th>
      <td>21</td>
      <td>516.2</td>
      <td>704.0</td>
      <td>750.2</td>
    </tr>
    <tr>
      <th>22</th>
      <td>22</td>
      <td>589.5</td>
      <td>715.1</td>
      <td>758.5</td>
    </tr>
    <tr>
      <th>23</th>
      <td>23</td>
      <td>594.1</td>
      <td>725.7</td>
      <td>764.1</td>
    </tr>
    <tr>
      <th>24</th>
      <td>24</td>
      <td>635.3</td>
      <td>735.8</td>
      <td>775.3</td>
    </tr>
    <tr>
      <th>25</th>
      <td>25</td>
      <td>670.1</td>
      <td>746.0</td>
      <td>785.4</td>
    </tr>
    <tr>
      <th>26</th>
      <td>26</td>
      <td>680.3</td>
      <td>755.9</td>
      <td>791.4</td>
    </tr>
    <tr>
      <th>27</th>
      <td>27</td>
      <td>693.3</td>
      <td>765.8</td>
      <td>808.2</td>
    </tr>
    <tr>
      <th>28</th>
      <td>28</td>
      <td>707.4</td>
      <td>776.0</td>
      <td>816.1</td>
    </tr>
    <tr>
      <th>29</th>
      <td>29</td>
      <td>719.1</td>
      <td>786.4</td>
      <td>826.1</td>
    </tr>
    <tr>
      <th>30</th>
      <td>30</td>
      <td>733.6</td>
      <td>796.4</td>
      <td>832.3</td>
    </tr>
    <tr>
      <th>31</th>
      <td>31</td>
      <td>739.7</td>
      <td>806.8</td>
      <td>842.5</td>
    </tr>
    <tr>
      <th>32</th>
      <td>32</td>
      <td>751.6</td>
      <td>817.6</td>
      <td>860.3</td>
    </tr>
    <tr>
      <th>33</th>
      <td>33</td>
      <td>770.1</td>
      <td>828.6</td>
      <td>867.8</td>
    </tr>
    <tr>
      <th>34</th>
      <td>34</td>
      <td>781.1</td>
      <td>840.1</td>
      <td>877.9</td>
    </tr>
    <tr>
      <th>35</th>
      <td>35</td>
      <td>795.0</td>
      <td>851.9</td>
      <td>887.3</td>
    </tr>
    <tr>
      <th>36</th>
      <td>36</td>
      <td>811.2</td>
      <td>864.3</td>
      <td>905.0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>37</td>
      <td>826.1</td>
      <td>876.9</td>
      <td>919.9</td>
    </tr>
    <tr>
      <th>38</th>
      <td>38</td>
      <td>833.8</td>
      <td>891.6</td>
      <td>929.6</td>
    </tr>
    <tr>
      <th>39</th>
      <td>39</td>
      <td>852.0</td>
      <td>906.4</td>
      <td>949.1</td>
    </tr>
    <tr>
      <th>40</th>
      <td>40</td>
      <td>868.6</td>
      <td>922.2</td>
      <td>963.0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>41</td>
      <td>884.7</td>
      <td>939.4</td>
      <td>975.2</td>
    </tr>
    <tr>
      <th>42</th>
      <td>42</td>
      <td>906.8</td>
      <td>955.8</td>
      <td>984.2</td>
    </tr>
    <tr>
      <th>43</th>
      <td>43</td>
      <td>927.3</td>
      <td>971.3</td>
      <td>985.0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>44</td>
      <td>959.7</td>
      <td>982.1</td>
      <td>985.5</td>
    </tr>
    <tr>
      <th>45</th>
      <td>45</td>
      <td>985.5</td>
      <td>985.5</td>
      <td>985.5</td>
    </tr>
  </tbody>
</table>
</div>


