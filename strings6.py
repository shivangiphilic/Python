vowels = ['a','e','i','o','u','A','E','I','O','U']

s = input("Enter a string: ")

#No. of Vowels
v = 0
for char in s:
    if char in vowels:
        v+=1
print(v,"Vowels")

#No. of spaces
print(s.count(" "),"Spaces")

#Longest word
l = s.split()
longest = ""            #initially len(longest) is 0
for word in l:
    if len(word) >= len(longest):
        longest = word           #store longest word
print("Longest word is",longest)
