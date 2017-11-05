import random

#ukoly na hru HAD -> ukol 13 - 19


def mapa(souradnice,ovoce,velikost_pole):
    rows = velikost_pole[0]
    cols = velikost_pole[1]
    for radek in range(rows):
        for sloupec in range(cols):
            xy = (radek,sloupec)
            if xy in souradnice:
                print('x',end="")
            elif xy == ovoce:
                print('?',end="")
            else:
                print('.',end="")
        print()


def pohyb(souradnice,smer,velikost_pole):
    posledni_souradnice = souradnice[-1]
    vert = posledni_souradnice[0]
    horizont = posledni_souradnice[1]
    if smer == 'v':
        horizont+=1
    elif smer == 's':
        vert-=1
    elif smer == 'z':
        horizont-=1
    elif smer == 'j':
        vert+=1
    if (vert,horizont) in souradnice or vert > velikost_pole[0] or horizont > velikost_pole[1]\
            or vert < 0 or horizont < 0:
        raise ValueError('Hra skoncila')
    souradnice.append((vert,horizont))
    return souradnice


def pohyb_hada(souradnice, ovoce, smer, velikost_pole):
    nove_souradnice_hada = pohyb(souradnice, smer, velikost_pole)
    if ovoce in nove_souradnice_hada:
        return True, nove_souradnice_hada
    else:
        return False, nove_souradnice_hada[1:]


def vygeneruj_ovoce(souradnice, velikost_pole):
    for r in range(0,velikost_pole[0]):
        random_row = random.randint(0,velikost_pole[0])
        for s in range(0,velikost_pole[1]):
            random_col = random.randint(0,velikost_pole[0])
            pozice = (random_row,random_col)
            if pozice in souradnice:
                continue
            else:
                return pozice


### kod samotne hry ###

def hra():
    velikost_pole = (10, 20)
    souradnice = [(0,0)]
    ovoce = (2,3)
    pocitadlo_nesezrano = 0
    try:
        while True:
            mapa(souradnice, ovoce, velikost_pole)
            strana = input('zadej stranu ')
            sezrano, souradnice = pohyb_hada(souradnice, ovoce, strana, velikost_pole)
            if sezrano or pocitadlo_nesezrano == 10:
                ovoce = vygeneruj_ovoce(souradnice,velikost_pole)
                pocitadlo_nesezrano = 0
            pocitadlo_nesezrano = pocitadlo_nesezrano+1
            print(souradnice)
            print(ovoce)
    except(ValueError):
        print('Hra skoncila')

hra()
