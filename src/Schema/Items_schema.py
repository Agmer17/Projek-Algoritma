import datetime
class Items :
    def __init__(self, name, category, stock, price, sellPrice, desc, supplier, status):
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price
        self.sellPrice = sellPrice
        self.entryDate = datetime.datetime.now()
        self.desc = desc
        self.supplier = supplier
        self.status = status