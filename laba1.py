import logging

logging.basicConfig(level=logging.INFO)


def fibonacci(number):
    fib1 = fib2 = 1
    for i in range(number):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


def main():
    is_correct = False
    while is_correct is False:
        try:
            number = int(input("Введите количество чисел для ряда Фибоначчи:"))
        except ValueError:
            logging.info("Преобразование прошло неудачно")
            continue
        if number < 1:
            logging.info("Введите положительное число!")
        else:
            is_correct = True
            data = list(fibonacci(number))
            print(data)


if __name__ == "__main__":
    main()
