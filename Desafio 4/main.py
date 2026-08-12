# Exercício 04 - Condições com if, elif e else
nome = input("Digite seu nome: ").strip()
nota1 = float(input("Digite a primeira nota: ").replace(",","."))
nota2 = float(input("Digite a segunda nota: ").replace(",","."))

media = (nota1 + nota2) / 2

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situcao = "Recuperação"
else:
    situacao = "Reprovado"
    
print("\n--- RESULTADO ESCOLAR ---")
print(f"Aluno: {nome}")
print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")