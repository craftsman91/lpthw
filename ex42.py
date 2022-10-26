## Animal jest obiektem 
class Animal(object):
    pass

## Dog jest Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog ma name
        self.name = name

## Cat jest Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat ma name
        self.name = name

## Person jest object
class Person(object):

    def __init__(self, name):
        ## Person ma name
        self.name = name

        ## Person (osoba) ma pet (jakiegoś zwierzaka)
        self.pet = None

## Employee jest Person 
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee ma name i salary?
        super(Employee, self).__init__(name)
        ## Employee ma salary
        self.salary = salary

## Fish jest object
class Fish(object):
    pass

## Salmon jest Fish
class Salmon(Fish):
    pass

## Halibut jest Fish
class Halibut(Fish):
    pass


## rover jest Dog
rover = Dog("Rover")

## ?? satan jest Cat
satan = Cat("Satan")

## mary jest Person(Mary)
mary = Person("Mary")

## mary ma pet (satan
mary.pet = satan 

## frank jest Employee (Frank, 120000) 
frank = Employee("Frank", 120000)

## frank ma pet (rover)
frank.pet = rover

## flipper jest Fish 
flipper = Fish()

## crouse jest Salmon
crouse = Salmon()

## hary jest Halibut 
harry = Halibut()

