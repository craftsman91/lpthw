name = 'Zed A. Shaw'
age = 35 #nie kłamię
height = 190 #centymetrów
height_inch = round(height * 0.39)
weight = 80 #kg
weight_lb = round(weight * 2.2)
eyes = 'niebieskie'
teeth = 'białe'
hair = 'brązowe'


print(f"Porozmawiajmy o {name}.")
print(f"Ma {height} centymetrów wzrostu.")
print(f"Ma {height_inch} cali wzrostu")
print(f"Waży {weight} kilogramów.")
print(f"Waży {weight_lb} funtów.")
print("Tak na prawdę nie waży dużo")
print(f"Ma {eyes} oczy i {hair} włosy.")
print(f"Jego zęby są zazwyczaj {teeth}, w zależności od ilości wypitej kawy.")

#ta linia jest trudna
total = age + weight + height
print(f"Jeśli dodam {age}, {height} i {weight}, otrzymam {total}.")
