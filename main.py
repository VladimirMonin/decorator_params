# Решение домашней работы №20

def say_hello(name: str):
    """
    Функция приветствия
    :param name: Имя
    :return: None
    """
    print(f"Привет, {name}!")


def main():
    name = input("Пожалуйста введите ваше имя: ")
    say_hello(name)
    input("Нажмите Enter для выхода")


if __name__ == "__main__":
    main()
