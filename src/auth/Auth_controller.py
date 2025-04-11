from . import PersonManager as Manage
from src.Config import dataUser

#todo perbagus auth section

def login(listData:Manage.PersonManager) :
    listUserData = listData
    
    print("===LOGIN===")
    
    userInput = {
        "username" : input("Masukan username : "),
        "password" : input("Masukan password : ")
    }
    
    dataPengguna = listUserData.findUser(userInput.get("username"))
    
    if dataPengguna and dataPengguna.password == userInput.get("password"):
        print("Kamu berhasil login")
        return dataPengguna
        
    else : 
        print("username atau password salah")
        return None

def signIn(listData:Manage.PersonManager) : 
    listUserData = listData
    print("=== Sign In ===")
    
    userInput = {
        "name" : input("Masukan nama : "),
        "username" : input("Masukan username akun : "),
        "email" : input("Masukan Email : "),
        "password" : input("Masukan Password : "),
        "role" : input("Masukan role : ")
    }
    
    listUserData.addData(userInput)

def authSection(listData:Manage.PersonManager) : 
    currentUser = None
    
    while currentUser == None :
        userChoice = None 
        print("Halo! Silahkan Login/Sign in terlebih dahulu")
        print("1. Login\n2.Sign-in")
        try :
            userChoice = int(input("Masukan pilihan : "))
            if userChoice == 1 : 
                currentUser = login(listData)
                return currentUser
            elif userChoice == 2 : 
                signIn(listData)
                
            else : 
                print("Pilihan tidak ada!")
        except : 
            print("Input tidak valid! Harap masukan angka 1/2")
        
        
        