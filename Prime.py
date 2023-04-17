num = int(input("Enter a number: "))
count = 0 
for i in range (2,int(num)):
    if num%i == 0:
        count = count+1
    else:
        continue

if count==1:
    print("Prime")
else:
    print("Not prime")