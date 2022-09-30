from  sys import argv

script, first, second, third = argv


print("Ten skrypt nazywa się:", script)
print("Pierwsza zmienna nazywa się:", first)
print("Druga zmienna to:", second)
print("Trzecia zmienna to:", third)

fourth = input("Podaj jeszcze kolejny argument")
print(f"Kolejna zmienna {fourth}")
