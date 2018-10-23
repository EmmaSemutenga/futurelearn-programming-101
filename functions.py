# calling a function before defining it
def main():
    '''This is a docstring'''
    for i in range(3):
        # hellos()
        embuza()


def hellos():
    print("Its 5 oclock in the morning")


# function name can be assigned to another name which can then be used as a function
embuza = hellos
# functions without a return statement do return a value called None (an inbuilt name)

if hellos() == None:
    print("Yey it returned something")

print(hellos())  # will return none
# function arguments take 3 forms
# main()
# or
if __name__ == "__main__":
    main()

# defining funtions with arguments takes 3 forms
# form 1, Default Argument Values


def addnumbers(n, m):

    return


#newsum = addnumbers(3,4) + 15
print(addnumbers(3, 6))

name = input("Put in your name")
# def ask_ok(prompt = "Do you really")


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


details = {"address": "Kampala", "job": "carpenter"}
print(details["address"])

mary = [1, 4, 5, 6, 78]
print(mary[:])
mary.append([45, 67, 89])
print(mary)
mary.extend(str(1000))
print(mary)


def maryiterator(item):
    for n in item:
        mary.append(n)


maryiterator("semutenga")
print(mary)
mary.extend((5, 7, 8))
print(mary)

books = {"george orwell": "Aniamal Farm", "Ngugi": "things fall apart"}
mary.extend(books.values())
print(mary)
print(type(list(books.values())))
l = []
for x in books.values():
    l.append(x)

mary.extend(l)
mary.insert(1, 100)
print(mary)
ages = [4, 5, 7, 4]
# ages.remove(4)
ages.pop()  # will return last item
ages.pop(2)
print(ages)
horses = ['billy', 'trudy', 'tago5', 'loom', 'pepper', 'hobb']
print(horses.index('loom', 1, len(horses)))
