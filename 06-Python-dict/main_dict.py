# "имя": "Виктор"
# "возраст": 30

# my_dict1 = {}
# my_dict2 = dict()

# print(type(my_dict1))
# print(type(my_dict2))

my_dict = {
    "user": "Thomas Anderson",
    "nickname": "Neo",
    "team": ["Morpheus", "Trinity"],
    # [1, 2, 3]: "Hello"
    1: "Matrix",
    "has": "you",
    (1, 2, 3): "Hello"
}

# print(my_dict)

# print(my_dict["user"])
# print(my_dict[1])
# print(my_dict[(1, 2, 3)])

months = {1: "January", 2: "February"}
# print(months[2])

person = {"имя": "Виктор", "возраст": 27, "рост": 180}
# print(person["рост"])
# print(person["любимое блюдо"])

# print(person)
person["вес"] = 93
person["любимое блюдо"] = "карбонара"
# print(person)

person["вес"] = 109
# print(person)

# del person["любимое блюдо"]
# print(person)

person["машина"] = "Porsche"

# for k, v in person.items():
#     print(f"{k} >>> {v}")

# for key in person:
#     print(key)

# print("-" * 20)

# for key in person.keys():
#     print(key)

# if "рост" in person.keys():
# if "язык" in person.keys():
# if "язык" in person:
#     print("Данный ключ уже используется!")
# else:
#     print("Вы можете использовать данный ключ для создания пары.")

# for value in person.values():
#     print(value)

# print(person)

person = {
    'имя': 'Виктор',
    'возраст': 27,
    'рост': 180,
    'вес': 109,
    'любимое блюдо': ['карбонара', 'пельмешки', 'картошка с грибами'],
    'машина': 'Porsche'
}

# for values in person['любимое блюдо']:
#     print(values)

persons = {
    "Александр": {
        'возраст': 27,
        'рост': 180,
        'вес': 109,
        'любимое блюдо': ['карбонара', 'пельмешки', 'картошка с грибами'],
        'машина': 'Porsche'
    },
    "Ольга": {
        'возраст': 28,
        'рост': 165,
        'вес': 48,
        'любимое блюдо': ['кукуруза', 'креветки'],
        'машина': 'BMW'
    },
}

# for username, userinfo in persons.items():
#     print(f"Имя пользователя: {username}")
#     age = userinfo["возраст"]
#     car = userinfo["машина"]
    
#     print(f"Возраст пользователя {username} : {age} лет.")
#     print(f"Авто пользователя {username} : {car}\n")

print(person)
# print(person.get("имя"))
# print(person.get("адрес", "wtf dude?"))

# print(person.setdefault(5, "magic"))
# print(person)

# person_copy = person.copy()
# print(person_copy)

# person.update({"профессия": "слесарь"})
# print(person)
# person.update({"профессия": "программист"})
# print(person)

# print(person.pop("вес"))
# print(person.pop("весссс", "No key!"))

# print(person.popitem())
# print(person.popitem())
# print(person.popitem())
# print(person.popitem())

# print(person.keys())
# print(person.values())
# print(person.items())

person.clear()
print(person)
