def c_p_f(celcius):
  fahrenheit = (celcius * 9/5) + 32
  return fahrenheit

entrada = float(input("Digite a temperatura em Celsius: "))

print(f"A temperatura em Fahrenheit é: {c_p_f(entrada)}")