#chapter 8, Ex. 16
#by Ivanna Rurych
#task: Pick some common verbs and complete the following tasks:
#a. Write a program to find those verbs in the PP Attachment Corpus  nltk.cor
#pus.ppattach. Find any cases where the same verb exhibits two different attachments, but where the first noun, or second noun, or preposition stays
#unchanged (as we saw in our discussion of syntactic ambiguity in Section 8.2).
#b. Devise CFG grammar productions to cover some of these cases.
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
