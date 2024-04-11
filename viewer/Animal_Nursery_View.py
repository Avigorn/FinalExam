from typing import Collection

from models.Animal import Animal
from viewer.View import View
from viewer.View_Observer import View_Observer


class Animal_Nursery_View(View):

    def __init__(self):
        self.observer = View_Observer

    def show_animals(self, animals: Collection[Animal]) -> None:
        for animal in animals:
            print(animal)

    def set_observer(self, observer):
        self.observer = observer

    def get_animal(self, name, birthday, weight, type_animal):
        self.observer.on_get_animal(name, birthday, weight, type_animal)

    def load_animals(self):
        self.observer.load_animal_register()

