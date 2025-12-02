%pip install unidecode openpyxl
%pip install pandas
%pip install plotly.express

import pandas as pd
from unidecode import unidecode
try:
  df = pd.read_csv('/content/Lifestyle_and_Health_Risk_Prediction_Synthetic_Dataset.csv')
except FileNotFoundError:
  print("Erro: Arquivo não encontrado. Por favor, verifique o nome do arquivo e o caminho.")

if 'df' in locals():
  display(df.head())

df.info()
print("\Valores faltando:")
print(df.isnull().sum())

colunas_numericas = ['age', 'weight', 'height', 'sleep', 'bmi']
print("colunas numericas:")
print(colunas_numericas)

df['age'] = df['age']
df['weight'] = df['weight']
df['height'] = df['height']
df['sleep'] = df['sleep']
df['bmi'] = df['bmi']
df.head()

df.rename(columns={
    'age': 'idade',
    'weight': 'peso',
    'height': 'altura',
    'exercise': 'exercicio',
    'sleep': 'sono',
    'sugar_intake': 'consumo_acucar',
    'smoking': 'fumante',
    'alcohol': 'alcool',
    'married': 'casado',
    'profession': 'profissao',
    'bmi': 'imc',
    'health_risk': 'risco_saude'
}, inplace=True)

display(df.head())

colunas_numericas = ['idade', 'peso', 'altura', 'sono', 'imc']

correlacao_peso_imc = df['peso'].corr(df['imc'])
correlacao_altura_imc = df['altura'].corr(df['imc'])
correlacao_idade_sono = df['idade'].corr(df['sono'])
correlacao_peso_sono = df['peso'].corr(df['sono'])
correlacao_altura_sono = df['altura'].corr(df['sono'])


print(f"Correlação entre Peso e IMC: {correlacao_peso_imc}")
print(f"Correlação entre Altura e IMC: {correlacao_altura_imc}")
print(f"Correlação entre Idade e Sono: {correlacao_idade_sono}")
print(f"Correlação entre Peso e Sono: {correlacao_peso_sono}")
print(f"Correlação entre Altura e Sono: {correlacao_altura_sono}")

"""
**Análise das Relações:**

Com base nos resultados das correlações e nos gráficos, podemos observar algumas relações entre as variáveis numéricas e o risco de saúde:

*   **Peso e IMC:** Há uma correlação positiva forte entre peso e IMC (aproximadamente 0.78). Isso é esperado, pois o IMC é calculado a partir do peso e da altura. Um peso maior geralmente resulta em um IMC maior, assumindo que a altura permanece constante.

*   **Altura e IMC:** Há uma correlação negativa moderada entre altura e IMC (aproximadamente -0.59). Isso também é esperado, pois o IMC é inversamente proporcional à altura (ao quadrado). Pessoas mais altas tendem a ter um IMC menor, assumindo que o peso permanece constante.

*   **Idade e Risco de Saúde:** O boxplot mostra que, em média, o risco de saúde tende a aumentar com a idade, embora haja uma grande variação na idade dentro de cada categoria de risco.

     Idade e Sono :  A correlação entre idade e sono é muito baixa (-0.02), indicando pouca relação linear entre essas duas variáveis.

*   **Peso e Sono:** A correlação entre peso e sono é muito baixa (-0.01), sugerindo que, neste conjunto de dados, não há uma relação linear significativa entre o peso de uma pessoa e a quantidade de horas que ela dorme.

*   **Altura e Sono:** A correlação entre altura e sono também é muito baixa (-0.016), indicando que não há uma relação linear significativa entre a altura e a quantidade de sono.


"""

import pandas as pd
import plotly.express as px


tabela_consumo_acucar = pd.crosstab(df['consumo_acucar'], df['risco_saude'])
display(tabela_consumo_acucar)


fig = px.bar(tabela_consumo_acucar, barmode='group', title='Risco de Saúde por Consumo de Açúcar')
fig.show()


tabela_fumante = pd.crosstab(df['fumante'], df['risco_saude'])
display(tabela_fumante)


fig = px.bar(tabela_fumante, barmode='group', title='Risco de Saúde por Hábito de Fumar')
fig.show()

tabela_alcool = pd.crosstab(df['alcool'], df['risco_saude'])
display(tabela_alcool)


fig = px.bar(tabela_alcool, barmode='group', title='Risco de Saúde por Consumo de Álcool')
fig.show()

import plotly.express as px

fig = px.scatter(df, x='peso', y='imc', title='Correlação entre Peso e IMC')
fig.show()

fig = px.scatter(df, x='altura', y='imc', title='Correlação entre Altura e IMC')
fig.show()

df['risco_saude'] = pd.Categorical(df['risco_saude'], categories=['low', 'medium', 'high'], ordered=True)

fig = px.box(df, x='risco_saude', y='idade', title='Relação entre Idade e Risco de Saúde')
fig.show()
