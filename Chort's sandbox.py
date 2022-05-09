from random import choice, randint

from termcolor import cprint

from random_names import get_name


class Chort:

    def __init__(self, name: str, money: int):
        self.name = name
        self.money = money
        self.all_hastle_money = 0
        self.lost_money = 0
        self.was_hastle = 0
        self.hastle_other_chort = 0

    def hastle(self, other) -> None:
        hastle_money = randint(1, 9)
        self.money += hastle_money
        self.all_hastle_money += hastle_money
        self.hastle_other_chort += 1
        other.money -= hastle_money
        other.lost_money += hastle_money
        other.was_hastle += 1
        cprint(f'{self.name} отжал у {other.name} {hastle_money} денег', 'magenta')

    def pontovatza(self) -> None:
        phrases = ['Ты пидор!', 'Где бабки, сука?', 'Если мутишь, мути тихо', 'Потрачено', 'Иди на хуй',
                   'У всех бывают неудачи, кроме меня', 'Ну понятно, иди в пизду', 'Ты ебучий бомж', 'Умри, гнида',
                   'Мне поебать', 'Чмо', 'Пидор, пидор, пидор, пидор, пошел нахуй', 'Ты внюханный что ли?', 'Атсасииии']
        phrase = choice(phrases)
        cprint(f'{self.name}: {phrase}', color='cyan')

    def slitsya(self):
        cprint(f'{self.name} слился', color='red')


if __name__ == '__main__':
    n = randint(10, 100)
    chorts_sandbox = [Chort(name=get_name(), money=randint(20, 30)) for i in range(1, n + 1)]
    moves = 0

    while len(chorts_sandbox) > 1:
        moves += 1
        for chort in chorts_sandbox:
            cube = randint(1, 2)
            if cube == 1:
                other_chort = choice(chorts_sandbox)
                while other_chort == chort:
                    other_chort = choice(chorts_sandbox)
                chort.hastle(other=other_chort)
            else:
                chort.pontovatza()
            if chort.money <= 0:
                chort.slitsya()
                chorts_sandbox.remove(chort)
    chort_winner = chorts_sandbox[0]
    cprint(f'Победил - {chort_winner.name}', color='blue')
    cprint(f'Нахастленные им деньги - {chort_winner.all_hastle_money}, у него денег нахастлили - '
           f'{chort_winner.lost_money}', color='green')
    cprint(f'Хастлил раз - {chort_winner.hastle_other_chort}, его хастлили раз - {chort_winner.was_hastle}',
           color='green')
    cprint(f'Всего сделано ходов - {moves}', color='yellow')
