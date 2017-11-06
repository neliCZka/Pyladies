# 05 - RAZENI SEZNAMU

# Seznam je serazena datova struktura!

plemena_psu = ['labik','husky','ovcak','staffik','jezevcik']
kolik_sezerou_kg_za_mesic = [12,8,10,8,2]

# Seznamy se radi abecedne pokud jde o retezce

# muzeme pouzit funkci sorted(seznam), ktera nam samotny seznam NESERADI, ale jen vrati SERAZENY vystup ('nove' serazene pole)
# tato funkce tedy NEMENI seznam samotny
def vypis_serazeny_seznam(seznam):
    serazene_pole = sorted(seznam)
    print('toto je serazene pole od A, ale nezmenene: {}'.format(serazene_pole))
#vypis_serazeny_seznam(plemena_psu)

# pokud ale chceme seznam zmenit, aby byl uz naporad SERAZENY, muzeme pouzit funkci seznam.sort(), ktera nase stavajici pole seradi

def serad_seznam(seznam):
    seznam.sort()
    print('toto je serazene pole od A, ktere je zmeneme "naporad": {}'.format(seznam))
#serad_seznam(plemena_psu)

# muzeme i zmenit smer razeni, tedy ne A -> Z, ale Z -> A
def serad_seznam_opacne(seznam):
    seznam.sort(reverse=True)
    print('seznam serazeny od Z: {}'.format(seznam))
#serad_seznam_opacne(plemena_psu)
#print('i funkce sorted() umi radit opacne: {}'.format(sorted(plemena_psu,reverse=True)))

# to stejne muzeme udelat i s cisly v seznamu
# UKOL: seradte seznam kolik_sezerou_kg_za_mesic, pouzijte funkci, ktera puvodni seznam ZMENI na serazeny

