class ProductError(Exception):
    pass


class Product:
    def __init__(self, price, id, quantity):
        if isinstance(price, int) and price >= 0:
            self.__price = price
        else:
            raise ProductError("wrong input for price")
        if isinstance(id, int):
            self.__id = id
        else:
            raise ProductError("wrong input for id")
        if isinstance(quantity, int):
            self.__quantity = quantity
        else:
            raise ProductError("wrong input for quantity")

    def buy(self, count):
        if count <= self.__quantity:
            self.__quantity -= count
        else:
            raise ProductError("your count > quantity")

    def __repr__(self):
        return f"price-{self.__price}, id-{self.__id}, quantity-{self.__quantity}"

    @property
    def quantity(self):
        return self.__quantity

    @property
    def id(self):
        return self.__id


class InventoryError(Exception):
    pass


class Inventory:
    def __init__(self, lst):
        if isinstance(lst, list):
            for p in lst:
                if not isinstance(p, Product):
                    raise InventoryError("list members should be product type")
            else:
                self.__products = lst
        else:
            raise InventoryError("you should give a list for your constructor")

    def __repr__(self):
        return f"products are {self.__products}"

    def sum_of_products(self):
        sum = 0
        for l in self.__products:
            sum += l.quantity
        return sum

    def get_by_id(self, your_id):
        for l in self.__products:
            if l.id == your_id:
                return l
        else:
            return "no such product with your input id"


pr1 = Product(1200, 12, 3)
pr2 = Product(200, 1, 5)
pr3 = Product(900, 8, 79)
# print(pr1)
pr1.buy(2)
print(pr1.quantity)

lst = [pr1, pr2, pr3]
inv1 = Inventory(lst)
print(inv1)
print(inv1.sum_of_products())
print(inv1.get_by_id(4))
print(inv1.get_by_id(8))
