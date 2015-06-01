# Anna Karbivska AL-11
# 5.10.2
#Working with someone else, take turns to pick a word that can be either a noun or a verb (e.g. contest); the opponent has to predict which one is likely to be the most frequent in the Brown corpus; check the opponent's prediction, and tally the score over several turns.
>>> import nltk
>>> from nltk.corpus import brown
>>> tagged_w=brown.tagged_words()
>>> tagged_w[:15]
[('The', 'AT'), ('Fulton', 'NP-TL'), ('County', 'NN-TL'), ('Grand', 'JJ-TL'), ('Jury', 'NN-TL'), ('said', 'VBD'), ('Friday', 'NR'), ('an', 'AT'), ('investigation', 'NN'), ('of', 'IN'), ("Atlanta's", 'NP$'), ('recent', 'JJ'), ('primary', 'NN'), ('election', 'NN'), ('produced', 'VBD')]
# checking the word 'play'
>>> for w,t in tagged_w:
	if w=='play':
		print t

		
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
VB
VB
NN
NN
NN
NN
VB
VB
VB
VB
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
VB
VB
VB
VB
VB
VB
VB
NN
VB
VB
VB
VB
VB
NN
VB
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
NN
VB
VB
VB
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
NN
NN
NN
NN
VB
VB
NN
NN
VB
VB
VB
VB
VB
VB
NN
NN
VB
NN
NN
NN
VB
VB
VB
VB
NN
VB
NN
NN
NN
VB
VB
NN
VB
VB
NN
VB
VB
VB
VB
NN
VB
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
VB
VB
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
VB
VB
VB
VB
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
VB
VB
NN
NN
NN
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
VB
NN
NN
NN
VB
NN
VB
VB
VB
VB
VB
VB
VB
VB
VB
VB
VB
VB
VB
VB
VB
VB
VB
VB
VB
NN
NN
NN
# checking the word 'match'
>>> for w,t in tagged_w:
	if w=='match':
		print t

		
VB
NN
VB
VB
VB
NN
VB
VB
VB
NN
VB
NN
NN
VB
VB
VB
VB
VB
VB
VB
VB
VB
VB
NN
VB
VB
VB
NN
VB
NN
NN
VB
VB
VB
NN
NN
NN
NN
NN
VB
NN
#another way:
>>> cfd=nltk.ConditionalFreqDist(tagged_w)
>>> cfd['play']
<FreqDist with 2 samples and 197 outcomes>
>>> cfd['match']
<FreqDist with 2 samples and 41 outcomes>
>>> cfd['play'].keys()
['VB', 'NN']
>>> 
