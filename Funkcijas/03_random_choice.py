# Funkcija: random.choice(seq)
# Atgriež nejaušu elementu no virknes vai saraksta

import random

def demo():
    print("=== random.choice(seq) ===")
    print("Izvēlas nejaušu elementu no saraksta\n")

    # Piemērs ar vārdiem
    names = ["Anna", "Jānis", "Marta", "Kārlis", "Ilze"]
    print("Saraksts:", names)
    print("Nejauši izvēlētais vārds:", random.choice(names))

    # PPielietojums: izvēle no variāntiem
    print("\nPiemērs: nejauša pusdienu izvēle")
    lunch_options = ["pica", "salāti", "zupa", "sviestmaize", "pasta"]
    print(f"  Šodien ēdīsi: {random.choice(lunch_options)}")

    # Izvēle no virknes (string)
    print("\nNejauša burta izvēle no 'Python':", random.choice("Python"))

if __name__ == "__main__":
    demo()
