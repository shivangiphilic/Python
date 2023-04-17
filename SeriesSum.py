n = int(input("Enter a natural no: "))
sum = 0
for i in range(2,n+1):
    sum = sum + (1/i)
print(f"Sum is {sum}")