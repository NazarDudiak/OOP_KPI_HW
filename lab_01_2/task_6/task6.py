class Product:
    article = ""
    price = int()

    def __init__(self, article, price):
        self.article = article
        self.price = price
    pass


class Storage:
    storage_goods = {}

    def set_product(self, product, count):
        self.storage_goods[product.article] = {"article": product.article,
                                               "price": product.price,
                                               "count": 0}
        return self.storage_goods[product.article]

    def set_amount(self, article, count):
        self.storage_goods[article]["count"] = count
        return self.storage_goods[article]["count"]

    def get_products(self):
        print("=" * 40)
        for i in self.storage_goods.keys():
            article = self.storage_goods[i]["article"]
            price = self.storage_goods[i]["price"]
            count = self.storage_goods[i]["count"]
            print(f"| Article: [{article}]  Price: [{price}]  Count: [{count}]")
        print("=" * 40)
        return None

    def get_products_price(self):
        price = 0
        for i in self.storage_goods.keys():
            price += int(self.storage_goods[i]["price"]) * int(self.storage_goods[i]["count"])
        print("Price of all goods:", price)
        return price


def main():
    storage = Storage()

    print("\n\nAvailable operations:\n",
          "1: Create product and add product to storage;\n",
          "2: Set amount of products;\n",
          "3: Get all goods;\n",
          "4: Get all goods price;\n")

    option = input("Make choice: ")
    option_variants = {"1": "Create product and add product to storage",
                       "2": "Set amount of products",
                       "3": "Get all goods",
                       "4": "Get all goods price"}

    while option not in option_variants.keys():
        option = input("Wrong answer! Make choice: ")

    if option == "1":
        article = input("  Product article: ")
        price = input("  Product price: ")
        storage.set_product(Product(article, price), 0)
        main()
    elif option == "2":
        article = input("Enter product article: ")
        amount = input("Enter product amount: ")
        storage.set_amount(article, amount)
        main()
    elif option == "3":
        storage.get_products()
        main()
    elif option == "4":
        storage.get_products_price()
        main()
    else:
        pass


if __name__ == "__main__":
    main()
