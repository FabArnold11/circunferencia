from math import*
a = float(input("Digite o valor de um cateto: "))
b = float(input("Digite o valor do outro cateto: "))

r = (sqrt(a**2 + b**2))/2
A = pi*r**2
C = 2*pi*r
print("O raio é igual a %.2f" %r)
print("A área é igual a %.2f" %A)
print("O comprimento da circunferência é igual a %.2f" %C)

input()
