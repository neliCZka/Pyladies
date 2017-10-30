from piskvorky import vyhodnot, tah, rand_input, tah_obecny,out_none
from itertools import permutations

def piskvorky1d(hrac1_jmeno,hrac1_funkce,hrac2_jmeno,hrac2_funkce):
    herni_pole = '-'*20
    hraci = [hrac1_funkce,hrac2_funkce]
    hraci_jmena = [hrac1_jmeno,hrac2_jmeno]
    symboly=['x','o']
    counter = 0
    while vyhodnot(herni_pole)=='-':
        print(herni_pole)
        aktivni_hrac = hraci[counter%2]
        aktivni_hrac_jmeno = hraci_jmena[counter%2]
        herni_pole=tah(herni_pole,aktivni_hrac(herni_pole),symboly[counter%2])
        counter+=1
    print(herni_pole)
    if vyhodnot(herni_pole) == '!':
        return None
        #print('plichta')
    else:
        return aktivni_hrac_jmeno


#piskvorky1d('hrac1',tah_pocitace,'hrac2',tah_hrace)
#piskvorky1d('hrac1',tah_pocitace,'hrac2',tah_pocitace)

hraci = {'hrac1':rand_input,'hrac2':rand_input,'hrac3':rand_input}


def vsechny_dvojice(hraci):
    klice = hraci.keys()
    permutace = permutations(klice)
    return permutace


def souboje(hraci):
    dvojice = vsechny_dvojice(hraci)
    vysledky = {}
    for par in dvojice:
        prvni_hrac_jmeno = par[0]
        druhy_hrac_jmeno = par[1]
        prvni_hrac_funkce = lambda herni_pole:tah_obecny(herni_pole,hraci[prvni_hrac_jmeno],out_none)
        druhy_hrac_funkce = lambda herni_pole:tah_obecny(herni_pole,hraci[druhy_hrac_jmeno],out_none)
        vyherce = piskvorky1d(prvni_hrac_jmeno, prvni_hrac_funkce, druhy_hrac_jmeno, druhy_hrac_funkce)
        vysledky.setdefault(prvni_hrac_jmeno,{}).update({druhy_hrac_jmeno:vyherce})
    return vysledky

def vypis_vysledky(vysledky):
    sloupce = [*vysledky.keys()]
    radky = sloupce
    print(',',','.join(sloupce))
    for radek in radky:
        vysledky_hrace = vysledky[radek]
        print(radek,end=',')
        for protivnik in sloupce:
            if protivnik == radek:
                print ('x',end=',')
            else:
                vysledek = vysledky_hrace[protivnik]
                if vysledek is None:
                    print('0', end=',')
                elif vysledek == radek:
                    print('1', end=',')
                else:
                    print('-1', end=',')
        print()
#        print(radek,vysledky[radek])

vypis_vysledky(souboje(hraci))
