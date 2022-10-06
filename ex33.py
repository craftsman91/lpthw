i = 0
numbers = []

while  i < 6:
    print(f"Na górze i ma wartość {i}")
    numbers.append(i)

    i = i + 1
    print("Aktualne liczby: ", numbers)
    print(f"Na dole i ma wartość {i}")

    print("Te liczby to: ")

    for num in numbers:
        print(num)
