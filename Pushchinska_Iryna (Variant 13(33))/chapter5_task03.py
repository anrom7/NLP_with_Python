# Pushchinska_Iryna PRLs-11
# Chapter_5, Task_3

import nltk
text = nltk.word_tokenize("They wind back the clock, while we chase after the wind.")
nltk.pos_tag(text)
print nltk.pos_tag(text)
#POS tagger опрацьовує послідовність слів і присвоює кожному слову тег частину мови. Результати програми показали, що слово 'They' - займенник, 'wind'-дієслово, 'back'-прислівник, 'the'-артикль, 'clock'-годинник, 'while'-сполучник, 'we'-займенник, 'chase'-дієслово, 'after'-сполучник, 'the'-артикль, 'wind'- іменник.   
#тег вказує до якої частини мови належить слово. наприклад слово wind зусрічається 2 рази, перший раз воно виступає дієсловом і означає "переводити назад", а другий-іменником - "вітер".
