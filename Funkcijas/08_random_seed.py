# random.seed(a)
# Nosaka no kurienes ģenerators sāk skaitīt
# Ja lieto vienu un to pašu seed, vienmēr sanāk vienādi skaitļi

import random

def demo():
    print("=== random.seed(a) ===")
    print("Ar vienu seed vērtību vienmēr sanāk vienāds rezultāts\n")

    print("Bez seed, katru reizi cits rezultāts")
    print("  1. reize:", [random.randint(1, 100) for _ in range(3)])
    print("  2. reize:", [random.randint(1, 100) for _ in range(3)])

    print("\nAr seed 42, vienmēr vienāds")
    random.seed(42)
    print("  1. reize:", [random.randint(1, 100) for _ in range(3)])
    random.seed(42)
    print("  2. reize:", [random.randint(1, 100) for _ in range(3)])

    print("\nSeed noderīgs testēšanā, lai rezultātus varētu atkārtot")

if __name__ == "__main__":
    demo()