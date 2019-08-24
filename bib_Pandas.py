import pandas as pd

tit = pd.read_csv('titanic_data.csv')

### Informações do DataSet

tit.info()

# ### - Cálculos envolvendo colunas numéricas com dados faltantes podem sofrer impacto. É possível afirmar se há dados faltantes no dataset? Caso positivo, quais e quantos seriam esses dados? Preencha os dados faltantes de forma que não influenciem em operações futuras.

# Positivo - Lista com a quantidade de dados faltantes em cada coluna
tit.isnull().sum()
# A melhor maneira encontrada para aplicar na coluna Age foi de incluir a média
tit['Age'].fillna(tit['Age'].mean(), inplace=True)
# Na coluna Cabin foi inserido 0 nas informaçoes restantes
tit['Cabin'].fillna(0, inplace=True)

### Adequando o DataSet

### Algumas colunas não serão utilizadas, eventualmente é melhor excluí-las para que não interfiram na análise. Assim, exclua do dataset as colunas Sibsp, Parch e Ticket.

tit.drop('SibSp', axis=1, inplace=True)
tit.drop('Parch', axis=1, inplace=True)
tit.drop('Ticket', axis=1, inplace=True)

### Renomear as colunas restantes para a lingua portuguesa

tit.columns = ['IdPassageiro', 'Sobreviveu', 'Classe', 'Nome', 'Sexo', 'Idade', 'Tarifa', 'Cabine', 'Embarque']
### Alterar o conteudo da coluna Sobreviveu para:
# - 0 => Não
# - 1 => Sim
def alteracont(n):
    if n == 0:
        return 'Não'
    else:
        return 'Sim'

tit['Sobreviveu'] = tit['Sobreviveu'].map(alteracont)

### Alterar o conteudo da coluna Sexo para:
# - female => Mulher
# - male   => Homem

def alteracontSex(sex):
    if sex == 'female':
        return 'Mulher'
    else:
        return 'Homem'


tit['Sexo'] = tit['Sexo'].map(alteracontSex)

### Quantas mulheres e quantos homems estavam à bordo, de acordo com o dataset?

tit['Sexo'].value_counts()

### Quantos passageiros sobreviveram e quantos não sobreviveram?

tit['Sobreviveu'].value_counts()

### Quantas mulheres não sobreviveram?

tit.groupby(['Sexo', 'Sobreviveu']).size()['Mulher']['Não']

### Proporcionalmente, sobreviveram mais homens ou mais mulheres? Cite as proporções.

toths = tit.groupby(by=['Sobreviveu', 'Sexo']).size()['Sim']['Homem']
toth = tit.groupby(by=['Sexo']).size()['Homem']
proph = (toths / toth) * 100
totms = tit.groupby(by=['Sobreviveu', 'Sexo']).size()['Sim']['Mulher']
totm = tit.groupby(by=['Sexo']).size()['Mulher']
propm = (totms / totm) * 100
print('Proporção Homem -> {} \nProporção Mulher -> {}'.format(proph, propm))
if proph > propm:
    print('Sobreviveram mais Homens!')
else:
    print('Sobreviveram mais Mulheres!')

### Levando-se em consideração a idade dos passageiros, qual a idade e quantidade de pessoas com o maior número de mortos?

a = tit.groupby(by=['Sobreviveu', 'Idade']).size()['Não'].idxmax()
b = tit.groupby(by=['Sobreviveu', 'Idade']).size()['Não'].max()
print('Idade maior numero de mortos: {} anos \nQuantidade: {} pessoas'.format(int(a), b))

### Qual a média de idade dos homens sobreviventes?

tit.groupby(by=['Sobreviveu', 'Idade']).size()['Sim'].mean()

### Levando-se em consideração passageiros prioritários (mulheres e crianças de até 15 anos independente do sexo) qual a proporção de sobreviventes por sexo?

df1pri = pd.DataFrame(tit[(tit['Idade'] < 16) | (tit['Sexo'] == 'Mulher')])
dfpri = pd.DataFrame(df1pri.groupby(by=['Sobreviveu', 'Sexo']).size()['Sim'])
dfpri['Proporção'] = (dfpri[0] / tit['Sexo'].value_counts()) * 100

### Qual a quantidade de passageiros por classe?

tit.groupby(by=['Classe']).size()

### Qual o percentual de sobreviventes por classe?

df = pd.DataFrame(tit.groupby(by=['Sobreviveu', 'Classe']).size()['Sim'])
df['Percentual'] = (df[0] / tit['Classe'].value_counts()) * 100

### Crie um dataframe que demonstre a quantidade de sobreviventes e não sobreviventes, agrupados por sexo e classe.

tit.groupby(by=['Sobreviveu', 'Sexo', 'Classe']).size()   # !!! criar o dataframe

### Dos homens com idade entre 24 e 30 anos quantos da classe 3 sobreviveram? Quantos da classe 2 não sobreviveram?

# Classe 3 Sobreviveram
tit[((tit['Idade'] > 23) & (tit['Idade'] < 31)) & (tit['Classe'] == 3) & (tit['Sobreviveu'] == 'Sim')]

# Classe 2 Não Sobreviveram
tit[((tit['Idade'] > 23) & (tit['Idade'] < 31)) & (tit['Classe'] == 2) & (tit['Sobreviveu'] == 'Não')]

### Calcule a probabilidade condicional de uma pessoa sobreviver, dado seu sexo e a classe em que estava viajando:
# - P(S= true | G=female,C=1)
# - P(S= true | G=female,C=2)
# - P(S= true | G=female,C=3)
# - P(S= true | G=male,C=1)
# - P(S= true | G=male,C=2)
# - P(S= true | G=male,C=3)

fem_sob = pd.DataFrame(tit.groupby(by=['Sobreviveu', 'Sexo', 'Classe']).size()['Sim'])
fem_tot = pd.DataFrame(tit.groupby(by=['Classe']).size())
fem_sob['Probabilidae'] = (fem_sob / fem_tot) * 100
