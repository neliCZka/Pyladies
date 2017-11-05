import pytest
import piskvorky

def test_vyhodnot_vyhral_x_uprostred():
    assert piskvorky.vyhodnot('ooxxxoo') == 'x'

def test_vyhodnot_vyhral_x_nakraji():
    assert piskvorky.vyhodnot('xxxoo') == 'x'

def test_vyhodnot_vyhral_o_uprostred():
    assert piskvorky.vyhodnot('xxooo--') == 'o'

def test_vyhodnot_vyhral_o_nakraji():
    assert piskvorky.vyhodnot('-xxooo') == 'o'

def test_vyhodnot_remiza():
    assert piskvorky.vyhodnot('ooxxooxo') == '!'

def test_vyhodnot_nedohrano():
    assert piskvorky.vyhodnot('xoxo-o-') == '-'

def test_tah():
    assert piskvorky.tah('-x-ox-o--',2,'x') == '-xxox-o--'

def test_tah():
    assert piskvorky.tah('-x-ox-o--',0,'x') == 'xx-ox-o--'

def test_tah_obecny_zaporne_cislo():
    def out(s):
        assert s == 'Zadej hodnotu v rozmezi 0 - 8!'
    piskvorky.tah_obecny('--xxoo--',lambda x:-1,out)

def test_tah_obecny_obsazena_pozice():
    def out(s):
        assert s == 'Tam uz tah je, zkus jinou pozici!'
    piskvorky.tah_obecny('--xxoo--',lambda x:2,out)

