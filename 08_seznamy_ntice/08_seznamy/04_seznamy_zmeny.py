
# 04 - ZMENY V SEZNAMECH

# ZMENY PRVKU
# Prvky seznamu se daji modifikovat, takze muzeme zmenit jakoukoli hodnotu v seznamu.

# Rekneme, ze jsme vlastne nechteli ovcaka, ale vlcaka. Co s tim?

plemena_psu = ['labik','husky','ovcak','staffik']
def zmen_ovcaka_za_vlcaka(seznam):
    seznam[2] = 'vlcak'
    print('tohle je seznam s vlcakem misto ovcaka: {}'.format(seznam))

#zmen_ovcaka_za_vlcaka(plemena_psu)

# UKOL XX: Zmen nektere plemeno za jine, nemusis nutne pres funkci :)


# A nam se vlastne nelibi ani ten staffik, dejme ho pryc.
# Funkce del smaze hodnotu z daneho indexu, nebo klidne i vic hodnot, pokud zadame rozsah jako [2:4]

def zrus_staffika(seznam):
    del seznam[3]
    print('tohle je seznam bez staffika: {}'.format(seznam))
#zrus_staffika(plemena_psu)

# A uz se nam nelibi ani vlcak, pryc s nim!
# Funkce pop() vyhodi posledni prvek ze seznamu

def zrus_i_vlcaka(seznam):
    seznam.pop()
    print('tohle je uz dost vyprazdnenej seznam: {}'.format(seznam))
#zrus_i_vlcaka(plemena_psu)

# A taky labika pryc

def labik_pryc(seznam):
    seznam.remove('labik')
    print('uz nam tu zbude jen husky: {}'.format(seznam))
#labik_pryc(plemena_psu)

# No asi se na ty pejsky vykasleme uplne a zacnem odznova

def vycisti_seznam(seznam):
    seznam.clear()
    print('a tady pojedem odznova s prazdnou: {}'.format(seznam))
#vycisti_seznam(plemena_psu)

