# Funkcija: random.random()
# Atgriež nejaušu komata skaitli diapazonā [0.0, 1.0)
# Katra faila dokumentācija/avots ir norādīts README.md failā.

import random

def demo():
    print("=== random.random() ===")
    print("Ģenerē nejaušu komata skaitli diapazonā [0.0, 1.0)\n")

    for i in range(5):
        value = random.random()
        print(f"  Piemērs {i+1}: {value:.6f}")

    # Praktisks pielietojums: simulēt 30% varbūtību
    print("\nPraktisks piemērs: simulēt 30% varbūtību (1000 mēģinājumi)")
    count = sum(1 for _ in range(1000) if random.random() < 0.3)
    print(f"  Notika ~30% gadījumu: {count}/1000 reizes")

if __name__ == "__main__":
    demo()
