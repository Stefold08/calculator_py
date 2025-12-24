import math

#creare il menu di base testuale
def menu() :
    print("-------------------")
    print("menu calcolatrince")
    print("1) addizione ")
    print("2) sottrazione")
    print("3) moltiplicazione ")
    print("4) divisione")
    print("5) potenza")
    print("6) radice")
    print("0) esci")
    print("-------------------")

#varie scelte basate sul menu
while True :
    menu()
    scelta = int(input("inserire una opcione:"))

    #funzione per addizione,sottrazione,moltiplicazione,divisione
    if scelta == 1 :
        a = input("inserisci il primo numero:")
        a = int(a)
        b = input("inserisci il secondo numero:")
        b = int(b)
        somma = a + b
        print(f"il risultato e` {somma} ")
    elif scelta == 2 :
        a = input("inserisci il primo numero:")
        a = int(a)
        b = input("inserisci il secondo numero:")
        b = int(b)
        somma = a - b
        print(f"il risultato e` {somma} ")
    elif scelta == 3 :
        a = input("inserisci il primo numero:")
        a = int(a)
        b = input("inserisci il secondo numero:")
        b = int(b)
        somma = a * b
        print(f"il risultato e` {somma} ")
    elif scelta == 4 :
        a = input("inserisci il primo numero:")
        a = int(a)
        b = input("inserisci il secondo numero:")
        b = int(b)
        somma = a / b
        print(f"il risultato e` {somma} ")
    elif scelta == 5 :
        a = input("inserisci il primo numero:")
        a = int(a)
        b = input("inserisci il secondo numero:")
        b = int(b)
        somma = a ** b
        print(f"il risultato e` {somma} ")
    elif scelta == 6 :
        print("scegli quale tipo di radice: ")
        print("1) quadrata ")
        print("2) cubica ")
        scelta1 = int(input("inserire una opcione:"))

        if scelta1 == 1 :
            a = input("inserire il numero da mettere sotto radice:")
            a = int(a)
            somma = math.sqrt(a)
            print(f"il risultato e` {somma} ")
        elif scelta1 == 2 :
            a = input("inserire il numero da mettere sotto radice:")
            a = int(a)
            somma = math.cbrt(a)
            print(f"il risultato e` {somma} ")
        else :
            break
    elif scelta == 0 :
        print("Arrivederci!!")
        break
    else:
        print("opzione non valida!! Riprova.")