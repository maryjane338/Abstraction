class Tamagochi:
    def __init__(self, name):
        self.name = name
        self.hunger = 80
        self.overfeeding = 0
        self.health = 20
        self.happiness = 20
        self.hygiene = 20
        self.energy = 20
        self.life = True

    def feed(self):
        if self.life is True:
            if self.hunger == 0:
                self.overfeeding += 10
                print(f'{self.name} уже сыт.')
                if self.overfeeding == 30:
                    self.life = False
                    print(f'{self.name} умер от обжорства.')
            else:
                self.hunger -= 20
                print(f'Вы покормили {self.name}')
        else:
            print(f'Вы не можете покормить {self.name}, потому что он скончался.')

    def play(self):
        if self.life is True:
            self.happiness += 20
            self.energy -= 5
            if self.overfeeding > 0:
                self.overfeeding = 0
            else:
                self.hunger += 5
            self.hygiene -= 5
            self.health -= 5
            if self.energy == 0:
                self.life = False
                print(f'{self.name} умер от переутомления.')
            elif self.hygiene == 0:
                self.life = False
                print(f'{self.name} умер от загрязнения.')
            elif self.hunger == 100:
                self.life = False
                print(f'{self.name} умер от голода.')
            else:
                print(f'Вы поиграли с {self.name}.')
        else:
            print(f'Вы не можете поиграть с {self.name}, потому что он скончался.')

    def heal(self):
        if self.life is True:
            self.health += 20
            self.happiness -= 5
            if self.happiness == 0:
                self.life = False
                print(f'{self.name} умер от скуки.')
            else:
                print(f'Вы полечили {self.name}.')
        else:
            print(f'Вы не можете полечить {self.name}, потому что он скончался.')

    def wash(self):
        if self.life is True:
            self.hygiene += 20
            self.happiness -= 5
            if self.happiness == 0:
                self.life = False
                print(f'{self.name} умер от скуки.')
            else:
                print(f'Вы помыли {self.name}.')
        else:
            print(f'Вы не можете помыть {self.name}, потому что он скончался.')

    def sleep(self):
        if self.life is True:
            self.energy = 100
            self.hunger += 5
            if self.hunger == 0:
                self.life = False
                print(f'{self.name} умер от голода.')
            else:
                print(f'{self.name} выспался, энергия восстановлена.')


    def info(self):
        if self.life is True:
            print(f'Голод: {self.hunger}\nЗдоровье: {self.health}\nСчастье: {self.happiness}\n'
                  f'Гигиена: {self.hygiene}\nЭнергия: {self.energy}')
        else:
            print(f'{self.name} скончался, поэтому вы не можете посмотреть информацию о нём.')


tamagochi = Tamagochi('Дружок')
tamagochi.info()
tamagochi.feed()
tamagochi.heal()
tamagochi.wash()
tamagochi.sleep()
tamagochi.play()
tamagochi.info()
