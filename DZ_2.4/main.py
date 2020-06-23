def write_file(file):
    book = {}
    try:
        with open(file, "r") as files:
            for line in files:
                line = line.strip()
                if not line:
                    continue
                elif  line.isdigit():
                    amount_of_ingredients = line
                elif  "|" not in line:
                    dish_name = line
                    book[dish_name] = []
                else:
                    f = line.split("|")
                    name_ingredients = f[0]
                    amount = f[1]
                    measure = f[2]
                    book[dish_name].append(
                        {"ingredient_name": name_ingredients, "quantity": amount, "measure": measure})
    except Exception as e:
        print(e)
    return book


# def __repr__
cook_book = write_file("recipes.txt")
print(cook_book)



# Задача №2
#
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
#
# get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова
#
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:
#
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# Обратите внимание, что ингредиенты могут повторяться

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list ={}
    for n_dishes in dishes:
        for ingredients in cook_book[n_dishes]:
            if  ingredients["ingredient_name"] not in shopping_list:
                shopping_list[ingredients["ingredient_name"]] = {"measure":ingredients["measure"] , "quantity": int(ingredients["quantity"]) *person_count}
            else:
                shopping_list[ingredients["ingredient_name"]]["quantity"] += int(ingredients("quantity")) * person_count
    print(shopping_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)