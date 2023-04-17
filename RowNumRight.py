n = int(input("Enter n: "))
for i in range(1,n+1):          #rows
    for j in range(n,i+1):      #col
        print(i, end = " ")
        j = j-1
    print("")
#FIXXXXXXXXXX