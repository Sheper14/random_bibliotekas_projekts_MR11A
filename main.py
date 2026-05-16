import random

def f1():
    print("random.random() - nejauša decimāldaļa no 0 līdz 1")
    print(random.random())

def f2():
    print("random.randint(a, b) - nejauša vesels skaitlis no a līdz b")
    print(random.randint(1, 100))

def f3():
    print("random.choice(seq) - nejauša elementa izvēle no saraksta")
    print(random.choice(["Anna", "Janis", "Marta", "Karlis"]))

def f4():
    print("random.choices(pop, k) - vairāki nejaušie ar atkārtošanos")
    print(random.choices(["sarkans", "zils", "zals"], k=5))

def f5():
    print("random.shuffle(lst) - sajauc sarakstu nejaušā kārtībā")
    lst = [1, 2, 3, 4, 5]
    random.shuffle(lst)
    print(lst)

def f6():
    print("random.sample(pop, k) - unikāli nejaušie bez atkārtošanas")
    print(random.sample(range(1, 50), 6))

def f7():
    print("random.uniform(a, b) - nejauša decimāldaļa norādītajā diapazonā")
    print(random.uniform(5.0, 25.0))

def f8():
    print("random.seed(a) - ar vienu seed vienmēr vienāds rezultāts")
    random.seed(42)
    print(random.randint(1, 100))
    random.seed(42)
    print(random.randint(1, 100))

def f9():
    print("random.randrange(s, e, st) - nejauša no diapazona ar soli")
    print(random.randrange(0, 51, 5))

def f10():
    print("random.gauss(mu, sigma) - zvana formas sadalījums")
    print(round(random.gauss(170, 10), 1), "cm")

def f11():
    print("random.getrandbits(k) - nejauša skaitlis ar norādītu bitu skaitu")
    print(random.getrandbits(8))

def f12():
    print("random.triangular(l, h, m) - mode vērtība sanāk visbiežāk")
    print(round(random.triangular(0, 100, 70), 1))

def f13():
    print("random.expovariate(lambd) - eksponenciālais sadalījums")
    print(round(random.expovariate(0.5), 2), "minūtes")

def f14():
    print("random.getstate un setstate - saglabā un atjauno ģeneratora stāvokli")
    state = random.getstate()
    a = random.randint(1, 100)
    random.setstate(state)
    b = random.randint(1, 100)
    print("Pirmais:", a, "Pēc setstate:", b, "Vienādi:", a == b)

def f15():
    print("random.betavariate(a, b) - skaitļi no 0 līdz 1, alpha un beta nosaka kur biežāk")
    print(round(random.betavariate(5, 2) * 100, 1), "%")

funkcijas = {
    "1": f1, "2": f2, "3": f3, "4": f4, "5": f5,
    "6": f6, "7": f7, "8": f8, "9": f9, "10": f10,
    "11": f11, "12": f12, "13": f13, "14": f14, "15": f15
}

while True:
    print("\nIzvēlies funkciju no 1 līdz 15, vai 0 lai izietu")
    izvele = input("Tavs ievads: ")
    if izvele == "0":
        break
    elif izvele in funkcijas:
        print()
        funkcijas[izvele]()
    else:
        print("Tāda izvēle nav, mēģini vēlreiz")