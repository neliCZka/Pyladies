
# 02 - PRISTUP K HODNOTAM V SEZNAMU

# Seznamy jsou SERAZENE a kazda hodnota ma svuj INDEX, ktery urcuje misto (poradi), na kterem se hodnota nachazi.
# Indexy (poradi) nezacinaji od 1, nybrz od 0!

# Vypiseme si prvni plemeno ze seznamu plemen psu
plemena_psu = ['labik','husky','ovcak','staffik']
# print plemena_psu[0]

# UKOL 02: Vypis druhe plemeno a pak i to treti

# Nekdy muzeme chtit zjistit, co je na prvnich nekolika mistech v seznamu, nebo treba prave na tech poslednich mistech.
# To nam Python umi ukazat pomoci SLICE funkce.

# Ted si vypiseme vsechna plemena od 3. v poradi:
# print plemena_psu[2:]

# Takto si zase vypiseme vsechna plemena od zacatku az do tretiho.
# print plemena_psu[:2]

# Hm, nejak ti tam to treti plemeno chybi, ne?
# No jo, je to tim, ze slice je exclusive - nefunguje jako "vcetne", takze pokud chceme vsechny az po treti plemeno VCETNE, musime pridat +1
# print plemena_psu[:3]


# Obcas muzeme potrebovat pristupovat k hodnote i indexu soucasne, i to nam Python umoznuje
# Tak jo, zkusime to asi takhle?
def dej_mi_index_i_hodnotu(seznam):
    for index, hodnota in seznam:
        print index, hodnota

#dej_mi_index_i_hodnotu(plemena_psu)

# Eeeeeh, co to ma byt jako???
# Bohuzel se k indexu a hodnote zaroven neda dostat tak uplne jednoduse, musime si zavolat na pomoc pythoni funkci 'enumerate'

def dej_mi_index_i_hodnotu_sakra(seznam):
    for index, hodnota in enumerate(seznam):
        print index, hodnota

# dej_mi_index_i_hodnotu_sakra(plemena_psu)

