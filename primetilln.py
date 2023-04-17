n = int(input("Enter a number: "))
count = 0 
for i in range(2,n+1):
    for j in range (2,i):
        if i%j == 0:        
            break               #breaking out of inner loops, stop dividing by more nos
    else:
        print(i)