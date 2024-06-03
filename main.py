import pandas as pd

data = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Mateus' , 'Lucas' , 'Brutus'],
    'Idade': [23, 25, 30, 22, 19, 11, 4],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Salvador' , 'Salvador' , 'Salvador']
}
df = pd.DataFrame(data)

df['Ano de Nascimento'] = 2024 - df['Idade']
df['Maiores de idade'] = df['Idade'] >= 18


print(df)