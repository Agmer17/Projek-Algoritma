from . import PersonManager as Manage
from src.Config import dataUser

def login() :
    listUserData = Manage.PersonManager(dataUser)
    
    print("===LOGIN===")
    
    userInput = {
        "username" : input("Masukan username : "),
        "password" : input("Masukan password : ")
    }
    
    dataPengguna = listUserData.findUser(userInput.get("username"))
    
    if dataPengguna and dataPengguna.password == userInput.get("password"):
        print("Kamu berhasil login")
        return True
        
    else : 
        print("username atau password salah")

def signIn() : 
    listUserData = Manage.PersonManager(dataUser)
    print("=== Sign In ===")
    
    userInput = {
        "name" : input("Masukan nama : "),
        "username" : input("Masukan username akun : "),
        "email" : input("Masukan Email : "),
        "password" : input("Masukan Password : "),
        "role" : input("Masukan role : ")
    }
    
    listUserData.addData(userInput)

def authSection() : 
    isLoggedIn = False
    
    while not isLoggedIn :
        userChoice = None 
        print("Halo! Silahkan Login/Sign in terlebih dahulu")
        print("1. Login\n2.Sign-in")
        userChoice = int(input("Masukan pilihan : "))
        
        try : 
            if userChoice == 1 : 
                isLoggedIn = login()
                
            elif userChoice == 2 : 
                signIn()
                
            else : 
                print("Pilihan tidak ada!")
        except : 
            print("Input tidak valid! Harap masukan angka 1/2")
        
        
        