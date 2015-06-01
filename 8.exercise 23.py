

# Fedorchak V ALs- 11
# Chapter 8, Exercise 22

import nltk
entries = nltk.corpus.ppattach.attachments('training') # empty dictionary
table = nltk.defaultdict(lambda: nltk.defaultdict(set)) # filling the dictionaty
for entry in entries:
	key = entry.verb + '-P-' + entry.noun1
	table[key][entry.attachment].add(entry.prep)

for key in sorted(table): # show the dictionary
	if len(table[key]) > 1:
		print key, '-', 'P depends on N:', sorted(table[key]['N']), 'P depends on V:', sorted(table[key]['V'])
