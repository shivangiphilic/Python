#import math
def isPerfect(n):
    sum = 0
    i = 1
    while i < n:
        if n%i == 0:
            sum = sum + i 
        i = i+1   
    if sum == n:
        return True
    else:
        return False

n = int(input("Enter a number: "))
if(isPerfect(n)):
     print("perfect")
else:
    print("not perfect")