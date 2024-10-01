def gerar_tabuada(numero):
  print(f"Tabuada de {numero}:")
  for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Solicitar ao usuário que insira um número

numero  = int(input("Digite um número para gerar a tabuada: "))

# Chamar a função para gerar a tabuada

gerar_tabuada(numero)