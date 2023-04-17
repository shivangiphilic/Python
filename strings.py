song = 'Blood, sweat and tears'
print(song)
print(song[0])
print(song[1])
print(song[-1])
print(song[-2])     #[x:y]excludes the numbers themselves
print(song[0:5])    #prints chars at indices 0,1,2,3,4
print(song[0:])     #prints chars from index 0 to end, -1 is assumed as end index
print(song[1:])     #prints chars from index 1 to end
print(song[:5])     #prints chars at 0,1,2,3,4; 0 is assumed as start index
print(song[1:-1])   #prints from chars at 1 to -1

copy = song[:]
print(copy)

#string methods
print(song.upper())
print(song.lower())
print(song.title())
print(song.find('t'))      #find function takes chars as an arg and returns index of its first occurrence, -1 if it's not present. Case sensitive
print(song.find('tears'))
print(song.replace('sweat','sweet'))
print(song.replace('Blood','Bloody'))
#to check for chars in a string, returns True or False
print('Bloody' in song)     #gives False cuz Bloody is not in song, it's only printed in previous line 
print('Blood' in song)

print(len(song))




