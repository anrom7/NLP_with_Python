# Categorizing and Tagging Words.
# Pokotylo Olena ALs-11
# 5.10 (exercise 2)
# Working with someone else, take turns to pick a word that can be either a noun or a verb (e.g. contest); the opponent has to predict which one is likely to be the most frequent in the Brown corpus; check the opponent's prediction, and tally the score over several turns.
>>> import nltk
>>> from nltk.corpus import brown
>>> tagged_w=brown.tagged_words()

>>> tagged_w[:15]
[('The', 'AT'), ('Fulton', 'NP-TL'), ('County', 'NN-TL'), ('Grand', 'JJ-TL'), ('Jury', 'NN-TL'), ('said', 'VBD'), ('Friday', 'NR'), ('an', 'AT'), ('investigation', 'NN'), ('of', 'IN'), ("Atlanta's", 'NP$'), ('recent', 'JJ'), ('primary', 'NN'), ('election', 'NN'), ('produced', 'VBD')]
# let's check which part of speech is word 'cake'
>>> for w,t in tagged_w:
	if w=='cake':
		print t

		
NN
NN
NN
NN
NN
NN
NN
NN
NN
NN
NN
NN
NN
# now let's check word 'fight'
>>> for w,t in tagged_w:
	if w=='fight':
		print t

		
NN
NN
NN
NN
NN
NN
NN-HL
NN
NN
VB
VB
NN
NN
VB
NN
VB
VB
NN
VB
NN
VB
VB
VB
VB
VB
NN
VB
VB
NN
NN
VB
NN
VB
NN
VB
NN
VB
NN
NN
NN
NN
NN
NN
VB
VB
VB
NN
VB
VB
NN
NN
NN
NN
VB
VB
VB
NN
NN
VB
VB
NN
NN
VB
VB
NN
NN
VB
VB
NN
NN
NN
NN
NN
VB
VB
VB
NN
VB
NN
VB
NN
NN
VB
NN
NN
VB
NN
VB
NN
NN
VB
NN
VB
NN
NN
VB
NN
# we can use another way and see if the particular word is used as different part of speech, and what those parts of speech are.
>>> cfd=nltk.ConditionalFreqDist(tagged_w)
>>> cfd['fight']
<FreqDist with 3 samples and 97 outcomes>
>>> cfd['name']
<FreqDist with 3 samples and 292 outcomes>
>>> cfd['name'].keys()
['NN', 'VB', 'NN-HL']
>>> cfd['signal'].keys()
['NN', 'VB']
>>> cfd['back'].keys()
['RB', 'NN', 'JJ', 'VB', 'RB-HL']
