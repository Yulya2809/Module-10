# Задача "Потоки гостей в кафе"


import random
from queue import Queue
from threading import Thread
from time import sleep

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.randint(3, 10))
        print(f"{self.name} покушал(-а) и ушёл(ушла)")

class Cafe:
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = list(args)

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    seated = True
                    break
            if not seated:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while True:
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                elif not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    table.guest.start()
            sleep(1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
