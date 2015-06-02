# Categorizing and Tagging Words.
# Pokotylo Olena ALs-11
# Chapter 8 (exercise 16)

import nltk
# technique for mining the PP Attachment Corpus
entries = nltk.corpus.ppattach.attachments('training')
table = nltk.defaultdict(lambda: nltk.defaultdict(set))
for entry in entries:
	key = entry.noun1+ '-'+entry.prep +  '-' + entry.noun2# looking for unchangeble construction noun + preposition + noun
	if key =="noun1":
		key1 = entry.verb + '-' + entry.noun1
	elif key == "noun2":
		key1 = entry.verb + '-' + entry.noun2
	else:
		key1 = entry.verb + '-' + entry.prep
		
		pphrase = entry.noun1 + '-' + entry.prep +  '-' + entry.noun2
		table[key1][entry.attachment].add(pphrase)# list of corteges

		
print pphrase # print noun1+preposition+noun2 = unchangeble construction
# with the help of this program we can find different groups of words which have construction Noun+ prepositon+ noun
# and also the words constraction which are unchangeble. also I find unchangeble construction as stance-in-light. 
