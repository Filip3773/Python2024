b = str(input())
l = list(b)
l[0],l[2] = l[2],l[0]
b = "".join(l)
print(b)

