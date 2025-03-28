class Person : 
    '''
    Class person tuh buat nampung data akun, soalnya dari 3 role 
    admin, karyawan dan suplier itu mereka punya kesamaan data dan method
    . Nanti pas di schema nya tinggal inherit aja ya, trs tambahin 
    method / data lain yg diperluin.
    
    nanti nyimpen data user di json nya pake nested dict => 
    {
        username : {
            email : Account.email,
            password : Account.password,
            role : Account.role
        },
    }
    
    cmn gua gatau ide bagus apa engga wkwkwk
    '''
    
    def __init__(self, nama:str, username:str, email:str, password:str, role:str):
        self.name:str = nama
        self.username:str = username
        self.email:str = email
        self.password:str = password
        self.role =role
    
    
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
    
    def getData(self) -> dict[str:str] :
        return {"username" : self.username,
                "nama" : self.name,
                "email" : self.email,
                "role" : self.role
                }

class PersonManager : 
    '''
    ini rencananya buat nampung data user soalnya kan struktur datanya sama
    '''
    def __init__(self):
        pass