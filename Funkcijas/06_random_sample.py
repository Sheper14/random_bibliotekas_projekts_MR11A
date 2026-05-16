# random.sample(population, k)
# Izvēlas k unikālus elementus no saraksta, neviens neatkārtojas

import random

def demo():
    print("=== random.sample(population, k) ===")
    print("Izvēlas k unikālus elementus, bez atkārtošanas\n")

    numbers = list(range(1, 21))
    print("Avota saraksts:", numbers)
    print("sample (bez atkārtošanas):", random.sample(numbers, 5))
    print("choices (ar atkārtošanos):", random.choices(numbers, k=5))

    print("\nPiemērs ar skolēniem")
    students = ["Anna", "Janis", "Marta", "Karlis", "Ilze",
                "Peteris", "Laura", "Andrejs", "Zane", "Toms"]
    selected = random.sample(students, 5)
    print("Izveletie skoleni:", selected)

if __name__ == "__main__":
    demo()