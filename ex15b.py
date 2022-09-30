from sys import argv

script, filename = argv

txt = open(filename)

print(f"Oto Twój plik {filename}:")
print(txt.read())
