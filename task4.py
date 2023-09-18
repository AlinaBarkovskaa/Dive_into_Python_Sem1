from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Ты в игре 'Угадай число'!")
print(f"У тебя есть 10 попыток.")

for attempt in range(1, 10 + 1):
    try:
        guess = int(input(f"Попытка {attempt}: Введи число от {LOWER_LIMIT} до {UPPER_LIMIT}: "))

        if guess < LOWER_LIMIT or guess > UPPER_LIMIT:
            print("Введи число в правильном диапазоне.")
            continue

        if guess < secret_number:
            print("Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Ты угадал число {secret_number} с {attempt} попытки.")
            break

    except ValueError:
        print("Введи корректное число.")

if secret_number != guess:
    print(f"Игра окончена. Загаданное число было: {secret_number}. Попробуй ещё раз!")