__author__ = 'angelinaprisyazhnaya'

import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import Levenshtein

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

all_lemmas = open('REVERSE.TXT', 'r', encoding='CP1251')
all_lemmas = all_lemmas.read()

words = open('dict.opcorpora.txt', 'r')
words = words.read()
all_words = set(words.lower().split())


def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))


def morph_analysis(word):
    aux_pos_tags = ['PREP', 'CONJ', 'PRCL', 'INTJ']
    m = morph.parse(word)
    first_pos = str(m[0][1])
    if first_pos in aux_pos_tags:
        p_misc = m[0][3]
        p_named = 0.0
        for i in m:
            if str(i[1]) not in aux_pos_tags:
                p_named = i[3]
                break

    else:
        p_misc = 0.0
        p_named = m[0][3]
        for i in m:
            if str(i[1]) in aux_pos_tags:
                p_misc = i[3]
                break
    return p_misc, p_named


def spellchecking(word):
    x_normal_i = {}
    if word not in all_words:
        possible_words = edits1(word)
        for i in possible_words:
            if morph.parse(i)[0][2] in all_lemmas:
                if i in all_words:
                    x_normal_i[i] = Levenshtein.distance(word, i)
    else:
        x_normal_i[word] = 0
    return x_normal_i


test_word = 'словл'
p = morph_analysis(test_word)
d = spellchecking(test_word)

print('word = ' + test_word)
print('P_misc = ' + str(p[0]))
print('P_named = ' + str(p[1]))
print('X_normal_i = ' + str(d))
