# random.getrandbits(k)
# Ģenerē nejaušu skaitli ar norādītu bitu skaitu
# Jo vairāk bitu, jo lielāks iespējamais skaitlis

import random

def demo():
    print("=== random.getrandbits(k) ===")
    print("Ģenerē nejaušu skaitli ar norādītu bitu skaitu\n")

    print("1 bits, sanāk vai nu 0 vai 1:", random.getrandbits(1))
    print("8 biti, skaitlis no 0 līdz 255:", random.getrandbits(8))
    print("32 biti:", random.getrandbits(32))

    print("\nPiemērs ar sesijas ID, kāds tiek lietots mājaslapās")
    session_id = hex(random.getrandbits(128))
    print(f"  Sesijas ID: {session_id}")

    val = random.getrandbits(8)
    print(f"\n8 bitu skaitlis decimālā: {val}, bināri: {bin(val)}")

if __name__ == "__main__":
    demo()