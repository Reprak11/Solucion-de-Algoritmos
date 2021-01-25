class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def __repr__(self):
        return f'Mi name is {self.name} and I am {self.age} years old'

p = Person('Pankaj', 34)

print(p)

