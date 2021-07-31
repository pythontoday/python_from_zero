# my_list_1 = []
# print(type(my_list_1))

# my_list_2 = list()
# print(type(my_list_2))

# my_list = ["hello", 23, 7.2, ("1", "2", "3"), {"user1": "Victor"}, [5, 8, 22, 13], [], ""]
# print(my_list)

my_list_1 = [55, 2, 9, 0, 123, 47]
                #    -4                -3                -2                -1 
                #     0               1               2               3
my_list_2 = ["Выпить кофе", "Изучить Python", "Захватить мир", "Купить хлеба"]

# print(my_list_2[0])
# print(my_list_2[2])
# print(my_list_2[-1])

# print(len(my_list_2))
# print(my_list_2[:])

my_list_2.append("Купить билеты в Таиланд")
# print(my_list_2)

my_list_2.insert(1, "Принять душ")
# print(my_list_2)

# my_list_2.pop(-2)
my_list_2.pop()
# print(my_list_2)

list2 = ["Пожарить шашлыки", "Сходить в бассейн", "Пожарить шашлыки"]
my_list_2.extend(list2)
# print(my_list_2)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b

# print(c)

x = ["Hello"] + ["friend"] + [3301]
# print(x)

# print(my_list_2)
# my_list_2.remove("Пожарить шашлыки")
# print(my_list_2)

my_list_2_copy = my_list_2.copy()
# print(my_list_2_copy)

# print(my_list_2.count("Пожарить шашлыки"))
# print(my_list_2)
# print(my_list_2.index("Пожарить шашлыки"))

# print(my_list_2)
# my_list_2.sort()
# print(my_list_2)

n_list = [22, 9, 13, 99, 0, 4]
n_list.sort()
# print(n_list)

n_list.reverse()
# print(n_list)

# print(n_list)
# print(min(n_list))
# print(max(n_list))

words_list = ["за", "тобой", "выехали"]

# my_str = "".join(words_list)
my_str = " ".join(words_list)
my_str = "-".join(words_list)
# print(my_str)

print(words_list)
words_list.clear()
print(words_list)
