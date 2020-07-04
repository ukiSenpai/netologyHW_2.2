import time
from datetime import datetime




class SearchTime:
    def __init__(self, index):
        self.file = open(index, 'w')

    def __enter__(self):
        self.start_time = time.time()
        self.write(f'Начало работы {self.start_time}\n')
        self.now = datetime.now()
        print(f'Начало работы программы {self.start_time}\n')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        difference_time = time.time()-self.start_time
        if exc_type is not None:
            print(exc_type)
            self.write(f'error: {exc_val}')
        print(f'Окончание работы программы {time.time()}\n')
        self.write(f'Окончание работы {time.time()}\n')
        print(f'Программа работала {difference_time} секунд')
        self.write(f'Программа работала {difference_time} секунд')

    def age(self):
        print('Посчитаем, сколько дней ты живешь\n')
        try:
            self.year = int(input('Введите год'))
            self.month = int(input('Введите месяц'))
            self.day = int(input('Введите день'))
            print('\n')
            self.deadline = datetime(self.year, self.month, self.day)
            if self.deadline > self.now:
                print('Ты еще не родился')
                self.write(f'Ты еще не родился')
                self.life = None
            else:
                life = self.now - self.deadline
                self.life = life
                print(f'Ты живешь,{self.life.days} дней,{self.life.seconds} секунд,{self.life.microseconds} микросекунд\n')
                self.write(f'Ты уже живешь,{self.life.days} дней,{self.life.seconds} секунд,{self.life.microseconds} микросекунд"\n')
            return self.life
        except ValueError or AttributeError:
            print('Ошибочный ввод даты')

    def write(self, fixed):
        self.file.write(f'{datetime.now()}    {fixed}\n')



with SearchTime('test.txt') as file:
    file.age()
