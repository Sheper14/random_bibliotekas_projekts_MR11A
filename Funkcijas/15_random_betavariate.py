# random.betavariate(alpha, beta)
# Ģenerē skaitļus no 0 līdz 1, bet var kontrolēt kur tie biežāk krīt
# Ja alpha lielāks par beta, skaitļi biežāk tuvāk 1niekam, un otrādi

import random

def demo():
    print("=== random.betavariate(alpha, beta) ===")
    print("Ģenerē skaitļus no 0 līdz 1, alpha un beta ietekmē kur tie biežāk sanāk\n")

    print("alpha 2, beta 5, skaitļi biežāk tuvu 0, zemi rezultāti")
    low_scores = [random.betavariate(2, 5) * 100 for _ in range(5)]
    for s in low_scores:
        print(f"  {s:.1f}%")

    print("\nalpha 5, beta 2, skaitļi biežāk tuvāk 1niekam, augsti rezultāti")
    high_scores = [random.betavariate(5, 2) * 100 for _ in range(5)]
    for s in high_scores:
        print(f"  {s:.1f}%")

    print("\nalpha 1, beta 1, vienmērīgi sadalīts tāpat kā random.random()")
    uniform_scores = [random.betavariate(1, 1) * 100 for _ in range(5)]
    for s in uniform_scores:
        print(f"  {s:.1f}%")

if __name__ == "__main__":
    demo()