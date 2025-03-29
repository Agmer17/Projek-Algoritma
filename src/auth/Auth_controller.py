from . import Auth_schema as Schema
from src.Config import dataUser

def login() :
    listUserData = Schema.PersonManager(dataUser)
    
    print("===LOGIN===")
    
    userInput = {
        "username" : input("Masukan username : "),
        "password" : input("Masukan password : ")
    }
    
    dataPengguna = listUserData.findUser(userInput.get("username"))
    
    if dataPengguna and dataPengguna.password == userInput.get("password"):
        print("Kamu berhasil login")
        
    else : 
        print("username atau password salah")

def signIn() : 
    pass