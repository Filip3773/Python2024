import math

def euklidsko_rastojanje(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def srednja_tacka(x1, y1, x2, y2):
    srednja_x = (x1 + x2) / 2
    srednja_y = (y1 + y2) / 2
    return srednja_x, srednja_y

def main():
    x1 = float(input("Unesite x koordinatu prve tačke: "))
    y1 = float(input("Unesite y koordinatu prve tačke: "))
    x2 = float(input("Unesite x koordinatu druge tačke: "))
    y2 = float(input("Unesite y koordinatu druge tačke: "))
    
    srednja_x, srednja_y = srednja_tacka(x1, y1, x2, y2)
    print("Srednja tačka je: ({}, {})".format(srednja_x, srednja_y))
    
    x3 = float(input("Unesite x koordinatu tačke susreta: "))
    y3 = float(input("Unesite y koordinatu tačke susreta: "))
    
    rastojanje = euklidsko_rastojanje(x1, y1, x3, y3)
    print("Rastojanje od početne pozicije do tačke susreta je: {:.2f}".format(rastojanje))

if __name__ == "__main__":
    main()
