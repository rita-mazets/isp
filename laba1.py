#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def fibonacci(number):
    num1 = num2 = 1
    for _ in range(number):
        yield num1
        num1, num2 = num2, num1 + num2


def main():
    while True:
        try:
            count = int(input("Введите количество чисел для ряда Фибоначчи:"))
        except ValueError:
            logging.info("Преобразование прошло неудачно")
            break

        if count < 1:
            logging.info("Введите положительное число!")
        else:
            logging.info(list(fibonacci(count)))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Упс, пора прощаться:(")
