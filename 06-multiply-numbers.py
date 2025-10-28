# leer archivo
with open("input.txt", "r") as file:
    lines = file.readlines()

first = []
second = []

# partir cada linea
# convertir en numeros
for line in lines:
    parts = line.strip().split()
    first.append( int( parts[0] ) )
    second.append( int( parts[1] ) )

# contar ocurrencias
ocurrencias = {}
for s in second:
    if s in ocurrencias:
        ocurrencias[s] += 1
    else:
        ocurrencias[s] = 1

# multiplicar numero de first por ocurrencias en second
resultado = 0
for f in first:
    if f in ocurrencias:
        resultado += (f * ocurrencias[f])

print(resultado)