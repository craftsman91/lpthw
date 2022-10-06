i = 0
numbers = []

def while_loop(i, n):
    j = input("Podaj wartość: ")
    while  i < int(j):
        print(f"Na górze i ma wartość {i}")
        numbers.append(i)

        i = i + n
        print("Aktualne liczby: ", numbers)
        print(f"Na dole i ma wartość {i}")

        print("Te liczby to: ")

        for num in numbers:
            print(num)

while_loop(i, 3)
