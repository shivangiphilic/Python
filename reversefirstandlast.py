#trytry
n = int(input("Enter a number: "))
temp = n
count = 0
while temp>0:
    temp = temp//10
    count = count-1
print(count)
first = n//(10**count)
last = n%10
print(last)
new = (n//10)*10*first
print(new)
last = ((new)%(10**count)+(last)*(10**count))
print(last)
