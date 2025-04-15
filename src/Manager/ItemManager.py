from src.Schema.Items_schema import Items
import json

class ItemManager : 
    
    @staticmethod
    def loadFile(path:str) -> dict[str:str] :
        try :
            with open(path, "r", encoding="utf-8") as files:
                data = json.load(files)
                return data
            
        except Exception as e:
            print("Error saat membaca file! harap perisa path nya! " + e)
            return {}
    
    @staticmethod
    def convertFileToClass(listItems:dict[str:dict]) : 
        data = {}
        if len(listItems) != 0 :
            for itemsName, itemData in listItems.items() :
                data.update({itemsName : Items(**itemData)})
            
            return data
        else : 
            return data
        
    def __init__(self, path):
        self.path = path
        data = self.loadFile(path)
        self.listData = self.convertFileToClass(data)
