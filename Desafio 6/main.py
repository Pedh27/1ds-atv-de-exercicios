# Exercício 06 - Repetição com for em Python
numero = int(input("Número da tabuada: "))
inicio = int(input("Multiplicador inicial: "))
fim = int(input("Multiplicador final: "))

if inicio > fim:
  print("Intervalo inválido")
else:
  print(f"\n--- TABUADA DO {numero} ---")
  for multiplicador in range(inicio, fim + 1):
      resultado = numero * multiplicador
      print(f"{numero} x {multiplicador} = {resultado}")