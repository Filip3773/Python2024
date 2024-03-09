a = int(input("broj:"))
h= a//1000
s = a // 100
d = (a//10)//10
j = (a%100)%10

z = ((h**2)+(j**2)) - (s**2 -d**2)
print(z)