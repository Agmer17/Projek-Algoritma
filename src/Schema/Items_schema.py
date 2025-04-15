import datetime
from .Suppliers_schema import Supplier
class Items :
    def __init__(self, name:str, category:str, stock:int, price:float, sellPrice:float, desc:str, supplier:Supplier, status:str):
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price
        self.sellPrice = sellPrice
        self.entryDate = datetime.datetime.now()
        self.desc = desc
        self.supplier = supplier
        self.status = status
        
    
    def addStock(self, amount):
        
        self.stock += amount

    def reduceStock(self, amount):
        if amount > self.stock:
            raise ValueError("stock melebihi kapasitas yang ada")
        self.stock -= amount

    def getStockValue(self):
        return self.stock * self.price

    def getPotentialRevenue(self):
        return self.stock * self.sellPrice

    def isInStock(self):
        return self.stock > 0

    def setStatus(self, status):
        self.status = status

    def updatePrice(self, newPrice):
        if newPrice < 0:
            raise ValueError("harga tidak boleh negatif")
        self.price = newPrice

    def updateSellPrice(self, newSellPrice):
        if newSellPrice < 0:
            raise ValueError("harga jual gaboleh negative")
        self.sellPrice = newSellPrice
    
    def getAllData(self) :
        return {
            "name": self.name,
            "category": self.category,
            "stock": self.stock,
            "price": self.price,
            "sellPrice": self.sellPrice,
            "entryDate": self.entryDate.strftime("%Y-%m-%d %H:%M:%S"),
            "desc": self.desc,
            "supplier": self.supplier,
            "status": self.status
        } 
