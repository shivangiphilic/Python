def palindrome (n):
    num = n
    revnum = 0
    while(num!=0):
        revnum = revnum*10 + num%10
        num = num//10
    return revnum

n = int(input("Enter a number: "))
rev = palindrome(n)
if (n==rev):
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")
