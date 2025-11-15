# Simulando um Caixa Eletrônico

# O usuário tem um saldo inicial de R$ 500,00 e pode
# sacar dinheiro até zerar o saldo ou encerrar.

saldo = 500

while saldo > 0:
    saque = float(input("Informe o valor do saque: "))

    if saque == 0:
        break

    if saque > saldo:
        print("Saldo insuficiente. Saque não efetuado.")
    else:
        saldo -= saque
        print(f"Saque efetuado com sucesso! Novo saldo: {saldo:.2f}")

print("Operação encerrada.")