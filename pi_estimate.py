from pylab import *
import matplotlib.patches as mpatches
import random
#comment

def estimatePi(n,m):
    insideQ = 0  # punkty w kwadracie
    insideC = 0  # punkty w kole
	
    listQ = []
    listC = []
    axis([0, m, 0, m])
    while insideQ < n:
        x = random.randrange(m)
        y = random.randrange(m)
        plt.plot([x], [y], 'ro') #jak resetowac wykres!??!
        if (x*x + y*y <= m*m): #sprawdzamy czy znajduje sie w kole
            insideC += 1
            listC.append()
        insideQ += 1
    return 4 * insideC/insideQ

def main():
    print("PROGRAM DO WYLICZANIA LICZBY PI\n")
    while(True):
        print("Wybierz co chcesz zrobić:\n")
        print("1. Wyliczyć liczbę pi\n")
        print("2. Zakończyć program\n")
        choice = input()
        if choice == "1":
            check = False
            check2 = False
            while(check == False):
                print ("Podaj liczbe punktow:\n")
                points = input()
                if points.isdigit():
                    n = int(points)
                    if n > 0:
                        check = True

            while(check2 == False):
                print("Podaj zakres losowanych liczb:\n")
                range = input()
                if range.isdigit():
                    m = float(range)
                    check2 = True

            pi = estimatePi(n,m)
            plt.show()
            print("Wyliczona liczba pi: {}\n".format(pi))
            print("Wykres zapisano do pliku")
        #elif choice == 2:
            #zakonczyc dzialanie
        else:
            print("Wybrano nieistniejącą opcję!\n")


if __name__ == "__main__":
    main()
