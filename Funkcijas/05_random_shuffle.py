# Funkcija: random.shuffle(lst)
# Sajaukt sarakstu nejaušā kārtībā (izmaina oriģinālo sarakstu)

import random

def demo():
    print("=== random.shuffle(lst) ===")
    print("Sajaukt saraksta elementus nejaušā kārtībā (maina pašu sarakstu)\n")

    # Vienkāršs piemērs
    deck = list(range(1, 11))
    print("Pirms sajaušanas:", deck)
    random.shuffle(deck)
    print("Pēc sajaušanas: ", deck)

    # Pielietojums: kārtis
    print("\nPiemērs: kāršu sajaukšana")
    suits = ["♠", "♥", "♦", "♣"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    full_deck = [v + s for s in suits for v in values]
    random.shuffle(full_deck)
    print("  Pirmās 5 kārtis pēc sajaušanas:", full_deck[:5])

if __name__ == "__main__":
    demo()
