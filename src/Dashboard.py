from src.admin.Admin_schema import Admin
from src.employees.Employees_schema import Employee
from src.suppliers.Suppliers_schema import Supplier


def mainMenu(currentUser: Admin | Employee | Supplier) -> None:
    
    if isinstance(currentUser, Admin) :
        print("Kamu login sebagai admin!")
    elif isinstance(currentUser, Employee) : 
        print("Kamu login sebagai karyawan!")
    elif isinstance(currentUser, Supplier) :
        print("Kamu login sebagai supplier!")