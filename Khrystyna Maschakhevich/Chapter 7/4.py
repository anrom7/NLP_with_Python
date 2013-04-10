## Khrystyna Maschakevich, AL-13, Chapter 7, Task 4. 
##The task was to create a chunker that starts with the sentence in one chunk. To determine those tags which will probably fill the holes with the help of effective program


import nltk
sentence = [("Sumsung", "NNP"), ("is", "VBZ"), ("the", "DT"),
("leader", "NN"), ("in", "IN"), ("mobile", "JJ"), ("technology", "NN"), ("with", "IN"),("In-line", "JJ"), ("combination", "NN"), ("processes", "NNS"), ("for", "IN"), ("the", "DT"),("label", "NN"), ("industry", "NN"),  ("one", "CD"), ("of", "IN"), ("the", "DT"), ("fastest", "JJS"),("developing", "VBG"), ("trends", "NNS"), ("today", "NN] 
## example of sentence
grammar = r""" ## grammar
NP:
	{<.*>+}   ##Chunk everything
	}<VBD|IN|CC|IN|MD|RB|RBR|RP|SYM|TO|UH|VB|VBD|VBG|VBN|VBP|VBZ|WRB>+{
	"""
cp = nltk.RegexpParser(grammar)  ##using that grammar we create a chunk parser
result = cp.parse(sentence)    ## test it on our example sentence
## one can examine the results using  procedure - print result - the result can be a tree, or with the help of - result.draw()- displayed graphically




