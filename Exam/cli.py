import click
from pizza import Margherita, Pepperoni, Hawaiian
from random import randint

MENU = {'Margherita': Margherita(),
        'Pepperoni': Pepperoni(),
        'Hawaiian': Hawaiian()}


def log(template: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(template.format(randint(50, 1200)))
            return result

        return wrapper

    return decorator


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery_order', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
def order(pizza: str, size: str = 'L', delivery_order: bool = False):
    """Готовит и доставляет пиццу"""
    Menu = {'Margherita': Margherita(size),
            'Pepperoni': Pepperoni(size),
            'Hawaiian': Hawaiian(size)}
    if pizza not in Menu.keys():
        print(
            "Такой пиццы нет в меню. "
            "Выберите одну из других пицц: ")
        for element in MENU.values():
            print('--', element.name, element.symbol, ':')
            element.dict()
        return
    pizza_to_make = Menu[pizza]
    if delivery_order is False:
        bake(pizza_to_make)
    else:
        bake(pizza_to_make)
        delivery(pizza_to_make)


@cli.command()
def menu():
    """Выводит меню"""""
    print('У нас есть пиццы c размерами L и XL:')
    for element in MENU.values():
        print('--', element.name, element.symbol, ':')
        element.dict()


@log('👨‍🍳 Приготовили за {} с')
def bake(_):
    """"Готовит пиццу"""
    pass


@log('🚲 Доставили за {} с')
def delivery(_):
    """"Доставляет пиццу"""
    pass


if __name__ == '__main__':
    cli()
