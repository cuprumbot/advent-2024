# leer archivo
with open("input.txt", "r") as file:
    lines = file.readlines()

# imprimir cada linea
for line in lines:
    print(line, end="")
