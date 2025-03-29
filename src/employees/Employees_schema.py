from src.auth import Auth_schema

class Employee(Auth_schema.Person) :
    def __init__(self, name, username, email, password, role):
        super().__init__(name, username, email, password, role)