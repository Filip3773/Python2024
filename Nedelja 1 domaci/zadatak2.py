
import math
print("Popunite parametre kvadratne jednacine ax+bx+c")
a=int(input("Unesite a:"))
b=int(input("Unesite b:"))
c=int(input("Unesite c:"))

x1 = (-b + ((b**2 - 4*a*c)**0.5))/2
x2 = (-b - ((b**2 - 4*a*c)**0.5))/2
 
x1= str(x1) 
x2= str(x2) 
print("x1 : "+ x1 +"x2 : " + x2+ ".")

