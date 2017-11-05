## SEZNAMY - LISTS ##

# 01 - INICIALIZACE

# Prazdny seznam:

def prazdny_seznam():
    seznam = []
    print(seznam)
# prazdny_seznam()

# Seznam obsahujici nejake hodnoty

plemena_psu = ['labik','husky','ovcak','staffik']
#print(plemena_psu)

# Vypsani hodnot pomoci for cyklu

def vypis_plemena(list_plemen):
    for plemeno in list_plemen:
        print(plemeno)

#vypis_plemena(plemena_psu)

# UKOL 01: Vytvor seznam oblibenych jidel a vypis je pod sebe, staci jen par jidel :)


# Ano, ano, seznamy muzou obsahovat ruzne datove typy, je to heterogenni datova struktura

def vytvor_typove_nesourody_seznam(polozka):
    typove_nesourody_seznam = ['mela', 'babka', 4, polozka, 'a', 'dedecek', 'jenom', None, ['dej', 'mi', 'babko'], 4, polozka, 'budeme mit', True]
    return typove_nesourody_seznam

#print(vytvor_typove_nesourody_seznam('jabka'))

