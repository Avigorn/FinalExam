from viewer.View_Observer import View_Observer


class Animal_Presenter(View_Observer):
    def __init__(self, animal_servserse, animal_viewer):
        self.animal_servserse = animal_servserse
        self.animal_viewer = animal_viewer
        animal_viewer.set_observer(self)

    def load_animals(self):
        return self.animal_servserse.load_animal()

    def load_reservation_animal_result(self, get_animal_result):
        self.animal_viewer.show_animals(get_animal_result)

    def on_get_animal(self, name, birthday, weight, type_animal):
        self.animal_servserse.get_new_animal(name, birthday, weight, type_animal)

    def load_animal_register(self):
        self.load_reservation_animal_result(self.animal_servserse.load_animal())
