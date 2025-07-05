# Calculadora básica en Python

# Solicitar números al usuario
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
except ValueError:
    print("Entrada inválida. Debes ingresar números.")
    exit(1)

# Calcular resultados
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Validar división por cero
if num2 == 0:
    division = "Error: no se puede dividir por cero"
else:
    division = num1 / num2

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
