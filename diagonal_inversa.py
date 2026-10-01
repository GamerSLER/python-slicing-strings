cuadrado  = []

for i in range(10):
	cuadrado.append([])
	for j in range(10):
		if i == j:
			cuadrado[i].append(1)
		else:
			cuadrado[i].append(0)

for l in cuadrado:
	print(l)
