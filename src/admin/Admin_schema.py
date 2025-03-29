from src.auth import Auth_schema

class Admin(Auth_schema.Person) :
    def __init__(self, nama, username, email, password, role):
        super().__init__(nama, username, email, password, role)
    