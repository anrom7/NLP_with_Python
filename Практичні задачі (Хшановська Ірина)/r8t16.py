import nltk
entries = nltk.corpus.ppattach.attachments('training')
table = nltk.defaultdict(lambda: nltk.defaultdict(set)) # empty dictionary,values of it's entries are dictionaries
# choice of the verb determines whether the PP is attached to the VP or to the NP.
for entry in entries:
    key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2 # fill the dictionary by keys that will contain a noun+preposition+noun
    table[key][entry.attachment].add(entry.verb) 
#Review of the vocabulary and the text output
for key in sorted(table):
    if len(table[key]) > 1:
        print key, 'N:', sorted(table[key]['N']), 'V:', sorted(table[key]['V'])
