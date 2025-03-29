from src.admin import Admin_schema
from src.employees import Employees_schema
from src.suppliers import Suppliers_schema

import json
from .Auth_schema import Person

class PersonManager : 
    '''
    Person manager nih dipake buat nampung data dari semua class role yang ada (
        admin,
        employee,
        suplier
    ) 
    
    dalam bentuk dictionary. Contoh datanya : 
    
    {
        username : ClassObject()
    }
    '''
    
    @staticmethod
    def loadFile(path:str) -> dict[str:str] :
        '''static method buat load file dari path yang dikasih
        nanti path nya itu berupa absolute path biar gak error'''
        data = None
        try :
            with open(path, "r", encoding="utf-8") as files:
                data = json.load(files)
                return data
            
        except Exception as e:
            print("Error saat membaca file! harap perisa path nya! " + e)
            return {}
        
        
    @staticmethod
    def convertToClass(listData:dict[str:dict]) -> dict[str:object] : 
        data = {}
        
        for username, userData in listData.items() : 
            role = userData.get("role").lower()
            if role == "admin":
                data[username] = Admin_schema.Admin(username=username, **userData)
            if role == "employee":
                data[username] = Employees_schema.Employee(username=username, **userData)
            if role == "supplier":
                data[username] = Suppliers_schema.Supplier(username=username, **userData)
            
        
        return data
    
    
    def __init__(self, path:str):
        '''
        pas class di inisiasi data dari json otomatis diubah jadi objek class
        '''
        data = self.loadFile(path)
        self.items = self.convertToClass(data)
        
    
    def findUser(self, username:str) -> object : 
        return self.items.get(username)
    
    def addData(self, dataUser:dict[str:str]) : 
        '''
        fungsi buat nambah data ke json. Format dict yang di parameter itu : 
        {
            name : nama,
            username : username,
            email : email,
            password : password,
            role : role
        }
        
        penentuan role bedasarkan key role dari parameter yg dikasih
        '''
        
        newUsers:object = None
        role:str = dataUser.get("role").lower()
        
        if role == "admin" :
            newUsers:Admin_schema.Admin = Admin_schema.Admin(**dataUser)
            
            self.items.update({dataUser.get("username") : newUsers})
        
        elif role == "employee" : 
            newUsers:Employees_schema.Employee = Employees_schema.Employee(**dataUser)
            
            self.items.update({dataUser.get("username") : newUsers})
            
        elif role == "supplier" : 
            newUsers:Suppliers_schema.Supplier = Suppliers_schema.Supplier(**dataUser)
            
            self.items.update({dataUser.get("username") : newUsers})
        
        

