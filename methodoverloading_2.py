class Animal:
    def food_habit(self, animal_type, food=None):
        if food is None:
            if animal_type.lower() == "lion":
                return "Lions are carnivores and primarily eat meat."
            elif animal_type.lower() == "cow":
                return "Cows are herbivores and primarily eat grass."
            elif animal_type.lower() == "crow":
                return "Crows are omnivores and eat both plants and meat."
            else:
                return "Unknown animal type."
        else:
            return f"{animal_type.capitalize()}s typically eat {food}."
animal = Animal()
print(animal.food_habit("lion"))
print(animal.food_habit("cow"))
print(animal.food_habit("crow"))
print(animal.food_habit("lion", "buffaloes"))
print(animal.food_habit("cow", "hay"))
print(animal.food_habit("crow", "fruits and insects"))
