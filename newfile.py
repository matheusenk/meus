lista=[] 
for i in range(5):
	num = int(input("digite um numero: "))
	lista.append(num)
print(f"os numeros é: {lista}")
n2 = int(input("digite um numero pra saber ver se ta na lista: "))

v = n2 in lista

if v == True:
	print("Esta")
else:
	print("Nao esta")