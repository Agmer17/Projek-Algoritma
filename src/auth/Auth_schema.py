import time
import json
from src.admin import Admin_schema

class Person : 
    '''
    Class person tuh buat nampung data akun, soalnya dari 3 role 
    admin, karyawan dan suplier itu mereka punya kesamaan data dan method
    . Nanti pas di schema nya tinggal inherit aja ya, trs tambahin 
    method / data lain yg diperluin.
    
    nanti nyimpen data user di json nya pake nested dict => 
    {
        username : {
            nama : nama,
            email : Account.email,
            password : Account.password,
            role : Account.role
        },
    }
    
    cmn gua gatau ide bagus apa engga wkwkwk
    '''
    
    def __init__(self, nama:str, username:str, email:str, password:str, role:str):
        self.id = f"USER-{int(time.time()*1000)}"
        self.name:str = nama
        self.username:str = username
        self.email:str = email
        self.password:str = password
        self.role =role

    def _changeAtrribute(self, attributeName:str, newValue:str) -> bool :
        #isSameData tuh dia ngecek apakah value yg dimasukin sama
        #kayak data lama? kalo iya value nya gajadi diganti
        isNotSameData = (getattr(self, attributeName) != newValue)
        
        if isNotSameData: 
            setattr(self, attributeName, newValue)
            print(f"{attributeName} berhasil diubah!")
            return True
        
        print(f"{attributeName} tidak boleh sama!")
        return False
    
    def changeName(self, newName:str) :
        return self._changeAtrribute("name", newName)
        
    def changeUsername(self, newUsername:str) :
        return self._changeAtrribute("username", newUsername)
        
    def changePassword(self, newPassword:str) :
        return self._changeAtrribute("password", newPassword)
        
    def changeEmail(self, newEmail:str) :
        return self._changeAtrribute("email", newEmail)
    
    def getData(self) -> dict[str:str] :
        return {"username" : self.username,
                "nama" : self.name,
                "email" : self.email,
                "role" : self.role
                }

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
    def convertToClass(listData) : 
        data = {}
        
        for username, userData in listData.items() : 
            role = userData.get("role")
            if role == "admin":
                data[username] = Admin_schema.Admin(username=username, **userData)
            else : 
                data[username] = Person(username=username, **userData)
        
        return data
    
    
    def __init__(self, path:str):
        '''
        pas class di inisiasi data dari json otomatis diubah jadi objek class
        '''
        data = self.loadFile(path)
        self.items = self.convertToClass(data)
        
    
    
            
    

