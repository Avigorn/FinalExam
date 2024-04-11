from models.Animal_Registry_Service import Animal_Registry_Service
from viewer.Animal_Presenter import Animal_Presenter
from viewer.Animal_Nursery_View import Animal_Nursery_View


def main():
    registry = Animal_Registry_Service()
    nursery = Animal_Nursery_View()
    presenter = Animal_Presenter(registry, nursery)

    while True:
        choice = input(f"1 - Занести новое животное\n"
                       f"2 - Отобразить список команд\n"
                       f"3 - Обучить животное новым командам\n"
                       f"4 - Вывести всех животных питомника\n"
                       f"5 - Выйти\n")

        match choice:
            case "1":
                name, birthday, weight, type_animal = _get_animal_info()
                nursery.get_animal(name, birthday, weight, type_animal)

            case "2":
                name = input("Введите кличку животного: ")
                try:
                    registry.get_command_animal(name)
                except KeyError:
                    print("Такого животного нет")

            case "3":
                name, new_skill = _get_animal_and_skill()
                try:
                    registry.learn_command_animal(name, new_skill)
                except KeyError:
                    print("Такого животного нет")

            case "4":
                nursery.load_animals()

            case "5":
                break

            case _:
                print("Неверный выбор.")


def _get_animal_info():
    name = input("Введите кличку животного: ")
    birthday = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")
    weight = float(input("Введите вес животного: "))
    type_animal = input("Выберите тип животного:\n"
                        "1 - Кошка\n"
                        "2 - Собака\n"
                        "3 - Хомяк\n"
                        "4 - Лошадь\n"
                        "5 - Верблюд\n"
                        "6 - Осел\n")
    if type_animal == '1':
        type_animal = 'Кошка'
    elif type_animal == '2':
        type_animal = 'Собака'
    elif type_animal == '3':
        type_animal = 'Хомяк'
    elif type_animal == '4':
        type_animal = 'Лошадь'
    elif type_animal == '5':
        type_animal = 'Верблюд'
    elif type_animal == '6':
        type_animal = 'Осел'

    return name, birthday, weight, type_animal


def _get_animal_and_skill():
    name = input("Введите имя животного: ")
    new_skill = input("Введите команду: ")
    return name, new_skill


if __name__ == "__main__":
    main()
