# Задача "Банковские операции"

import random
from threading import Thread, Lock
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def run(self):
        pass

    def deposit(self):
        deposit = random.randint(50, 500)
        for _ in range(100):
            self.balance += deposit
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                print(f"Пополнение: {deposit}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        deposit = random.randint(50, 500)
        for _ in range(100):
            print(f"Запрос на {deposit}")
            if deposit <= self.balance:
                self.balance -= deposit
                print(f"Снятие: {deposit}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()


# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
