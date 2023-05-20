# Fichier de Test des Fonctions 
from Nim_variante_part3_Naumova_Silva import *

tab1 = [31, 4, 6, 3]
tab2 = [21, 5, 33, 9]
tab3 = [0, 1, 0, 1]

tab4 = ['001', '00101', '11010', '1101110']
tab5 = ['10110', '10110', '0000', '10110']
tab6 = ['1', '1011', '10111', '11101']
tab7 = ['0001', '100', '110', '11100']
tab8 = ['01', '1', '1001', '1111']

def test_verif_tri():
	assert verif_tri([0, 1, 2, 3, 4, 5]) == False, "Erreur sur verif_tri : test 1"
	assert verif_tri([5, 4, 3, 2, 1, 0]) == True, "Erreur sur verif_tri : test 2"
	assert verif_tri([]) == False, "Erreur sur verif_tri : test 3"

def test_int_to_bin():
	assert int_to_bin(13) == '1101', "Erreur sur test_int_to_bin : test 1"
	assert int_to_bin(53) == '110101', "Erreur sur test_int_to_bin : test 2"
	assert int_to_bin(22) == '10110', "Erreur sur test_int_to_bin : test 3"
	assert int_to_bin(14) == '1110', "Erreur sur test_int_to_bin : test 4"
	assert int_to_bin(0) == '0', "Erreur sur test_int_to_bin : test 5"
	assert int_to_bin(1) == '1', "Erreur sur test_int_to_bin : test 6"

def test_bin_to_int():
	assert bin_to_int('0100101') == 37, "Erreur sur test_bin_to_int : test 1"
	assert bin_to_int('01011110100001') == 6049, "Erreur sur test_bin_to_int : test 2"
	assert bin_to_int('0101111010') == 378, "Erreur sur test_bin_to_int : test 3"
	assert bin_to_int('010') == 2, "Erreur sur test_bin_to_int : test 4"
	assert bin_to_int('0') == 0, "Erreur sur test_bin_to_int : test 5"
	assert bin_to_int('1') == 1, "Erreur sur test_bin_to_int : test 6"

def test_tab_int_to_tab_bin():
    assert tab_int_to_tab_bin(tab1) == ['11111', '100', '110', '11']
    assert tab_int_to_tab_bin(tab2) == ['10101', '101', '100001', '1001']
    assert tab_int_to_tab_bin(tab3) == ['0', '1', '0', '1']
    assert tab_int_to_tab_bin([]) == []
    
def test_xor():
    assert xor("1", "0") == "1", "Erreur sur test_xor : test 1"
    assert xor("0", "0") == "0", "Erreur sur test_xor : test 2"
    assert xor("1", "1") == "0", "Erreur sur test_xor : test 3"
    assert xor("101", "000") == "101", "Erreur sur test_xor : test 4"
    assert xor("101", "010") == "111", "Erreur sur test_xor : test 5"
    assert xor("", "") == "", "Erreur sur test_xor : test 6"
    
def test_somme_xor():
    assert somme_xor(tab4) == '1110000', "Erreur sur test_somme_xor : test 1"
    assert somme_xor(tab5) == '10110', "Erreur sur test_somme_xor : test 2"
    assert somme_xor(tab6) == '00000', "Erreur sur test_somme_xor : test 3"
    assert somme_xor(tab7) == '11111', "Erreur sur test_somme_xor : test 4"
    assert somme_xor(tab8) == '0110', "Erreur sur test_somme_xor : test 5"

def test_type_config():
    assert type_config(tab4) == False, "Erreur sur test_type_config : test 1"
    assert type_config(tab5) == False, "Erreur sur test_type_config : test 2"
    assert type_config(tab6) == True, "Erreur sur test_type_config : test 3"
    assert type_config(tab7) == False, "Erreur sur test_type_config : test 4"
    assert type_config(tab8) == False, "Erreur sur test_type_config : test 5"

def test_ligne_a_modifer():
    assert ligne_a_modifier(tab4) == 3, "Erreur sur test_ligne_a_modifer : test 1"
    assert ligne_a_modifier(tab5) == 0, "Erreur sur test_ligne_a_modifer : test 2"
    assert ligne_a_modifier(tab6) == 3, "Erreur sur test_ligne_a_modifer : test 3"
    assert ligne_a_modifier(tab7) == 3, "Erreur sur test_ligne_a_modifer : test 4"
    assert ligne_a_modifier(tab8) == 3, "Erreur sur test_ligne_a_modifer : test 5"
    
test_bin_to_int()
test_int_to_bin()
test_tab_int_to_tab_bin()
test_verif_tri()
test_xor()
test_somme_xor()
test_type_config()
test_ligne_a_modifer()
print ("Tout les tests sont bon")