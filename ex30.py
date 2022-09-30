people = 30
cars = 40
trucks = 15


if cars > people:
    print("Powinniśmy jechać samochodami.")
elif cars< people:
    print("Nie powinniśmy jechać samochodami.")
else:
    print("Nie możemy się zdecydować.")

if trucks > cars:
    print("Jest zbyt dużo ciężarówek.")
elif trucks < cars:
    print("Może powinniśmy wziąć ciężarówki.")
else:
    print("Nadal nie możemy się zdecydować.")

if people > trucks:
    print("W porządku, po prostu weźmiemy ciężarówki.")
else:
    print("Dobra, w takim razie zostajemy w domu.")
