from models.Pack_Animal import Pack_Animal


class Horse(Pack_Animal):

    def __init__(self, name, birthday, weight, type_animal):
        super().__init__(name, birthday, weight, type_animal)
