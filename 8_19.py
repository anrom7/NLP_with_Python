# Anna Karbivska, ALs-11
# 8.9.19
#Read up on Уgarden pathФ sentences. How might the computational work of
#a parser relate to the difficulty humans have with processing these sentences?
#(See http://en.wikipedia.org/wiki/Garden_path_sentence.)

import nltk
grammar = nltk.parse_cfg("""
S -> NP VP
NP -> Det N | Det N VP
VP -> V NP | V
Det -> 'The' | 'the'
N -> 'old' | 'boat'
V -> 'man'
""") # створюЇмо граматику
sent = ['The', 'old', 'man', 'the', 'boat'] # створюЇмо реченн€
parser = nltk.ChartParser(grammar) # використовуЇмо ChartParser дл€ нашого анал≥зу 
trees = parser.nbest_parse(sent)
for tree in trees:
	print 'Tree = ', tree # виводимо дерево на екран
	

answer1=('_______________Answer:')
print answer1
answer=('#Уgarden pathФ sentences - це граматично правильн≥ реченн€, в €ких кожне слово в≥доме, проте зрозум≥ти чи зробити cинтаксичний анал≥з таких речень важко €к ≥ дл€ людини, так ≥ дл€ комютера.Ќаприклад  УThe old man the boat.Ф це може означати, що "старий чолов≥к ... човен", табто реченн€ некоректне тому що без д≥Їслова,але насправд≥ "man" це д≥Їслово що означаЇ "укомплектовувати" ≥ це реченн€ перекладають €к "—тарий укомплектовуЇ човен". ќтже, €к ≥ людина так ≥ машина може припуститис€ помилки,хоча людина правильн≥ше анал≥зуЇ реченн€.')
print answer



