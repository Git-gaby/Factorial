# Pedimos el número al usuario
numero = int(input("Ingresa un número entero: "))

factorial = 1  # Valor inicial

# Bucle para calcular el factorial
for i in range(1, numero + 1):
    factorial *= i  # equivalente a factorial = factorial * i

print(f"El factorial de {numero} es {factorial}")