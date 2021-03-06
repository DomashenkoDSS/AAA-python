class Pizza:
    """Базовый класс для создания пиццы"""
    def __init__(self, size='L'):
        if size == 'L':
            self.tomato_sauce = 100
            self.mozzarella = 100
        else:
            self.tomato_sauce = 200
            self.mozzarella = 200
        self.size = size
        if size not in ('L', 'XL'):
            raise AttributeError('Size should be L or XL')

    def dict(self):
        ingredients = [key for key in self.__dict__
                       if key not in ('size', 'name', 'symbol')]
        print(*ingredients, sep=', ')


class Margherita(Pizza):
    """Класс пиццы Маргарита"""
    def __init__(self, size='L'):
        super().__init__(size)
        self.name = 'Margherita'
        if size == 'L':
            self.tomatoes = 200
            self.mozzarella = 160
        else:
            self.tomatoes = 290
            self.mozzarella = 220
        self.symbol = '🍅'


class Pepperoni(Pizza):
    """Класс пиццы Паперрони"""
    def __init__(self, size='L'):
        super().__init__(size)
        self.name = 'Pepperoni'
        if size == 'L':
            self.pepperoni = 200
        else:
            self.pepperoni = 400
        self.symbol = '🍕'


class Hawaiian(Pizza):
    """Класс гавайской пиццы"""
    def __init__(self, size='L'):
        super().__init__(size)
        self.name = 'Hawaiian'
        if size == 'L':
            self.chicken = 200
            self.pineapples = 200
        else:
            self.chicken = 400
            self.pineapples = 400
        self.symbol = '🍍'
