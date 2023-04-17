a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

sum = a+b+c
if a!=0 and b!=0 and c!=0:
    if sum == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")
else:
   print("Invalid Triangle")

