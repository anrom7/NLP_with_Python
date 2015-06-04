# Уляна Щомак ПРЛс-12 

import nltk
from nltk.corpus import conll2000
test_sents = conll2000.chunked_sents('test.txt'[:100], chunk_types=['NP'])
grammar="NP: {<DT|JJ>?<RB>?<VBN>?<NN.*>+}" # Створюю правило для граматики, обираю довільне речення
sent='Forecsasts for the trade figures range widely but few economists expect the data to show a very marked improwment from the 2 billion deficit in the current account reported for August'
sentence=sent.split()
tagged=nltk.pos_tag(sentence)
cp=nltk.RegexpParser(grammar) # Парсер на основі граматики
result=cp.parse(tagged) # Обробляю речення
print cp.evaluate(test_sents)
print result
#(S
#  (NP Forecsasts/NNS)
#  for/IN
#  (NP the/DT trade/NN figures/NNS)
#  range/VBP
#  widely/RB
#  but/CC
#  (NP few/JJ economists/NNS)
#  expect/VBP
#  (NP the/DT data/NNS)
#  to/TO
#  show/VB
#  (NP a/DT very/RB marked/VBN improwment/NN)
#  from/IN
#  the/DT
#  2/CD
#  billion/CD
#  (NP deficit/NN)
#  in/IN
#  the/DT
#  (NP current/JJ account/NN)
#  reported/VBD
#  for/IN
#  (NP August/NNP))

