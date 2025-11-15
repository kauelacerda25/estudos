# for -> Quando sabemos quantas queremos repetir algo

#for numero in range(1, 6):
 #   print(numero)

#compras = ["Arroz", "Feijão", "Carne", "Macarrão", "Tomate"]    

#for item in compras:
   # print(f"Comprar: {item}") 

""" palavra = "Python"
for letra in palavra:
    print(letra) """


""" contador = 5 

while contador > 0:
    print(contador)
    contador -= 1  #contador = contador - 1
print("Fogo!!!") """

senha_correta = "12345"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")
print("Senha correta! Acesso liberado.")