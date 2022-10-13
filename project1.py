# prosty projekt do ćwiczenia z funkcjami i gałęziami
from sys import exit 

def good():
    print("Wygrywasz życie!")
    exit(0)

def bad():
    print("Umierasz!")
    exit(0)

def neutral():
    print("Nic nie zdobyłeś, ale żyjesz.")


def option_a():
    #przydałoby się zaimplementować pętlę while w celu utrwalenia jej działania
    print("Znajdujesz się w ciemnym pomieszczeniu, ledwo co widzisz. Dostrzegasz tylko dziwną książkę.")

    choice = input("co robisz?: uciekam | zabieram książkę | nic nie robię")
    
    if choice == "uciekam":
        #to będzie zakończenie pozytywne
        print("Unikasz śmiercionośnej pułapki.")
        good()

    elif choice == "zabieram książkę":
        print("Wpadasz w pułapkę.")
        bad()
    
    else:
        dead("")
    

def option_b():
    print("Znajdujesz się w podejrzanym miejscu. Widzisz dziwne pudełko. Co robisz?")

    choice = input("co robisz? zabieram pudełko | wychodzę | zostaję")

    if choice == "zabieram pudełko":
        print("Udaje Ci się wydostać, ale w pudełku nic nie było.")
        neutral()

    elif choice == "wychodzę":
        print("Wychodząc potykasz się o prógi upadasz.")
        bad()
    
    else:
        dead("Po godzinie drzwi się zamykają i już nie możesz wyjść.")

def start_point():
    print("Tutaj startujesz i masz trzy opcie wyboru: ")
    
    choice = input("wybierz: opcja A, opcja B lub opcja C \n >")
    
    if choice == "opcja A":
        print("Wchodzisz do ciemnego pomieszczenia.")
        option_a()
    
    elif choice == "Wchodzisz do podejrzanego pomieszczenia.":
        print("Idę do ")
        option_b()
    
    else:
        dead("Stagnacja nie pomaga.")



def dead(why):
    print(why, "Przegrałeś!")
    exit(0)

start_point()