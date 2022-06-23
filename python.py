# Classes
class MyClass:
    name = "Abi"

    def __init__(self, name, age) -> None:
          self.name = name,
          self.age = age
    
    def sum(self, a, b):
            print (a+b)

x = MyClass("John", 32)
print (x.name)
x.sum(4,5)
print(x.age)

# Lists

my_list = ["tokyo", "London", "New York"]
print(my_list)
print(my_list[0])

# List [] ordered | indexed | changable | duplicates
# Tuple () ordered | indexed | unchangable | duplicates
# set {} uordered | uindexed | unchangable | no duplicates
# Dictionary {K:V} uordered | indexed | changable | no duplicates

my_list[2] = 'Reading'

print(my_list)


# Loops

for val in my_list:
    print(val)

print(len(my_list))
my_list.append('hello')

my_list.insert(2, 'goodbye')
print(my_list)
my_list.reverse()
print(my_list)

my_tuple = ('cat', 'dog', 'monkey', 'hamster')
print(my_tuple)
# tuples start again if you minus 1
print(my_tuple[1 - 1])
print(my_tuple[1])

my_set = { 'hello', 'goodbye'}