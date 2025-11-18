# 10. Fibonacci
# Mostre os 10 primeiros números da sequência de Fibonacci.

a, b = 0, 1
print("Os 10 primeiros números da sequência de Fibonacci são:")
for i in range(10):
    print(a)
    a, b = b, a + b
#