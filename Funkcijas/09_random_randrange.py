# random.randrange(start, stop, step)
# Līdzīgi kā randint, bet stop skaitlis netiek iekļauts
# Var arī norādīt soli, piemēram tikai pāra skaitļi

import random

def demo():
    print("=== random.randrange(start, stop, step) ===")
    print("Nejauša skaitļa izvēle no diapazona, stop netiek iekļauts\n")

    print("Skaitļi no 0 līdz 9 (stop ir 10 bet tas netiek iekļauts)")
    print([random.randrange(10) for _ in range(8)])

    print("\nTikai pāra skaitļi no 0 līdz 20, step ir 2")
    print([random.randrange(0, 21, 2) for _ in range(6)])

    print("\nReizinājumi ar 5 no 0 līdz 50, step ir 5")
    print([random.randrange(0, 51, 5) for _ in range(6)])

if __name__ == "__main__":
    demo()