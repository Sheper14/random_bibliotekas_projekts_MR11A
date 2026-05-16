# random.gauss(mu, sigma)
# Ģenerē skaitļus pēc zvana formas sadalījuma
# mu ir vidējā vērtība, sigma ir cik tālu skaitļi drīkst noiet no vidējā

import random

def demo():
    print("=== random.gauss(mu, sigma) ===")
    print("Lielākā daļa skaitļu sanāk tuvu vidējam, reti kāds ļoti tālu\n")

    mu = 170
    sigma = 10

    print(f"Simulēts cilvēku augums, vidējais {mu} cm, novirze {sigma} cm")
    heights = [random.gauss(mu, sigma) for _ in range(10)]
    for i, h in enumerate(heights, 1):
        print(f"  Cilvēks {i:2d}: {h:.1f} cm")

    avg = sum(heights) / len(heights)
    print(f"\nIzlases vidējais: {avg:.1f} cm, teorētiskais: {mu} cm")

if __name__ == "__main__":
    demo()