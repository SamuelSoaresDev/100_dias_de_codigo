import pandas as pd
import numpy as np  

# Exemplo de criação de um dataFrame

data = {
    'nome':['Ana', 'João', 'Maria', 'Pedro', 'Lucas', 'Carla'],
    'departamento':['TI', 'RH', 'TI', 'Financeiro', 'TI', 'RH'],
    'salario':[5000, 4500, 5200, 6000, 4800, 4700]
}
df = pd.DataFrame(data) 

#filtragem dos funcionario  de TI
funcionarios_ti = df[df['departamento'] == 'TI']
print(funcionarios_ti)
 
# Média salario
media_salarial = funcionarios_ti['salario' ].mean()
print(f'A media salaria é: {media_salarial}')
