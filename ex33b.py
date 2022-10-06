i = 0
numbers = []

for i in range(0, 6):
    print(f"Na górze i ma wartość {i}")
    numbers.append(i)

    #tego kodu chyba nie potrzeba
    #i = i + 1
    print("Aktualne liczby: ", numbers)
    print(f"Na dole i ma wartość {i}")

    print("Te liczby to: ")

    for num in numbers:
        print(num)
