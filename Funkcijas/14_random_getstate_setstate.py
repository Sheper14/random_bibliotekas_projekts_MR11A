# random.getstate() un random.setstate(state)
# Saglabā ģeneratora stāvokli un vēlāk var to atjaunot
# Tad ģenerators turpina no tā paša punkta un dod vienādus skaitļus

import random

def demo():
    print("=== random.getstate() un random.setstate(state) ===")
    print("Saglabā ģeneratora punktu un var atgriezties pie tā\n")

    random.seed(99)
    state = random.getstate()

    first_run = [random.randint(1, 50) for _ in range(5)]
    print("Pirmā sērija pēc saglabāšanas:", first_run)

    random.randint(1, 1000)
    random.randint(1, 1000)

    random.setstate(state)
    second_run = [random.randint(1, 50) for _ in range(5)]
    print("Pēc setstate, sanāk vienādi:", second_run)

    print("\nAbi rezultāti ir vienādi:", first_run == second_run)

if __name__ == "__main__":
    demo()