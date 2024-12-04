class Animal:
    def breathe(self):
        print("I breathe oxygen")

    def food(self):
        print("I eat food")

class Herbivores(Animal):
    def food(self, name):
        print(f"{name}: I am a Vegetarian")

class Carnivores(Animal):
    def food(self, name):
        print(f"{name}: I am a Non Vegetarian")

class Omnivores(Animal):
    def food(self, name):
        print(f"{name}: I eat both")

herbivore = Herbivores()
carnivore = Carnivores()
omnivore = Omnivores()

herbivore.breathe()
herbivore.food("Cow")

carnivore.breathe()
carnivore.food("Lion")

omnivore.breathe()
omnivore.food("Bear")
