# Функция FizzBuzz — классическая задача на собеседованиях
def fizz_buzz(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Пример вызова функции
fizz_buzz(17)
