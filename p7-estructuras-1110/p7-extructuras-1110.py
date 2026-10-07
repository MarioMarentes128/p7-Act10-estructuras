# Mario Yañez NC 1110
#Condiciones 
# EJEMPLO 1
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")

#EJEMPLO 2
numero = int(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo")

#if/Elif
# EJEMPLO 1
calificacion = int(input("Ingresa tu calificación: "))

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")
elif calificacion >= 60:
    print("Suficiente")

#EJEMPLO 2
edad = int(input("Ingresa tu edad: "))

if edad < 13:
    print("Niño")
elif edad < 18:
    print("Adolescente")
elif edad >= 18:
    print("Adulto")

#if/Else
#EJEMPLO 1
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

#EJEMPLO 2
contraseña = input("Ingresa la contraseña: ")

if contraseña == "1234":
    print("Acceso permitido")
else:
    print("Acceso denegado")

#Ciclo For
#EJEMPLO 1
for numero in range(1, 6):
    print(numero)

#EJEMPLO 2
for numero in range(1, 11):
    print(numero * 2)

#Ciclo While
#EJEMPLO 1
numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1

#EJEMPLO 2
numero = int(input("Ingresa un número mayor que 0: "))

while numero <= 0:
    numero = int(input("Ingresa otro número: "))

print("Número válido:", numero)

print("Mario Yañez NC 1110")