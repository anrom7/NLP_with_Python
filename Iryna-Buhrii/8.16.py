import nltk
items = nltk.corpus.ppattach.attachments('training') 
list = nltk.defaultdict(lambda: nltk.defaultdict(set)) 
# Creating empty dictionary, which items values are dictionaries.
for item in items:
    key = item.noun1 + '-' + item.prep + '-' + item.noun2 
# Filling the dictionary with items Noun + Preposition + Noun.
    list[key][item.attachment].add(item.verb)
# Revision of the dictionary and output data.
for key in sorted(list):
    if len(list[key]) > 1:
        print key, 'N:', sorted(list[key]['N']), 'V:', sorted(list[key]['V'])


