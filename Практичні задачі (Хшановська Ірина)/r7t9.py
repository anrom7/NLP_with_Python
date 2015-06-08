

import nltk,re, pprint
def ie_preprocess(document):
	sentences=nltk.sent_tokenize(document)# sentence segmenter
	sentences=[nltk.word_tokenize(sent) for sent in sentences] # word tokenizer
	sentences=[nltk.pos_tag(sent) for sent in sentences]# part-of-speech tagger
	print sentences

document="Greece is close to finalizing a deal with private sector creditors."
print ie_preprocess(document)
grammar=r"""
NP: {<DT|JJ|NN.*>+}
PP: {<IN><NP>}
VP:{<VB.*><NP|PP|CLAUSE>+$}
CLAUSE: {<NP><VP>}
"""
sentence=[("Greece","NNP"), ("is","VBZ"),("close","JJ"),("to","TO"),("finalizing","VBG"),("a","DT"),("deal","NN"), ('with', 'IN'), ('private', 'JJ'), ('sector', 'NN'), ('creditors', 'NNS'), ('.', '.')]
cp=nltk.RegexpParser(grammar) # chunker
result=cp.parse(sentence)
print result
