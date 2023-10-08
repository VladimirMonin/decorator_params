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

def say_goodbye(name: str):
    """
    Функция прощания
    :param name: Имя
    :return: None
    """

    print(f"До свидания, {name}!")

def main():
    name = input("Пожалуйста введите ваше имя: ")
    say_hello(name)
    say_something("Это моя первая программа")
    say_goodbye(name)
    input("Нажмите Enter для выхода")


if __name__ == "__main__":
    main()
