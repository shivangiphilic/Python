s = input("Enter a string: ")
l = s.split()           #split str into list of words
d={}
for i in l:
    d[i]=len(i)
print("Resultant Dictionary: ",d)