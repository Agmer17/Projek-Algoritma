from src.auth import Auth_schema

class Admin(Auth_schema.Person) :
    def __init__(self, nama, username, email, password, role):
        super().__init__(nama, username, email, password, role)
    
    #SETTER UNTUK DATA PERSON (BUAT UBAH DATA EMAIL, PW, NAMA DLL, TAPI 
    # GABISA UBAH ROLE)
    
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