from src.Schema.Employees_schema import Employee
from src.Schema.Suppliers_schema import Supplier
from src.Manager.PersonManager import PersonManager


def getDataByRole(dataUser:PersonManager, type:str="employee") -> list[Employee] | list[Supplier] | None :
    
    resultData = []
    if type.lower() == "employee" : 
        for data in dataUser.items.values() :
            if isinstance(data, Employee) :
                resultData.append(data)
        return resultData
    
    elif type.lower() == "supplier" :
        for data in dataUser.items.values() :
            if isinstance(data, Supplier) :
                resultData.append(data)
        return resultData
    
    else : 
        print(f"type {type} tidak ada, hanya tersedia : employee atau supplier")
        return None
    

def showEmployee(dataUser:PersonManager) -> None :
    employeeData = getDataByRole(dataUser)
    
    for data in employeeData : 
        print(data.getData())

def showSupllier(dataUser:PersonManager) -> None :
    supplierData = getDataByRole(dataUser, type="supplier")
    for data in supplierData : 
        print(data.getData())

def changeData(dataUser:PersonManager) : 
    for data in dataUser.items.values() : 
        print(data.getData())
    username = input("Masukin username yang pengen dirubah : ")
    keyToChange = input("data apa nih yang mau diganti? \nsilahkan masukin (nama, username, email, password)\n>")
    dataUser.editUser(username, keyToChange)
    #todo nanti benerin ni fungsi