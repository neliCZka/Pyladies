# 01 - TUPLES (N-TICE)

# Jsou to datove struktury obsahujici obvykle vice prvku
# Nejsou uplne stejne jako seznamy

# Narozdil od seznamu jsou NEMENITELNE -> neda se k nim pridavat, neda se z nich mazat a nedaji se jim menit hodnoty
# Ale stejne jako seznamy jsou SERAZENE

# Tuple vypada treba takto:
plemena_psu = 'labik','ovcak','jezevcik'
sezerou = '10','12','2'

# Nepouzivaji zadne hranate [], chlupate {} nebo jine zavorky, proste se hodnoty jen oddeli carkou

def vypis_plemena(ntice):
    for plemeno in ntice:
        print(plemeno)

#vypis_plemena('labik','ovcak','jezevcik')
# Jooo, chudak funkce potrebuje nejak vedet, co jsou jednotlive argumenty a co uz jsou hodnoty, ktere se ji snazime predat
#vypis_plemena(plemena_psu)
#vypis_plemena(('labik','ovcak','jezevcik'))

def rekni_mi_kolik_sezere(plemeno):
    index = plemena_psu.index(plemeno)
    krmivo = sezerou[index]
    return plemeno, krmivo

#print(rekni_mi_kolik_sezere('ovcak'))
#plemeno, krmivo = rekni_mi_kolik_sezere('ovcak')
#print('{} sezere {} kg krmiva za mesic'.format(plemeno,krmivo))

# Hodnoty z dvou tuplu se daji kombinovat mnohem elegantneji a sice pouzitim funkce zip()
# funkce zip funguje podobne jako zip na mikine, takze spoji hodnoty z obou ntic na stejne pozici

def rekni_mi_kolik_sezere_kazde_plemeno(plemena,sezerou):
    for plemeno, krmivo in zip(plemena,sezerou):
        print('{} sezere {} kg krmiva za mesic'.format(plemeno, krmivo))

#rekni_mi_kolik_sezere_kazde_plemeno(plemena_psu,sezerou)

# Enumerate proiteruje list nebo i tuple s jeho indexy i hodnotami
def vypis_index_kazdeho_psa(seznam):
    for index,plemeno in enumerate(seznam):
       print('na indexu {} je plemeno {}'.format(index, plemeno))

#vypis_index_kazdeho_psa(plemena_psu)

