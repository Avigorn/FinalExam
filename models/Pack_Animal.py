from models.Animal import Animal


class Pack_Animal(Animal):
    def __init__(self, name, birthday, weight, type_animal):
        super().__init__(name, birthday, weight, type_animal)