a = int(input("broj:"))
h= a//1000
s = a // 100
d = (a//10)//10
j = (a%100)%10

z = (h+s+d+j)**2
print(z)