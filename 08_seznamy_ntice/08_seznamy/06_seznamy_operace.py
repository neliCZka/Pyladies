# 06 - OPERACE NAD SEZNAMY

plemena_psu = ['labik','husky','ovcak','staffik','jezevcik']
kolik_sezerou_kg_za_mesic = [12,8,10,8,2]

# Se seznamy muzeme provadet spoustu operaci, ktere uz zname napriklad od retezcu.
# Muzeme si jim posvitit na delku (pocet zaznamu v listu), muzeme je nasobit, muzeme je prochazet v cyklu, muzeme je i tvorit v cyklu,
# muzeme je rozdelit atd.

def zdvojnasob_seznam(seznam1,seznam2):
    print('v tomto pripade to nedava moc smysl, ale sezamy se daji nasobit stejne jako retezce a navic se daji secist s dalsim seznamem: {}'.format((seznam1*2)+seznam2))
#zdvojnasob_seznam(plemena_psu,kolik_sezerou_kg_za_mesic)

# ta delka se fakt hodi, protoze se podle ni casto muze iterovat treba v cyklu,  takze si ji ukazeme

def dej_mi_delku_seznamu(seznam):
    print('pocet prvku v seznamu je: {}'.format(len(seznam)))
#dej_mi_delku_seznamu(plemena_psu)

def dej_mi_pocet_ovcaku_a_jejich_index(seznam):
    print('pocet ovcaku je: {} a index ovcaka je: {}'.format(seznam.count('ovcak'),seznam.index('ovcak')))
#dej_mi_pocet_ovcaku_a_jejich_index(plemena_psu)

# UKOL: co se stane, kdyz bude vic ovcaku v seznamu? Jaky index nam to vrati a proc? Vyzkousejte, muzete pouzit treba takovy seznam:
plemena = ['ovcak','rotwik','ovcak']

# sikovny operator je i "in" diky kteremu muzeme treba vytvaret podminky:

def pozor_na_jezevciky(seznam):
    if 'jezevcik' in seznam:
        print('pozor na jezevciky, utikaji, pletou se pod nohama a jsou to fakt agresori')
    else:
        print('pohoda, mate tam same hodne pejsky')

#pozor_na_jezevciky(plemena_psu)
#pozor_na_jezevciky(plemena)

# stejne jako pro prevod na retezce funguje funkce str() a pro prevod na cela cisla funkce int(), mame neco podobneho i pro listy

def udelej_mi_z_toho_list(neco_z_ceho_chceme_list):
    novy_list = list(neco_z_ceho_chceme_list)
    print('tady mas ten list: {}'.format(novy_list))

#udelej_mi_z_toho_list('pohodicka')
#udelej_mi_z_toho_list(range(20))
#udelej_mi_z_toho_list(100)

# fuuu, to posledni nejak nevyslo, je to proto, ze list muzeme udelat jen z neceho, pres co muzeme iterovat - z neceho, co muze projit
# for cyklus a rozsekat to na mensi jednotky...u samotneho jednoho cisla to nejde

def rekni_mi_kolik_kterej_sezere():
    kolik_ktery_sezere = []
    for pes in plemena_psu:
        index = plemena_psu.index(pes)
        kolik_ktery_sezere.append(pes+' sezere '+str(kolik_sezerou_kg_za_mesic[index]))  # funkce str() je tu proto, ze v puvodnim seznamu kolik_sezerou_kg_za_mesic jsou cisla, ne retezce a ve vyslednem seznamu tvorim retezec
    print(kolik_ktery_sezere)
#rekni_mi_kolik_kterej_sezere()

# vzhledem k tomu, ze retezce a listy jsou si dost podobne, muzeme se k nim casto chovat podobne
# funkce SPLIT muze rozdelit retezec na slova

def vrat_mi_seznam_slov(retezec):
    return retezec.split()
#print vrat_mi_seznam_slov('Je to asi trosku divny, ale z retezce se proste da udelat seznam znaku celkem jednoduse.')

slova = vrat_mi_seznam_slov('Je to asi trosku divny, ale z retezce se proste da udelat seznam znaku celkem jednoduse.')

def to_by_stacilo_dej_mi_zase_vetu(slova):
    print(' '.join(slova))
#to_by_stacilo_dej_mi_zase_vetu(slova)

# seznamy se daji dobre michat i s random funkcemi, tzn. kdyz uz mame seznam vic hodnot, muzeme je nahodne zprehazet
# nebo z nich muzeme vybirat nahodne prvky

import random

def vypisuj_mi_nahodne_pejsky(plemena_psu):
    for i in range(10):
        print(random.choice(plemena_psu))
#vypisuj_mi_nahodne_pejsky(plemena_psu)

def zprehazej_mi_pejsky(plemena_psu):
    random.shuffle(plemena_psu)
    print(plemena_psu)
#zprehazej_mi_pejsky(plemena_psu)

# rekneme, ze mali psi jsou prvni podseznam, stredni ten druhy a velci jsou posledni

plemena_podle_velikosti = [['jezevcik','jack-russel','shiba-inu'],['bigl','borderka','kokrspanel'],['labik','doga','ovcak']]

def vypis_mi_male_pejsky(seznam):
    print(seznam[0])
#vypis_mi_male_pejsky(plemena_podle_velikosti)

def vypis_mi_prvniho_velkeho_psa(seznam):
    velci_psi = seznam[2]
    print(velci_psi[0])
    # print(seznam[2][0])
#vypis_mi_prvniho_velkeho_psa(plemena_podle_velikosti)
