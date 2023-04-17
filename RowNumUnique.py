num = int(input("Enter num: "))
n = 1
for i in range(0,num):            #rows
    for j in range(0,i+1):        #col
        print(n,end=" ")
        n = n+1
    print("\r")
    
