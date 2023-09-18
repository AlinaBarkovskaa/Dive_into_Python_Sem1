def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    num = int(input("Введите число (от 2 до 100000): "))
    if num < 2 or num > 100000:
        print("Число должно быть от 2 до 100000.")
    else:
        if prime(num):
            print(f"{num} - число простое.")
        else:
            print(f"{num} - число составное.")
except ValueError:
    print("Введите корректное число.")






