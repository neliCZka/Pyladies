
# 03 - ZMENY V SEZNAMECH

# Seznamy jsou MENITELNE (MUTABLE), takze se do nich daji pridat prvky, daji se z nich smazat prvky a take se prvky daji menit
# Je to dulezitejsi vlastnost, nez by se mohlo zdat!


# PRIDAVANI PRVKU

# Pridame si plemeno
plemena_psu = ['labik','husky','ovcak','staffik']

def pridej_plemeno(seznam):
    seznam.append('samojed')
    print(seznam)
#pridej_plemeno(plemena_psu)

# UKOL 03: Pridej dalsi plemeno (napr. jezevcik), nemusis ve funkci


# Nemusime pridavat vzdy jen jeden prvek, muze se stat, ze jich potrebujeme pridat vic a k tomu slouzi funkce extend

# Pridame par dalsich plemen
def pridej_vic_plemen(seznam,hodnoty):
    seznam.extend('bernak','malamut')
    print(seznam)
#pridej_vic_plemen(plemena_psu)

# Jezismarja, tohle je nejaka blbost, vzdyt to nefunguje.
# Nefunguje to proto, ze extend bere jako parametr list hodnot a tento list "rozseka" na jednotlive hodnoty a prave ty prida do puvodniho seznamu.

def pridej_vic_plemen(seznam):
    seznam.extend(['bernak','malamut'])
    print(seznam)
#pridej_vic_plemen(plemena_psu)

# A co kdyz budeme chtit ale pridat samotnej seznam do seznamu?
# Tak pouzijeme append :)

def pridej_seznam_do_seznamu(seznam):
    seznam.append(['rotwik','dobrman'])
    print(seznam)
#pridej_seznam_do_seznamu(plemena_psu)
