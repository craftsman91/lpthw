from sys import argv

script, filename = argv

print(f"Wymażemy {filename}.")
print("Jeśli tego nie chcesz, wciśnij CTRL+C (^C).")
print("Jeśli tego chcesz, wciśnij RETURN.")

input("?")

print("Otwieranie pliku...")
target = open(filename, 'w')

print("Wykasowanie plik. Do widzenia!")
target.truncate()

print("Teraz poproszę Cię o wpisanie trzech linii tekstu.")

line1 = input("linia 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Zapiszę je w pliku.")

# the newer string formatting used in Python 3 and also available from Python 2.6
target.write("{0}\n{1}\n{2}\n".format(line1,line2,line3))

print("A na koniec zamykamy plik.")
target.close()
