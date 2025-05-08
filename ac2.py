import math
n=34.68
f=math.floor(n)
print("Floor of number:",f)
c=math.ceil(n)
print("Ceil of number:",c)

x=10
y=-24
print("After copysign operation:")
print(math.copysign(x,y))

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
print("GCD:", math.gcd(n1,n2))