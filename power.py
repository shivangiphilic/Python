def power(b,e):
    if e==1:
        return b
    else:
        return b*power(b,e-1)


b = int(input("Enter base: "))
e = int(input("Enter exponent: "))
if e==0:
    print(1)
else:
    print(power(b,e))
