imie = str(input("Imie:"))
płeć = str(input("płeć:"))

if płeć == "kobieta" or płeć == "Kobieta":
    print(f"Spłyń kobieto") 
    exit()
else: 
    print(f"Siemka {imie} idziemy na piwko?")

TakNie = str(input("Tak / Nie?:"))
 
if TakNie == "Tak" or TakNie == "tak" or TakNie == "T" or TakNie == "ta" or TakNie == "TAK" or TakNie == "Taa" or TakNie == "Ta" or TakNie == "TaK" or TakNie == " tak" or TakNie == " Tak" or TakNie == " Ta" or TakNie ==" ta":
    print(f"No i git nawalimy się w pizdu")
else:
    print(f"Trudno podjedzie się następnym razem.")

wiek = int(input("A ile ty masz lat ziomuś:"))

if wiek < 18:
    print(f"Nevermind spłyń dzicioku")
else:
    print(f"No i gitara.")

Piwo = str(input("Czy masz własne piwo?:"))
if Piwo == "Tak" or Piwo == "tak" or Piwo == "T" or Piwo == "ta" or Piwo == "TAK" or Piwo == "Taa" or Piwo == "Ta" or Piwo == "TaK" or Piwo == " tak" or Piwo == " Tak" or Piwo == " Ta" or Piwo == " ta":
    print(f"No i dokurwiście, idziemty kurwa na piwo")
else:
    print(f"Trudno podjedzie się na stację.") 