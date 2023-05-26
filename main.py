import random
import time

persons = [
    {
              'person': 'warrior',
              'HP': 100,
              'damage': 20,
              'best_enemy': 'mage'
    },
    {
              'person': 'mage',
              'HP': 50,
              'damage': 50,
              'best_enemy': 'archer'
    },
    {
              'person': 'archer',
              'HP': 70,
              'damage': 40,
              'best_enemy': 'warrior'
    }
        ]
colors_cmd = {
    'yellow': '\033[33m',
    'red': '\033[31m',
    'grey': '\033[37m',
    'purple': '\033[35m',
    'green': '\033[32m',
    'default': '\033[0m'
}
first_hero_sequence = []
second_hero_sequence = []
speed = 1


def change_color(text, color):
    return colors_cmd[color] + text + colors_cmd['default']


def round_of_fight(attacking_player, attacking_person, defending_player, defending_person):
    best_enemy = attacking_person['best_enemy'] == defending_person['person']
    knocking = attacking_person['damage'] * (1.5 if best_enemy else 1)
    print(attacking_player + '(' + change_color(attacking_person['person'], 'yellow') + ') наносит урон - ',
          change_color(str(knocking), 'red'))
    defending_person['HP'] -= knocking
    if defending_person['HP'] <= 0:
        print(defending_player + '(' + change_color(defending_person['person'], 'yellow') + ') убит')
        return
    print(defending_player + '(' + change_color(defending_person['person'], 'yellow') + '): HP - ',
          change_color(str(defending_person['HP']), 'green'))


def fight(first_person, second_person):
    first_kick = random.choice([True, False])
    print('Начало боя!',
          'По жеребьевке первый бьет',
          ('первый игрок(' + change_color(first_person['person'], 'yellow') + ')') if first_kick else
          ('второй игрок(' + change_color(second_person['person'], 'yellow') + ')'), '\n'
          )
    while True:
        if first_kick:
            round_of_fight('Первый игрок', first_person, 'Второй игрок', second_person)
            if second_person['HP'] <= 0:
                return True
        else:
            round_of_fight('Второй игрок', second_person, 'Первый игрок', first_person)
            if first_person['HP'] <= 0:
                return False
        print('')
        first_kick = not first_kick
        time.sleep(speed)


def choose_person(name):
    while True:
        player_input = input(name + ' - введи последовательность персонажей: ')
        hero_sequence = player_input.split()
        if len(set(hero_sequence) - {'1', '2', '3'}) > 0 or len(hero_sequence) != 5:
            print('Некорректные данные! Повторите ввод: ')
            continue
        choosen_hero_sequence = [persons[int(i)-1].copy() for i in hero_sequence]
        print('Вы выбрали такой порядок: ')
        for person in choosen_hero_sequence:
            print(change_color(person['person'], 'yellow'))
        return choosen_hero_sequence


def main():
    global second_hero_sequence, first_hero_sequence
    print("Есть 3 класса персонажей:", '\n')
    for person in persons:
        print(change_color('Класс: ', 'grey') + change_color(person['person'], 'yellow'),
              change_color('Жизнь: ', 'grey') + change_color(str(person['HP']), 'green'),
              change_color('Урон: ', 'grey') + change_color(str(person['damage']), 'red'),
              change_color('Лучший враг (х1.5 урон): ', 'grey') + change_color(person['best_enemy'], 'purple'),
              '\n', sep='\n'
              )
    print('Выбери 5 любых персонажей в той последовательности, в которой они будут сражаться',
          'Нужно указать 5 цифр через пробел, учитывая что 1 - '
          + change_color('warrior', 'yellow') + ', 2 - '
          + change_color('mage', 'yellow') + ', 3 - '
          + change_color('archer', 'yellow') + ','
          '(Например: 1 1 2 1 3)', sep='\n')
    first_hero_sequence = choose_person('Первый игрок')
    second_hero_sequence = choose_person('Второй игрок')
    first_person = first_hero_sequence.pop(0)
    second_person = second_hero_sequence.pop(0)
    while True:
        print('\n', 'Бой между ',
              change_color(first_person['person'], 'yellow'), '(первый игрок) и ',
              change_color(second_person['person'], 'yellow'), '(второй игрок)', '\n')
        time.sleep(speed)
        print('В запасе у игроков осталось: ',
              'Первый игрок - ' + str(len(first_hero_sequence)) + ' персонажей,',
              'Второй игрок - ' + str(len(second_hero_sequence)) + ' персонажей,', '', sep='\n'
              )
        time.sleep(speed)
        first_winner = fight(first_person, second_person)
        if first_winner:
            if len(second_hero_sequence) == 0:
                print('\n', 'Первый игрок - ПОБЕДИЛ!!!')
                return
            second_person = second_hero_sequence.pop(0)
        else:
            if len(first_hero_sequence) == 0:
                print('\n', 'Второй игрок - ПОБЕДИЛ!!!')
                return
            first_person = first_hero_sequence.pop(0)


if __name__ == '__main__':
    main()
