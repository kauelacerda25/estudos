# Variáveis e tipos de dados "básicos"

# Uma variável é um espação na memória onde armazenamos um valor.

nome = "Kauê"   # variável do tipo string (texto), sempre entre aspas ("" ou '')
idade = 39      # var do tipo inteiro (número sem casa decimal)
altura = 1.78   # var do tipo float (número com casa decimal)
dev = True      # var do tipo booleano (verdadeiro ou falso) - True ou False

#print(f"Olá {nome}! Você tem {idade} anos e mede {altura}.")

nome = input("Qual é o seu nome? ")
idade = int(input("Quantos anos você tem? "))  # converte a entrada para inteiro
altura = float(input("Qual é a sua altura em metros? "))  # converte a entrada para float

print(f"Olá {nome}! Você tem {idade} anos e mede {altura} metros.")