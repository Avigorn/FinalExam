from typing import Collection

from models.Animal import Animal
from models.Camel import Camel
from models.Cat import Cat
from models.Counter import Counter
from models.Dog import Dog
from models.Donkey import Donkey
from models.Hamster import Hamster
from models.Horse import Horse
from viewer.Model import Model


class Animal_Registry_Service(Model):
    def __init__(self):
        self.animal_registry: list[Animal] = []

    def get_new_animal(self, name: str, birthday: str, weight: float, type_animal: str) -> None:
        counter = Counter()
        animal_map = {
            "Кошка": Cat(name, birthday, weight, type_animal),
            "Собака": Dog(name, birthday, weight, type_animal),
            "Хомяк": Hamster(name, birthday, weight, type_animal),
            "Лошадь": Horse(name, birthday, weight, type_animal),
            "Верблюд": Camel(name, birthday, weight, type_animal),
            "Осел": Donkey(name, birthday, weight, type_animal),
        }

        animal = animal_map.get(type_animal)
        self.animal_registry.append(animal)
        assert animal
        counter.add_count()

    def load_animal(self) -> Collection[Animal]:
        return self.animal_registry

    def get_command_animal(self, name: str) -> None:
        for animal in self.animal_registry:
            if animal.name == name:
                print(animal.get_commands())

    def learn_command_animal(self, name: str, command: str) -> None:
        for animal in self.animal_registry:
            if animal.name == name:
                animal.add_command(command)
                print("Команда выучена")
