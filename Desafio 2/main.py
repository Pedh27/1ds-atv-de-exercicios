nota1 = float(input("Digite a primeira nota: ").replace(",", "."))
nota2 = float(input("Digite a segunda nota: ").replace(",", "."))
minutos_estudo = int(input("Digite o total de minutos estudados: "))
questoes_corretas = int(input("Digite a quantidade de questões corretas: "))
total_questoes = int(input("Digite o total de questões: "))
 
soma_notas = nota1 + nota2
media = round(soma_notas / 2, 2)
diferenca = abs(nota1 - nota2)
horas_estudo = minutos_estudo // 60
minutos_restantes = minutos_estudo % 60
aproveitamento = round((questoes_corretas / total_questoes) * 100, 1)
pontos_bonus = questoes_corretas ** 2
 
print("\n--- RESUMO DE DESEMPENHO ---")
print(f"Soma das notas: {soma_notas:.2f}")
print(f"Média: {media:.2f}")
print(f"Diferença entre as notas: {diferenca:.2f}")
print(f"Tempo de estudo: {horas_estudo} h e {minutos_restantes} min")
print(f"Aproveitamento: {aproveitamento:.1f}%")
print(f"Pontos de bônus: {pontos_bonus}")