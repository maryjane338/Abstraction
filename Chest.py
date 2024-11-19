class Chest:
    def __init__(self):
        self.content = []
        self.lock = 'locked'

    def open(self):
        if self.lock == 'locked':
            self.lock = 'unlocked'
            print('Вы открыли сундук.')
        else:
            print('Сундук уже открыт.')

    def put(self, thing):
        if self.lock == 'unlocked':
            self.content.append(thing)
            print(f'Вы положили {thing} в сундук.')
        else:
            print('Перед тем как класть предмет в сундук, откройте его.')

    def take(self, thing):
        if self.lock == 'unlocked':
            for i in range(len(self.content)):
                if self.content[i - 1] == thing:
                    i -= 1
                    self.content.pop(i)
                    break
            print(f'Вы взяли {thing} из сундука')
        else:
            print('Перед тем как брать предмет из сундука, откройте его.')

    def show_content(self):
        if self.lock == 'unlocked':
            print(f'Содержимое сундука: {', '.join(self.content)}')
        else:
            print('Перед тем как смотреть содержимое сундука, откройте его.')

    def close(self):
        if self.lock == 'unlocked':
            self.lock = 'locked'
            print('Вы закрыли сундук.')
        else:
            print('Сундук уже закрыт.')


chest = Chest()
chest.open()
chest.put('sword')
chest.put('shield')
chest.put('shield')
chest.put('arrows')
chest.take('shield')
chest.show_content()
chest.close()
