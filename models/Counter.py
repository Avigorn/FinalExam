

class Counter:
    counter = 0

    def __init__(self):
        pass

    def add_count(self):
        Counter.counter += 1

    def get_counter(self):
        return Counter.counter
