# Funkcija: random.randint(a, b)
# Atgriež nejaušu veselu skaitli diapazonā [a, b]

import random

def demo():
    print("=== random.randint(a, b) ===")
    print("Ģenerē nejaušu veselu skaitli diapazonā [a, b]\n")

    # Vienkāršs piemērs
    print("Kauliņa mešana (1-6), 5 reizes:")
    for i in range(5):
        roll = random.randint(1, 6)
        print(f"  Mešana {i+1}: {roll}")

    #Pielietojums - loterija
    print("\nPiemērs: loterija (izvēlies 6 skaitļus no 1-49)")
    lottery = [random.randint(1, 49) for _ in range(6)]
    print(f"  Izlozētie skaitļi: {sorted(lottery)}")

if __name__ == "__main__":
    demo()
