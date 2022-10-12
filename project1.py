# prosty projekt do ćwiczenia z funkcjami i gałęziami
from sys import exit 

def start_point():
    print("Tutaj startujesz i masz trzy opcie wyboru: ")
    choice = input("wpisz: opcja A, opcja B lub opcja C \n >")
    

    if choice == "opcja A":
        print("Idę do ")
        option_a()
    elif choice == "opcja B":
        print("Idę do ")
        option_b()
    else:
        dead()



def dead():
    print("Przegrałeś!")
    exit(0)

start_point()

#todo
"""
def option_a():
    

def option_b():

def good():
    

def bad():
    
def neutral():

"""
print("Kilka funkcji do zdefiniowania na później")