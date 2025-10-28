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

# ordenar
first.sort()
second.sort()

result = 0
for f, s in zip(first, second):
    result += abs(f - s)

print(result)