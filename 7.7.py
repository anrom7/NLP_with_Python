import nltk
from nltk.corpus import conll2000
grammar="NP: {<DT|IN|PRP|NN>?<VBG><DT>?<NN>*}" # Задаю граматику
cp=nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt'[:100], chunk_types=['NP']) # Оцінюю якість роботи чанкера на прикладі 100 тестових речень
print cp.evaluate(test_sents)
# ChunkParse score:
#    IOB Accuracy:  42.3%
#    Precision:      4.9%
#    Recall:         0.3%
#    F-Measure:      0.5%
sentence='My brother found me wishing upon the falling star'
sentence=sentence.split()
tagged=nltk.pos_tag(sentence)
result=cp.parse(tagged)
print result
#(S
#  My/PRP$
#  brother/NN
#  found/VBD
#  (NP me/PRP wishing/VBG)
#  upon/IN
#  the/DT
#  falling/NN
# star/NN)

chunkscore = nltk.chunk.ChunkScore()
chunkscore.score(test_sents,result)
for chunk in chunkscore.incorrect(): # The chunks which were included in the guessed chunk structures, but not in the correct chunk structures, listed in input order.
	print chunk

#(NP me/PRP wishing/VBG)

for chunk in chunkscore.missed(): # The chunks which were included in the correct chunk structures, but not in the guessed chunk structures, listed in input order.
	print chunk	
#(S
#  As/IN
#  recounted/VBN
#  in/IN
#  (NP a/DT stipulation/NN)
#  (NP that/WDT)
#  summarized/VBD
#  (NP government/NN documents/NNS)
#  released/VBN
#  for/IN
#  (NP the/DT North/NNP trial/NN)
#  ,/,
#  (NP Mr./NNP Noriega/NNP)
#  offered/VBD
# to/TO
#  assassinate/VB
# (NP the/DT Sandinista/NNP leadership/NN)
#  in/IN
#  (NP exchange/NN)
#  ``/``
#  for/IN
#  (NP a/DT promise/NN)
#  to/TO
#  help/VB
#  clean/JJ
#  up/IN
#  (NP Noriega/NNP)
#  (NP 's/POS image/NN)
#  and/CC
#  (NP a/DT commitment/NN)
#  to/TO
#  lift/VB
#  (NP the/DT -LCB-/( U.S./NNP ./. -RCB-/) ban/NN)
#  on/IN
#  (NP military/JJ sales/NNS)
#  to/TO
#  (NP the/DT Panamanian/NNP Defense/NNP Forces/NNPS)
#  ./.
#  ''/'')
