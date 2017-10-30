from ai import rand_input

def vyhodnot(herni_pole):
    if 'xxx' in herni_pole:
        stav_hry = 'x'
    elif 'ooo' in herni_pole:
        stav_hry = 'o'
    elif '-' not in herni_pole:
        stav_hry = '!'
    else:
        stav_hry = '-'
    return stav_hry

def tah(herni_pole, policko, symbol):
    herni_pole_s_novym_tahem = herni_pole[:policko] + symbol + herni_pole[policko + 1:]
    return herni_pole_s_novym_tahem

def std_input(herni_pole):
    """funkce na vstup pozice od uzivatele. kvuli testum hlavne"""
    try:
        pozice = input('Na jake pozici chces tahnout? ')
        pozice = int(pozice)
        return pozice
    except ValueError:
        print('zadavej cislo')

def tah_obecny(herni_pole, inp, out):
    kontrola = True
    while kontrola:
        pozice = inp(herni_pole)
        if pozice < 0 or pozice > len(herni_pole):
            out('Zadej hodnotu v rozmezi 0 - ' + str(len(herni_pole)) + '!')
        elif herni_pole[pozice] != '-':
            out('Tam uz tah je, zkus jinou pozici!')
        else:
            kontrola = False
            out('Zaznamenano')
        return pozice

def out_none(*args):
    pass

# def tah_pocitace(herni_pole):
#     return tah_obecny(herni_pole, rand_input, out_none)
#
# def tah_hrace(herni_pole):
#     return tah_obecny(herni_pole, std_input, print)

