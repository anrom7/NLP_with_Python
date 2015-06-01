
#Turianska K., Prls-11, Chapter_7_ex_1
import nltk
sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"), ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]
grammar = r"""
NP:  {<DT|PP\$>?<JJ>*<NN>}
	{<NNP>+}
"""
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result
result.draw()
