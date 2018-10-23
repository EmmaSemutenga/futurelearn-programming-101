t = 1234, "emz", 89877
print(type(t))
for me in t:
    print(me)

nums = [5,6,7,3,4,5,6]

del(nums[5])
print(nums)

#tuple
#tuple packing:
t = (344, 666, "hello") #tuple

#sequence unpacking 
x, y, z = t

print(x)

name = ['s','e','m','u','t','e','n','g','a']

print(set(name))

staff = {"name":"Semutenga", "age":23, 345:783}
print(staff[345])

countries = dict(africa = "uganda", asia="china", num=567)
print(countries["num"])


#looping techniques
cars = ["kigege", "pijot","corona","benz"]

for car in cars:
    print(car)

#indexes

for i in range(len(cars)):
    print(f"the index of {cars[i]} is {i}")

for k, v in enumerate(cars):
    print(f"the index of {v} is {k}")
#strings
for k, v in enumerate("semutenga"):
    print(f"the index of {v} is {k}")

#tuple
for k, v in enumerate(('hellos','egeg','hkryo','gtrytyr')):
    print(f"the index of {v} is {k}")

#sets
for k, v in enumerate({'fgfdg','dfgdf','gdgfdg','dfgdw'}):
    print(f"the index of {v} is {k}")

#dictionaries
for k, v in staff.items():
    print(f"the index of {v} is {k}")

#looping two or more sequencies using zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions,answers):
    print(f"what is your {q}? It is {a}")

#looping over a sequence in reverse
#strings
for i in reversed("semutenga"):
    print(i)

#lists
for i in reversed(questions):
    print(i)