# 4. Tabuada

# Peça um número e exiba sua tabuada (1 a 10).

num = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada de {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")