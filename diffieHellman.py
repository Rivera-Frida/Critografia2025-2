import random

def main():
    p = 1009
    g = random.randint(1,10)
    A = int(input("Ingrese su clave  privada A:_"))
    B = int(input("Ingrese su clave  privada B:_"))
    pubA = (g**A)%p
    pubB = (g**B)%p

    print(f"Llave publica A: {pubA}")
    print(f"Llave publica B: {pubB}")

    privA = (pubB**A)%p
    privB = (pubA**B)%p

    print(f"Llave privada de A para B {privA}")
    print(f"Llave privada de B para A {privB}")

main()
