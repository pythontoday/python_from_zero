# my_tuple = (1, 2, 3)
# print(type(my_tuple))

# my_tuple = tuple((1, 2, 3))
# print(type(my_tuple))

# my_tuple = 1
# print(my_tuple)
# print(type(my_tuple))

# my_tuple = 1,
# print(my_tuple)
# print(type(my_tuple))

# my_list = ["python", "is", "awesome"]
# my_tuple = ("python", "is", "awesome")

# print(my_list.__sizeof__())
# print(my_tuple.__sizeof__())

# my_tuple = ("python", "is", "awesome")

# print(my_tuple[0])
# print(my_tuple[1])
# print(my_tuple[2])

# print(my_tuple[0:2])
# print(my_tuple[0:3])
# print(my_tuple[:])

# print(len(my_tuple))

# my_tuple[0] = "php"

# my_tuple = ("python", "is", "awesome")
# print(my_tuple)
# print(id(my_tuple))

# my_list = list(my_tuple)
# print(my_list)

# my_list.append("and so useful")
# print(my_list)

# my_tuple = tuple(my_list)
# print(my_tuple)
# print(id(my_tuple))

# my_tuple = (1, 2, 3) + my_tuple
# print(my_tuple)
# print(id(my_tuple))

# my_tuple = ("python", "is", "awesome", [1, 2, 3], 85, ("a", "b", "c"), {"user": "Mr.Anderson"})
# print(my_tuple)
# print(id(my_tuple))

# my_tuple[3].append(99)
# print(my_tuple)
# print(id(my_tuple))

# my_tuple[0].append("JavaScript")
# print(my_tuple)

my_tuple = ("python", "is", "awesome", [1, 2, 3], 85, ("a", "b", "c"), 85, {"user": "Mr.Anderson"})

# print(my_tuple.count("python"))
# print(my_tuple.count(85))

# print(my_tuple.index(85))
# print(my_tuple.index("awesome"))

# del my_tuple[3]
del my_tuple
print(my_tuple)
