# TALLER 6 PYTHON
# AUTOR EDUAR ALEJANDRO CANO MONTOYA
# FECHA: 27 DE SEPTIEMBRE DE 2022

from datetime import date
hoy=date.today() #fecha actual
print("Hoy es el dia: ", hoy)
print()
print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()
num1=int(input("digite un numero: "))
print("***Ciclo controlado por contador")
i=1
while i<=num1:
    print(i)
    i+=1
print("fin del ciclo")

print()
print("***Ciclo controlador por evento")
i=1
numero1=5
numero2=int(input("Digite un número del 1 al 10: "))
while numero2 !=numero1:
    i+=1
    numero2=int(input("Digite un número del 1 al 10: "))
print("Acertaste en el intento numero: ",  i)
print("fin del ciclo")

print()
print("***Ciclo abortado con la secuencia break")
amistad=input("Digite el nombre de una amistad: ")
amistad=amistad.upper()
for character in amistad:
    print(character)
    if character=="A":
        break
print("fin del ciclo")
print()
print("FIN")