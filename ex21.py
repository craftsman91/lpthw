def add(a, b):
    print(f"Dodawanie {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Odejmowanie {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Mnożenie {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dzielenie {a} / {b}")
    return a / b

print("Wykonajmy kilka operacji arytmetycznych jedynie za pomocą fukcji")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Wiek: {age}, wzrost: {height}, waga: {weight}, IQ: {iq}")
