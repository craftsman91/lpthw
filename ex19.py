def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"Masz {cheese_count} kawałków sera!")
    print(f"Masz {boxes_of_crackers} paczek krakersów!")
    print(f"Stary, to wystarczy, żeby zrobić imprezę!")
    print("Zorganizuj sobie koc.\n")

print("Możemy po prostu bezpośrednio podać funkcji liczby:")
cheese_and_crackers(20, 30)

print("Albo możemy użyć zmiennych ze skryptu:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("Możemy również wykonać wewnątrz operacje artymetyczne:")
cheese_and_crackers(10 + 20, 5 + 6)

print("I możemy połączyć te dwie rzeczy, czyli zmienne i operacje artymetyczne:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

input("Podaj ilość sera i krakersów: [ENTER]")
krakersy = input("Ilość krakersów:")
ser = input("Ilość sera:")
cheese_and_crackers(krakersy, ser)
