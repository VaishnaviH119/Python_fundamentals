# Create a class called Order which stores item and its price.
# Use Dunder function _ _gt_ _() to convey that:
#     order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order("Chips", 20)
ord2 = Order("Chocolate", 15)

print(ord1 > ord2)  
# This will print True if the price of ord1 is greater than the price of ord2

        