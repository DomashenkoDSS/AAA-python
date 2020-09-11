def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Утка благополучно добралась до бара. '
        'А если бы она не взяла зонт, то сыграем заново? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step1()
    return print('Спасибо за внимание')


def step2_no_umbrella():
    print(
        'Утка промокла и до бара не дошла. '
        'Однако попала в ТЦ к петухам-штукатурам. Купить ли зонт?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return print('Утка-маляр благополучно добралась до бара с петухами-штукатурами.')
    return step_pay_umbrella()
def step_pay_umbrella():
    print('Ура, ☂️ есть, и утка попала в бар.' 
         'Хорошего отдыха!')
if __name__ == '__main__':
    step1()





