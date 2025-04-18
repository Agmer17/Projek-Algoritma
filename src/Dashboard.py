from src.Schema.Admin_schema import Admin
from src.Schema.Employees_schema import Employee
from src.Schema.Suppliers_schema import Supplier

#controller 
from src.Controller.Admin_controller import *


def adminDashboard(admin:Admin, dataUser:PersonManager) :
    while True : 
        print(f"Halo admin {admin.name}")
        print(f"{admin.name} mau ngapain? \n1.lihat data karyawan\n2.lihat data supplier\n 3.Edit data user\n6.keluar")
        adminChoice = input("Masukan pilihan > ")
        
        match adminChoice : 
            case "1" :
                showEmployee(dataUser)
            case "2" :
                showSupllier(dataUser)
            case "3" :
                changeData(dataUser)
            case "6" :
                break


def mainMenu(currentUser: Admin | Employee | Supplier, dataUser:PersonManager) -> None:
    '''
    Menampilkan menu utama berdasarkan tipe pengguna yang sedang login.

    Parameter:
    ----------
    currentUser : Admin | Employee | Supplier
        Objek pengguna yang sedang login. Harus berupa instance dari salah satu
        class schema yang merupakan turunan dari Person, yaitu Admin, Employee, atau Supplier.

    Proses:
    -------
    - Mengecek tipe objek currentUser menggunakan isinstance().
    - Menampilkan Menu yang sesuai dengan tipe pengguna.
    - Menu yang ditampilkan bisa dikembangkan lebih lanjut berdasarkan tipe user.
    '''
    #todo bikin menu buat tiap user, trs panggil fungsi nya dari controller 
    if isinstance(currentUser, Admin):
        adminDashboard(currentUser,dataUser)
    elif isinstance(currentUser, Employee): 
        print("Kamu login sebagai karyawan!")
    elif isinstance(currentUser, Supplier):
        print("Kamu login sebagai supplier!")

