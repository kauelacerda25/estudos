# Jogo de advinhação

# No jogo, o usuário precisa advinhar um número secreto.
# Ele pode tentar várias vezes até acertar.

numero_secreto = 10
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Digite um número entre 1 e 10: "))
    if tentativa < numero_secreto:
        print("Tente um número maior.")
    elif tentativa > numero_secreto:
        print("Tente um número menor.") 
    else:
    print("Você acertou!")