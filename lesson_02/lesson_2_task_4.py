def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("fizz_buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            return "Неверное число"


try:
    enter_number = int(input("Введите число 17: "))
    print(fizz_buzz(enter_number))
except ValueError:
    print("Пожалуйста введите целое число 17")
