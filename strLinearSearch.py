s = input("Enter a string: ")
key = input("Enter char to search: ")
for i in range(0,len(s)):
    if s[i] == key:
        print(f"{key} is present at index {i+1}")
        break
