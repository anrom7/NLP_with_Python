# Pushchinska_Iryna PRLs-11
# Chapter_5, Task_19

import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

list_input = [
    (r'(I|you|they|he|she|it)$', 'PR'),   # pronouns
        (r'.*ing$', 'NN'),                # nouns
        (r'.*ing$', 'VBG'),               # gerunds
	(r'.*ed$', 'VBD'),                # simple past
	(r'.*es$', 'VBZ'),                # 3rd singular present
        (r'.*e$', 'VBZ'),                 # 1st singular present
	(r'.*ould$', 'MD'),               # modals
	(r'.*\'s$', 'NN$'),               # possessive nouns
	(r'.*s$', 'NNS'),                 # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
	(r'.*', 'NN')                     # nouns (default)
]

t = nltk.RegexpTagger(list_input)
t.tag(brown_sents[2])
print "\nWait some seconds... Counting...\n"
print t.evaluate(brown_tagged_sents)
# We can improve the performance this number by improving 
# RegExr or/and combine this tagger with the default tagger

# !!!!!
# То доповнена програмка на кращу поточку,
# де потрібно було дописати регулярні вирази,
# які могли б протегувати таке речення: "I like spring"
# Так, про всяк випадок, нагадую, що вже 15 балів я заробила ще в четвер після лекції,
# а ця доповнена програмка на вищу поточку.
