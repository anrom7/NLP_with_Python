import nltk,re, pprint
def ie_preprocess(document):
	sentences = nltk.sent_tokenize(document)                     # ������� ��������� �������
	sentences = [nltk.word_tokenize(sent) for sent in sentences] # ���������� ���
	sentences = [nltk.pos_tag(sent) for sent in sentences]       # ����� ������ ����
	print sentences
	
document = "Rapunze let down her long golden hair"               # ������� �������
print ie_preprocess(document)
grammar = r"""
NP: {<DT|JJ|NN.*>+} # Chunk sequences of DT, JJ, NN
PP: {<IN><NP>} # Chunk prepositions followed by NP
VP:{<VB.*><NP|PP|CLAUSE>+$}# Chunk verbs and their arguments
CLAUSE: {<NP><VP>}# Chunk NP, VP
"""
sentence =[("Rapunzel","NNP"), ("let","VBD"),("down","RP"),("her","PP$"),("long","JJ"),("golden","JJ"),("hair","NN")]
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)                                      # ��������� ������
print result                                                     # �������� ����������
