# random.uniform(a, b)
# Tāpat kā random() bet vari pats norādīt no kura līdz kuram skaitlim

import random

def demo():
    print("=== random.uniform(a, b) ===")
    print("Ģenerē nejaušu decimālskaitli norādītajā diapazonā\n")

    print("5 nejaušas temperatūras no 15 līdz 35 grādiem")
    for i in range(5):
        temp = random.uniform(15.0, 35.0)
        print(f"  {i+1}. {temp:.2f} C")

    print("\nPiemērs ar cenu")
    price = random.uniform(0.99, 9.99)
    print(f"  Nejauša cena: {price:.2f} eiro")

if __name__ == "__main__":
    demo()