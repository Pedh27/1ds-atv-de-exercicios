# Exercício 05 - Operadores Lógicos e validações

nome = input("Digitei sua nome: ").strip()
idade = int(input("Digite sua idade: "))
resposta_ingresso = input("Possui ingresso válido? (s/n): ").strip().lower()
resposta_autorizacao = input("Possui autorização do responsável? (s/n): ").strip().lower()

ingresso = resposta_ingresso in ("s", "sim")
autorizacao = resposta_autorizacao in ("s", "sim")
ingresso_resposta_valida = resposta_ingresso in ("s", "sim", "n", "nao", "não")
autorizacao_resposta_valida = resposta_autorizacao in ("s", "sim", "n", "nao", "não")

if idade < 0 or idade > 120 or not ingresso_resposta_valida or not autorizacao_resposta_valida:
    resultado = "Dados inválidos"
elif idade >= 18 and ingresso:
    resultado = "Entrada liberada"
elif idade >= 14 and ingresso and autorizacao:
    resultado = "Entrada liberada com autorização"
else:
    resultado = "Entrada não permitida"
    
print("\n--- CONTROLE DE ACESSO AO EVENTO ---")
print(f"Participante: {nome}")
print(f"Idade: {idade}")
print(f"Resultado: {resultado}")

if not ingresso and resultado != "Dados inválidos":
    print("Motivo: ingresso não confirmado.")