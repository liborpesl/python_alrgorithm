# 1. rozvalime testo
# 2. pridame rajcatovy zaklad
# 3. pridame syr
# 4. pridame sunku
# 5. pridame cerstva rajcata, pokud je tam chceme.
# 6. upect


# 1. vzit_testo()
# 2. add_tomato_sauce() | add_ingredient(tomato_sauce)
# 3. add_ingredient(cheese)
# 4. add_ingredient(ham)
# 5. if chceme_rajcata:
#     add_ingredient(rajcata)
# 6. bake()


class Pizza:

    def __init__(self):
        self.ingredients = []
        self.is_baked = False

    def add_ingredient(self, ingredient: str):
        self.ingredients.append(ingredient)

    def __repr__(self) -> str:
        if self.is_baked:
            return f"Upecena Pizza({','.join(self.ingredients)})"
        else:
            return f"Neupecena Pizza({','.join(self.ingredients)})"

    def bake(self):
        if not self.is_baked:
            print("Baking...")
            self.is_baked = True
        else:
            print("Pizza is already baked")
            return


my_pizza = Pizza()
print(my_pizza)

my_pizza.add_ingredient("tomato_sauce")
my_pizza.add_ingredient("cheese")
my_pizza.add_ingredient("ham")
print(my_pizza)

my_pizza.bake()
print(my_pizza)


def make_my_pizza(chceme_rajcata: bool):
    pizza = Pizza()
    pizza.add_ingredient("tomato_sauce")
    pizza.add_ingredient("cheese")
    pizza.add_ingredient("ham")

    if chceme_rajcata:
        pizza.add_ingredient("tomatoes")

    pizza.bake()

    return pizza


def make_my_pizza2(chceme_rajcata: bool):
    pizza = Pizza()
    ingredients = ["tomato_sauce", "cheese", "ham"]

    if chceme_rajcata:
        ingredients.append("tomatoes")

    for ingredient in ingredients:
        pizza.add_ingredient(ingredient)

    pizza.bake()
    return pizza

