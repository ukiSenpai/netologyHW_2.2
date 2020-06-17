# Нужно реализовать Польскую нотацию для двух положительных чисел. Реализовать нужно будет следующие операции:
#
# Сложение
# Вычитание
# Умножение
# Деление
# Например, пользователь вводит: + 2 2 Ответ должен быть: 4

def calc_1():
    calc = input("Введите задачу через пробел: ").split()

    for i in calc:
        if i == "+":
            print(int(calc[1]) + int(calc[2]))
        if i  == "-":
            print(int(calc[1]) - int(calc[2]))
        if i  == "*":
            print(int(calc[1]) * int(calc[2]))
        try:
            if i == "/":
                print(int(calc[1]) / int(calc[2]))
        except Exception as e:
            print("Делиить на 0 нельзя! Ошиибка : ", e)

# Задача №2
#
# С помощью выражения assert проверять, что первая операция в списке доступных операций (+, -, *, /).
# С помощью конструкций try/expcept ловить ошибки и выводить предупреждения Типы ошибок:
#
# Деление на 0
# Деление строк
# Передано необходимое количество аргументов
# и тд.
def calc_2():
    calc = input("Введите задачу через пробел: ").split()
    try:
        assert calc[0] in ["+", "-", "*", "/"], "первым должен идти знак : + , - , * , /"
    except Exception as e:
        print(e)

    for i in calc:
        try:
            if i == "+":
                print(int(calc[1]) + int(calc[2]))
            if i == "-":
                print(int(calc[1]) - int(calc[2]))
            if i == "*":
                print(int(calc[1]) * int(calc[2]))
            if i == "/":
                print(int(calc[1]) / int(calc[2]))
        except ZeroDivisionError as e:
             print("Делиить на 0 нельзя! Ошиибка : ", e)
        except ValueError as e:
            print("Вы ввели строку! Ошиибка : ", e)
        except IndexError as e:
            print("Не хватает данных! Ошиибка :", e)

# Задача №3
#
# Расширить домашние задание из лекции 2.1 «Функции — использование встроенных и создание собственных» новой функцией, выводящей имена всех владельцев документов.
# С помощью исключения KeyError проверяйте, есть ли поле "name" у документа.


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "5455 028765" }

]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def show_names():
    for i in directories:
        for ia in directories[i]:
           for a in documents:
               try:
                 if ia == a["number"]:
                   print(a["name"])
               except KeyError as e:
                   print("У документа ", a["number"], " не назначенно имя владельца")


def main():
    calc_1()
    calc_2()
    show_names()

main()