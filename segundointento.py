nombre = input("Dime tu nombre:")
area   = input("De qué área eres:")
ventas = int(input("Cuántas ventas tuviste en el mes:"))

comisiones = round(ventas * 13/ 100,2)

print(f"Hola {nombre}, del área de {area}, tu comisión de este mes es de ${comisiones} ")