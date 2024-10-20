# Задача "За честь и отвагу!"

from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        vragi = 100
        while vragi > 0:
            sleep(1)
            days += 1
            vragi -= self.power
            print(f'{self.name} сражается {days}-й день..., осталось {vragi} воинов.')

        print(f'{self.name} одержал победу спустя {days} дней(дня)!')
        print('Все битвы закончились!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
# Вывод строки об окончании сражения
first_knight.join()
second_knight.join()
