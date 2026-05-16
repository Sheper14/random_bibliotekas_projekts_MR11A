# random.expovariate(lambd)
# Ģenerē skaitļus kur mazākas vērtības sanāk biežāk nekā lielās
# lambd norāda cik bieži notikums notiek, vidējais intervāls ir 1 dalīts ar lambd

import random

def demo():
    print("=== random.expovariate(lambd) ===")
    print("Bieži lieto lai simulētu gaidīšanas laikus\n")

    lambd = 0.5
    print(f"Klientu gaidīšanas laika simulācija, vidēji {1/lambd:.0f} minūtes starp klientiem")

    waits = [random.expovariate(lambd) for _ in range(8)]
    total = 0
    for i, wait in enumerate(waits, 1):
        total += wait
        print(f"  Klients {i}: {wait:.2f} minūtes gaidīšana")

    print(f"\nVidējais gaidīšanas laiks: {total/len(waits):.2f} minūtes")
    print(f"Teorētiskais vidējais: {1/lambd:.2f} minūtes")

if __name__ == "__main__":
    demo()