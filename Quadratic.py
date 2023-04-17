import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

D = (b**2)-(4*a*c)

if D>0:
    d = math.sqrt(D)
    print("Two distinct real roots")
    x1 = (-b-d)/2*a
    x2 = (-b+d)/2*a
    print(f"Roots are {x1} and {x2}")
elif D==0:
    x = -b/(2*a)
    print(f"Real repeated roots are {x} and {x}")
else:
    print("Imaginary roots")


