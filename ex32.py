the_count = [1, 2, 3, 4, 5]
fruits = ['jabłka', 'pomarańcze', 'gruszki', 'morele']
change = [1, 'jednogroszówki', 2, 'dwugroszówki', 3, 'pięciogroszówki']

# to jest pierwszy rodzaj pętli for, która przechodzi przez listę
for number in the_count:
    print(f"To jest liczba {number}")

#to samo co wyżej
for i in fruits:
    print(f"Rodzaj owocu: {i}")

#możemy również przechodzić przez listy mieszane
#zwróć uwagę, że musimy użyć {} ponieważ nie wiemy co w niej jest
for j in change:
    print(f"Mam {j}")

#możemy również budować listy; zaczniemy od pustej:
elements = []

#następnie używamy funkcji range, aby odliczyć od 0 do 5
for n in range(0,6):
    print(f"Dodajemy {n} do tej listy.")
    #append jest funkcją, którą listy rozumieją
    elements.append(n)

#teraz możemy je również wydrukować
for n in elements:
    print(f"Tym elementem było: {n}")
