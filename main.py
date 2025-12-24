#creare il menu di base testuale
def menu() :
    print("-------------------")
    print("menu calcolatrince")
    print("1) addizione ")
    print("2) sottrazione")
    print("3) moltiplicazione ")
    print("4) divisione")
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
    elif scelta == 0 :
        print("Arrivederci!!")
        break
    else:
        print("opzione non valida!! Riprova.")