#Anna Karbivska, ALs-11
# 8.9.16
# Pick some common verbs and complete the following tasks:
#a. Write a program to find those verbs in the PP Attachment Corpus nltk.cor
#pus.ppattach. Find any cases where the same verb exhibits two different attachments,
#but where the first noun, or second noun, or preposition stays
#unchanged (as we saw in our discussion of syntactic ambiguity in Section 8.2).
#b. Devise CFG grammar productions to cover some of these cases.

import nltk
entries = nltk.corpus.ppattach.attachments('training')# empty dictionary
table = nltk.defaultdict(lambda: nltk.defaultdict(set))# filling the dictionaty
for entry in entries:
	 key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
	 table[key][entry.attachment].add(entry.verb)

for key in sorted(table): # show the dictionary
	if len(table[key]) > 1:
		print key, 'N:', sorted(table[key]['N']), 'V:', sorted(table[key]['V'])

import nltk
entries = nltk.corpus.ppattach.attachments('training')# empty dictionary
table = nltk.defaultdict(lambda: nltk.defaultdict(set))# filling the dictionaty
for entry in entries:
	if key =="noun1":
		key1 = entry.verb + '-' + entry.noun1
	elif key == "noun2":
		key1 = entry.verb + '-' + entry.noun2
	else:
		key1 = entry.verb + '-' + entry.prep
		pphrase = entry.noun1 + '-' + entry.prep +  '-' + entry.noun2
		table[key1][entry.attachment].add(pphrase)# list of corteges

def find_verb(verb):
	 return [(verb,w1[i]) for i in w1.keys() if str(i).startswith(verb) and len(w1[i])>1] # result of verbs
print pphrase
