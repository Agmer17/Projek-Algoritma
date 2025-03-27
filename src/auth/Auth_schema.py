class Person : 
    '''
    Class person tuh buat nampung data akun, soalnya dari 3 role 
    admin, karyawan dan suplier itu mereka punya kesamaan data dan method
    . Nanti pas di schema nya tinggal inherit aja ya, trs tambahin 
    method / data lain yg diperluin.
    
    nanti penyimpanan data user di json nya pake nested dict => 
    {
        "id" : {
            
        }
    }
    '''
    jumlah_user = 0 #ini nanti dipake buat generate id PERSON-(waktu akun dibuat)-(jumlah user)
    
    def __init__(self, nama:str, username:str, email:str, password:str, role:str):
        self.name:str = nama
        self.username:str = username
        self.email:str = email
        self.password:str = password
    
    
    #SETTER UNTUK DATA PERSON (BUAT UBAH DATA EMAIL, PW, NAMA DLL, TAPI 
    # GABISA UBAH ROLE)
    
    def changeName(self, newName:str) -> str :
        if self.name != newName :
            self.name = newName
            return f"Berhasil merubah nama menjadi {self.name}"
        
        return f"Nama tidak boleh sama!"
    
    def changeUsername(self, newUsername:str) -> str :
        if self.username != newUsername :
            self.username = newUsername
            return f"Berhasil merubah username menjadi {self.name}"
        
        return f"Username tidak boleh sama!"