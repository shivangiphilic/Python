n = int(input("Enter a number: "))
num = n
revnum = 0
while(num!=0):
    revnum = revnum*10 + num%10
    num = num//10               #// returns only int part of quotient
    
if (n==revnum):
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")