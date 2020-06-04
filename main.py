
class Animal:
    all_animal = []


    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.feed_animal = False
        self.all_animal.append(self)


    def feed_animals(self):
        if self.feed_animal == False:
            self.feed_animal = True
            print(f"Для {self.name} далии еду ")
        else:
            print(f"{self.name} уже дали еду, покормите позже" )

    def team_voice(self):
        print( f"{self.name} говорит {self.voice}")
class Artiodactyls(Animal):
    def get_resource(self):
        print(f"У животного {self.name} произошла {self.action} , собранны ресурсы ({self.resource})")
class Poultry(Animal):
    def get_resource(self):
        print(f"У птицы {self.name} собранны ресурсы ({self.resource})")
class Cow(Artiodactyls):
    resource = "Молоко"
    voice = "Муу"
    action = "дойка"
class Sheep(Artiodactyls):
    resource = "Шерсть"
    voice = "Мее"
    action = "стриижка"
class Goat(Artiodactyls):
    resource = "Молоко"
    voice = "Бее"
    action = "дойка"
class Geese(Poultry):
    resource = "Яйца"
    voice = "Га-Га"
class Duck(Poultry):
    resource = "Яйца"
    voice = "Кря-Кря"
class Сhicken(Poultry):
    resource = "Яйца"
    voice = "Ко-Ко-Ко"

geese1 = Geese("Серый", 6)
# geese1.feed_animals()
# geese1.feed_animals()
# geese1.team_voice()
# geese1.get_resource()

geese2 = Geese("Белый", 8)
# geese1.feed_animals()
# geese1.feed_animals()
# geese1.team_voice()
# geese1.get_resource()

cow1 = Cow("Манька", 140)
sheep1 = Sheep("Барашек", 40)
sheep2 = Sheep("Кудрявый", 50)
chicken1 = Сhicken("Ко-Ко", 2)
chicken2 = Сhicken("Кукареку", 2)
goat1 = Goat("Рога", 14)
goat2 = Goat("Копыта", 16)
duck = Duck("Кряква" , 4)


def main():
    for i in Animal.all_animal:
        i.feed_animals()
        i.team_voice()
        i.get_resource()
        i.feed_animals()
        print(sep="------")


    max_weight = Animal.all_animal[0]
    sum_weight = 0
    for i in Animal.all_animal:
        sum_weight += i.weight
        if max_weight.weight < i.weight:
            max_weight = i
    print(f"Самый большой вес у {max_weight.name} и он составляет {max_weight.weight}")
    print(f"Общиий вес {sum_weight}" )

main()