## Animal jest obiektem 
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person (osoba) ma pet (jakiegoś zwierzaka)
        self.pet = None

## ?? 
class Employee(Person):

    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover jest Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan 

## ?? Ustaw frank na instancję klasy Employee 
frank = Employee("Frank", 120000)

## ?? Z frank weź atrybut pet i ustaw go na rover
frank.pet = rover

## ?? Ustaw flipper na instancję klasy Fish
flipper = Fish()

## ?? Ustaw crouse na instancję klasy Salmon
crouse = Salmon()

## ?? Ustaw harry na instancję klasy Halibut
harry = Halibut()

