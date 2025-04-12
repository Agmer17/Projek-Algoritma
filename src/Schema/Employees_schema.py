from .UserSchema import Person

class Employee(Person) :
    def __init__(self, name, username, email, password, role):
        super().__init__(name, username, email, password, role)