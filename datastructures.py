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