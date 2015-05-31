# Shepelevych PRLs-11

import nltk
# technique for mining the PP Attachment Corpus
entries = nltk.corpus.ppattach.attachments('training')
table = nltk.defaultdict(lambda: nltk.defaultdict(set))
for entry in entries:
	key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
	table[key][entry.attachment].add(entry.verb)

for key in sorted(table):
	if len(table[key]) > 1:
		print key, 'N:', sorted(table[key]['N']), 'V:', sorted(table[key]['V'])

