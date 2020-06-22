# class Dish:
#
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_amount_of_ingredients(self, amount_of_ingredients):
#         self.amount_of_ingredients = amount_of_ingredients
#
#     def set_ingredients(self, name, quantity, measure, ingredients):
#         self.name = name
#         self.quantity = quantity
#         self.measure = measure
#         ingredients["ingredient_name"] = name
#         ingredients["quantity"] = quantity
#         ingredients["measure"] = measure


try:
    with open("recipes.txt", "r") as file:
        for line in file:
            line = line.strip()
            if type(line) ==int :
                name = line
                print(type(name))

except Exception as e:
    print(e)


# def __repr__
