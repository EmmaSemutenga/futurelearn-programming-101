#Python’s for statement iterates over the items of any sequence (a list or a string), 
# in the order that they appear in the sequence
for x in range(10, -10, -3):
    print(x)

dogs = ['puddle','maltese', 'German sherperd']
for dog in dogs:
    print(dog)
    for letter in dog:
        print(letter)

for position in range(len(dogs)):
    print(position)
    print(dogs[position])

#using break, continue and pass
#even and odd numbers

