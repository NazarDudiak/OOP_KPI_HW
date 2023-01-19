import random


class Menu:
    def __init__(self, default_menu=None):
        if default_menu:
            self.menu = default_menu
        else:
            self.menu = []

    def add_pizza(self, pizza):
        self.menu.append(pizza)

    def pizza_of_the_day(self):
        return random.choice(self.menu)


class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price


def main():
    сarbonara = Pizza("Carbonara", 110)
    hawaiian = Pizza("Hawaiian", 90)
    mushroom = Pizza("Mushroom", 100)
    meat = Pizza("Meat", 130)
    hunting = Pizza("Hunting", 140)
    quadruple_cheese = Pizza("Quadruple cheese", 150)
    pepperoni = Pizza("Pepperoni", 125)

    menu = Menu([сarbonara, hawaiian, mushroom, meat, hunting, quadruple_cheese, pepperoni])
    pizza_of_the_day = menu.pizza_of_the_day()
    print(f"Welcome!\n\t Today pizza of the day: {pizza_of_the_day.name} - Price: {pizza_of_the_day.price} UAH")
    choice = input("Want to see the whole menu [1] or buy the pizza of the day [2]?\n\t>>> ")
    if choice == "1":
        print("Our menu:")
        for i in menu.menu:
            print(f"\tPizza name: {i.name}; Price: {i.price} UAH;")

        pizza_name = input("\n\tEnter the name of the pizza you want to buy: ")
        for i in menu.menu:
            if pizza_name.lower() == i.name.lower():
                print(f"\nTo be paid {i.price} UAH. Thank you for your choice!")
                break
            else:
                continue
        else:
            print("Your pizza was not found :( See you soon!")
    elif choice == "2":
        print(f"To be paid {pizza_of_the_day.price} UAH. Thank you for your choice!")
    else:
        print("Choice variant was not found :( See you soon!")


if __name__ == "__main__":
    main()
