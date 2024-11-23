class Button:
    def __init__(self, label, color, shape):
        self.label = label
        self.color = color
        self.shape = shape
        self.checking = 0

    def set_text_to_click(self, text):
        self.checking = 1
        self.text = text
        print('Задан текст для вывода')

    def del_text_to_click(self):
        self.checking = 0
        print('Текст для вывода удалён')

    def click(self):
        if self.checking == 1:
            print(f'Кнопка нажата. Выведен текст:\n{self.text}')
        else:
            print('Кнопка нажата.')

    def info(self):
        print(f'Название: {self.label}\nЦвет: {self.color}\nФорма: {self.shape}')


button = Button('Привет!', 'red', 'round')
button.click()
button.set_text_to_click('Здравствуйте!')
button.click()
button.info()
