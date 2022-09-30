types_of_people = 10
x = f"Istnieje {types_of_people} rodzajów ludzi"

binary = "binarny"
do_not = "nie znają"
y = f"Ci, którzy znają system {binary} i ci, którzy go {do_not}."

print(x)
print(y)

print(f"Powiedziałem: {x}")
print(f"Powiedziałem również: '{y}'")

hilarious = False
joke_evaluation = "Czyżto nie jest przezabawny dowcip?! {}"

print(joke_evaluation.format(hilarious))

w = "To jest lewa strona..."
e = "łancucha znaków z prawą stroną."

print(w + e)
