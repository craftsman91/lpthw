cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("Dostępnych jest", cars, "samochodów")
print("Dostępnych jest tylko", drivers, "kierowców")
print("Dziś będzie", cars_not_driven, "pustych samochodów")
print("Dziś możemy przetransportować", carpool_capacity, "osób")
print("Mamy dziś do przewiezienia", passengers, "pasażerów")
print("Musimy umieścić średnio", average_passengers_per_car, "osoby w każdym samochodzie")
