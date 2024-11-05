# Задача "Многопроцессное считывание"

import multiprocessing
import datetime
import threading

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            line = line.strip()  # Удаляем лишние пробелы и символы новой строки
            if line:  # Проверяем, что строка не пустая
                all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == '__main__':
    start = datetime.datetime.now()
    res = map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'линейный: {end - start}')

    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
        end = datetime.datetime.now()
        print(f'многопроцессный: {end - start}')
        