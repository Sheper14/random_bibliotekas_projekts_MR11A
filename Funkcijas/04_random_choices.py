# Funkcija: random.choices(population, weights=None, k=1)
# Izvēlas k elementus no saraksta AR atkārtošanos; var norādīt svērtās vērtības

import random

def demo():
    print("=== random.choices(population, weights, k) ===")
    print("Izvēlas vairākus elementus AR atkārtošanos, var izmantot svērtās vērtības\n")

    # Vienkāršs piemērs
    colors = ["sarkans", "zils", "zaļš", "dzeltens"]
    picked = random.choices(colors, k=5)
    print("5 nejauši krāsas (ar atkārtošanos):", picked)

    # Piemērs ar svērtām vērtībām (weights): dažas izvēles ir ticamākas
    print("\nPiemērs ar svērtām vērtībām (sarkans 5x biežāk):")
    weights = [50, 10, 10, 10]
    results = random.choices(colors, weights=weights, k=20)
    for color in colors:
        print(f"  {color}: {results.count(color)} reizes no 20")

if __name__ == "__main__":
    demo()
