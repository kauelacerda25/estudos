# Condicionais

# São estruturas que permitem executar ao nosso programa tomar decisões com base em determinadas condições.
# Em outras palavras, o programa pode executar ações diferentes dependendo de uma situração específica.

#Exemplo de uso de condicionais em Python:

# Você está em uma cafeteria e está com pouca grana.
# O cappuciono custa 10 reais, café com leite 7 e o café simples 4.

# Se você tiver 10 reais ou mais, você compra o cappuccino.
# Se tiver entre 7 e 9 reais, compra o café com leite.
# Se não, pede café simples.

# if - se
# else - se não
# elif - se + se não


# if condição:
    # código a ser executado se a condição for verdadeira
# elif outra_condição:
    # código a ser executado se a outra condição for verdadeira
# else:
    # código a ser executado se nenhuma das condições anteriores for verdadeira

# Exemplo prático

""" idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode entrar no evento.")
else:
    print("Desculpe, você ainda não tem idade suficiente para entrar.") """

nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Parabéns! Você passou!")
elif nota >= 5:
    print("Você está de recuperação.")
else:
    print("Infelizmente, você foi reprado. Tente novamente no proximo ano.")