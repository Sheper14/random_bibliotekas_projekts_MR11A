# random.triangular(low, high, mode)
# Ģenerē skaitļus, bet mode vērtība sanāk visbiežāk
# Noderīgi, ja zini ka kaut kas notiek biežāk noteiktā diapazona daļā
import random

def demo():
    print("=== random.triangular(low, high, mode) ===")
    print("Skaitļi sanāk visdažādākie, bet mode vērtība visbiežāk\n")

    low, high, mode = 0, 100, 70
    print(f"Min {low}, max {high}, visbiežāk ap {mode}\n")

    samples = [random.triangular(low, high, mode) for _ in range(12)]
    print("12 ģenerētas vērtības")
    for i, v in enumerate(samples, 1):
        bar = "#" * int(v / 5)
        print(f"  {i:2d}. {v:5.1f} |{bar}")

    avg = sum(samples) / len(samples)
    print(f"\nVidējais: {avg:.1f}, lielākā daļa ir tuvu {mode}")

if __name__ == "__main__":
    demo()