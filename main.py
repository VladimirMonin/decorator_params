# Решение домашней работы №20

def say_hello(name: str):
    """
    Функция приветствия
    :param name: Имя
    :return: None
    """

    print(f"Привет, {name}!")


def say_something(something: str):
    """
    Функция вывода строки
    :param something: Строка
    :return: None
    """

    print(something)


def main():
    name = input("Пожалуйста введите ваше имя: ")
    say_hello(name)
    say_something("Это моя первая программа")
    input("Нажмите Enter для выхода")


if __name__ == "__main__":
    main()
