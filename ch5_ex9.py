# Anna Hadzalo
#PRLS-11
#Chapter 5
# Task 9

import nltk
from nltk.corpus import brown
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if w2=='go':
            print t1, t3

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)

def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if w2=='went':
            print t1, t3

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)
#Спочатку я переглянула слова, які можуть вживатися перед дієсловами go та went, та після них.

sent1=nltk.word_tokenize("Go away!")
sent2=nltk.word_tokenize("We went on the excursion.")
nltk.pos_tag(sent1), nltk.pos_tag(sent2)
print nltk.pos_tag(sent1), nltk.pos_tag (sent2)

#Потім я здійснила токенізацію речень, у яких вживаються дані дієслова.
#В результаті я зробила висновок, що дієслова go та went передають різні граматичні форми.
#Тому кожне з них вживається у конкретному контескті.
#В даному випадку вживання цих дієслів залежить від граматичної категорії - часу.
