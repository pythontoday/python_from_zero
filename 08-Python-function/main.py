def say_hello(username, age):
    """Функция приветствия пользователя"""
    
    print(f'Hello {username}!')
    print(f'Your age is {age}!')
    print('-' * 20)
    
    
# say_hello('Valera', 20)
# say_hello('mr.Anderson', 30)

# say_hello(username='Alex', age=35)
# say_hello(age=40, username='Anna')

def numbers_sum(username, num1=1, num2=2):
    print(f'Hello {username}!')
    print(num1 + num2)
    print(f'-' * 20)
    
    
# numbers_sum(num1=2, num2=7)
# numbers_sum(num1=13, num2=5)
# numbers_sum(num1=78, num2=349)
# numbers_sum()
# numbers_sum(username='Olga', num1=78)
# numbers_sum('Victor', num1=78)
# numbers_sum('Victor')
# numbers_sum('Max', num1=78, num2=-400)
    
    
# def check_user(username, age=0):
#     print(f'Hello {username}!')
    
#     if age >= 21:
#         print('Welcome to the club!')
    
#     print(f'-' * 20)
    
    
# check_user(username='Oleg')
# check_user(username='Svetlana', age=22)


def numbers_sum(num1=1, num2=2):
    return num1 + num2


print(numbers_sum(num1=7, num2=333))
result = numbers_sum(num1=13, num2=27)
print(result)

