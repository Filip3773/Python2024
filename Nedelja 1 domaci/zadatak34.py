n = int(input())
a = n//100000
b = n//10000
c= n//1000
d = n // 100
e = (n//10)//10
f = (n%100)%10

z = (a+b+c+d+e+f)**2 -(c*d)


print(z)