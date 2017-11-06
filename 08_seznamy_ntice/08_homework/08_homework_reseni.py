domaci_zvirata = ['pes','kocka','kralik','had','morce']
domaci_zvirata2 = ['pes','krava','fretka','andulka','had']

#ukol 1
def filter_delka(seznam):
    filtrovane_pole = []
    for jmeno in seznam:
        if len(jmeno)<5:
            filtrovane_pole.append(jmeno)
    return filtrovane_pole

#print(filter_delka(domaci_zvirata))

#ukol 2
def filter_zacinajici(seznam):
    filrovane_pole = []
    for jmeno in seznam:
        if jmeno[0] == 'k':
            filrovane_pole.append(jmeno)
    return filrovane_pole
#print(filter_zacinajici(domaci_zvirata))

#ukol 3
def slovo_v_poli(slovo,pole):
    for prvek in pole:
        if prvek == slovo:
            return True
    return False

#ukol 4
def zvirata_v_polich(pole1,pole2):
    v_obou = []
    v_prvnim = []
    v_druhem = []
    for prvek in pole1:
        for prvek2 in pole2:
            if prvek == prvek2:
                v_obou.append(prvek)
        if prvek not in pole2:
            v_prvnim.append(prvek)
    for prvek2 in pole2:
        if prvek2 not in pole1:
            v_druhem.append(prvek2)
    return v_obou,v_prvnim,v_druhem

#ukol 5
def serad(pole):
    nove_pole = list(pole)
    nove_pole.sort()
    return nove_pole

#ukol 6
def serad_bez_prvniho(pole):
    pole_dvojic = []
    serazene_pole = []
    for prvek in pole:
        pole_dvojic.append((prvek[1:],prvek))
    pole_dvojic.sort()
    for dvojice in pole_dvojic:
        serazene_pole.append(dvojice[1])
    return serazene_pole
print(serad_bez_prvniho(domaci_zvirata))

#ukol 9
def obrat_verse(pole):
    pole_versu = list(pole)
    pole_versu.reverse()
    return pole_versu

def nacti_ze_souboru(jmeno):
    soubor = open(jmeno,encoding='utf-8')
    pole_versu = []
    for radek in soubor:
        pole_versu.append(radek)
    return pole_versu

#ukol 10
def obrat_poradi_slov(retezec):
    pole = retezec.split()
    pole.reverse()
    return ' '.join(pole)

#ukol11
#asi zkusit split?
def obrat_sloky(pole_radku):
    indexy_radku = [0]
    pole_slok = []
    for i,radek in enumerate(pole_radku):
        if radek == '':
            indexy_radku.append(i+1)
    indexy_radku.append(len(pole_radku)+1)
    for i in range(len(indexy_radku)-1):
        od = indexy_radku[i]
        do = indexy_radku[i+1]-1
        sloka = pole_radku[od:do]
        pole_slok.append(sloka)
    pole_slok.reverse()
    nove_pole = []
    for sloka in pole_slok:
        for vers in sloka:
            nove_pole.append(vers)
        nove_pole.append('')
    return nove_pole[0:-1]

