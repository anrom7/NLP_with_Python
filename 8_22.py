##Viktoriia Palianytsia, AL-11, chapter 8, task 22
import nltk
entries = nltk.corpus.ppattach.attachments('training') #робота з корпусом PP Attachments
table = nltk.defaultdict(lambda: nltk.defaultdict(set))
for entry in entries:
	key = entry.verb + '-P-' + entry.noun1             #створення фраз з якими будемо працювати 
	table[key][entry.attachment].add(entry.prep)

for key in sorted(table): 
	if len(table[key]) > 1:                            #створення умови для презентабельного вигляду
		print key, '-', 'P depends on N:', sorted(table[key]['N']), 'P depends on V:', sorted(table[key]['V'])

		

