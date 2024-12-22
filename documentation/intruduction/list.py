letters = ['a', 'b', 'c', 'd', 'e']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

#Remove elements
letters[2:4] = []
print(letters)

# clear list
letters[:] = []
print(letters)