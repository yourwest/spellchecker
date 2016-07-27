from spellchecker import spellchecking, morph_analysis
import pytest

def test_sane():
    word = "самовар"
    p = morph_analysis(word)
    d = spellchecking(word)
    assert len(d) == 1
    assert list(d.keys())[0] == word
    
    print('P_misc = ' + str(p[0]))
    print('P_named = ' + str(p[1]))

def test_city():
	pass


def test_name():
	pass


def test_numbers():
	pass


def test_words():
	pass