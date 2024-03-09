n = int(input())
a = n//100000
b = n//10000
c= n//1000
d = n // 100
e = (n//10)//10
f = (n%100)%10

def is_true():
    if a* c + 2 + f == b + (d*e) :
        return True
    else :
        return False

z =  str(is_true())
print(z)