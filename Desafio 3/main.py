# Exercício 03 - Condições com if e else
nome = input("Digite seu nome: ").strip()
idade = int(input("Digite sua idade: "))
idade_minima = 14

print("\n--- VERIFICAÇÃO DE ACESSO ---")

if idade >= idade_minima:
    print(f"{nome}, seu acesso à oficina foi liberado.")
    print("Você já possui a idade mínima exigida.")
else:
    anos_faltantes = idade_minima - idade
    print(f"{nome}, seu acesso ainda não foi liberado.")
    print(f"Faltam {anos_faltantes} ano(s) para atingir a idade mínima.")