class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    pass


class Customer:
    def __init__(self, name, surname, patronymic, mobile_phone, email=None):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone
        self.email = email

    pass


class Order:
    final_order = {"owner": None, "products": []}
    order_price = 0

    def __init__(self, order_name, order_no):
        self.order_name = order_name
        self.order_no = order_no

    def set_owner(self, owner):
        if self.final_order["owner"]:
            return "Owner already exist."
        else:
            self.final_order["owner"] = owner
            return "Order owner: " + owner.name

    def get_owner(self):
        if self.final_order["owner"]:
            return self.final_order["owner"].name
        else:
            return None

    def set_product(self, product):
        self.final_order["products"].append({"Product name": product.name,
                                             "Product price": product.price,
                                             "Product description": product.description,
                                             "Product dimensions": product.dimensions})

    def get_products(self):
        return self.final_order["products"]

    def calc_final_price(self):
        self.order_price = 0
        for i in self.final_order["products"]:
            self.order_price += i["Product price"]
        return self.order_price


NazarDudiak = Customer(name="Nazar",
                       surname="Dudiak",
                       patronymic="Oleksandrovich",
                       mobile_phone="+380 96 589 89 00",
                       email="dudyak.nazar@gmail.com")

Laptop = Product(name="Dell XPS 13",
                 price=1000,
                 description="Dell XPS 13\" 9350; 16GB/1024GB; I7-6560U",
                 dimensions="9mm X 304mm X 200mm")

Car = Product(name="Volkswagen Golf IV",
              price=4300,
              description="Engine: 1.9 TDI",
              dimensions="4148mm X 1735mm X 1440mm")

OrderRecord = Order("Laptop for Nazar", "02203200401")
OrderRecord.set_owner(NazarDudiak)
OrderRecord.set_product(Laptop)
OrderRecord.set_product(Car)
print("Final price", OrderRecord.calc_final_price())
