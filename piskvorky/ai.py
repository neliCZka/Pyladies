from random import randint

def rand_input(herni_pole):
    prazdne_indexy = [idx for idx,i in enumerate(herni_pole) if i == '-']
    return prazdne_indexy[randint(0,len(prazdne_indexy)-1)]

def seq_input(herni_pole):
    volna_pozice = herni_pole.index('-')
    return volna_pozice