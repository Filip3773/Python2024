a = int(input("broj:"))
s = a // 100
d = (a//10)//10
j = (a%100)%10
z = (s*d*j)-(s+d+j)
print(z)

