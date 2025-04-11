from src.admin.Admin_schema import Admin
from src.employees.Employees_schema import Employee
from src.suppliers.Suppliers_schema import Supplier

def mainMenu(currentUser: Admin | Employee | Supplier) -> None:
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
    - Menampilkan pesan sambutan yang sesuai dengan tipe pengguna.
    - Menu yang ditampilkan bisa dikembangkan lebih lanjut berdasarkan tipe user.
    '''
    if isinstance(currentUser, Admin):
        print("Kamu login sebagai admin!")
    elif isinstance(currentUser, Employee): 
        print("Kamu login sebagai karyawan!")
    elif isinstance(currentUser, Supplier):
        print("Kamu login sebagai supplier!")
