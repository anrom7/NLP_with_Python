# Categorizing and Tagging Words.
# Pokotylo Olena ALs-11
# 5.10 (exercise 20)
# Write code to search the Brown Corpus for particular words and phrases according to tags, to answer the following questions:
>>> import nltk
>>> from nltk.corpus import brown
# 1.Produce an alphabetically sorted list of the distinct words tagged as MD.
>>> sorted(set([word for word, tag in tagged_w if tag=='MD']))
['Can', 'Could', 'May', 'Might', 'Must', 'Ought', 'Shall', 'Should', 'Will', 'Would', "c'n", 'can', 'colde', 'could', 'dare', 'kin', 'maht', 'mai', 'may', 'maye', 'mayst', 'might', 'must', 'need', 'ought', 'shall', 'should', 'shuld', 'shulde', 'wil', 'will', 'wilt', 'wod', 'wold', 'wolde', 'would']
#
#    =======  ======================  =====
#   Form     Category                Tag
#   =======  ======================  =====
#   go       base                    VB
#   goes     3rd singular present    VBZ
#   gone     past participle         VBN
#   going    gerund                  VBG
#   went     simple past             VBD
#   =======  ======================  =====
# plural nouns 'NNS'

# 2.Identify words that can be plural nouns or third person singular verbs (e.g. deals, flies).
>>> tagged_w=brown.tagged_words()
>>> for w,t in tagged_w[:500]
	if t=='VBZ':
		print w

deserves
believes
receives
>>> for w,t in tagged_w[:500]:
	if t=='NNS':
		print w

>>> for w,t in tagged_w[:500]:
	if t=='NNS':
		print w

		
irregularities
presentments
thanks
reports
irregularities
reports
voters
laws
legislators
laws
topics
departments
practices
governments
offices
personnel
personnel
policies
steps
funds
funds
services
homes
items
funds
departments
counties
jurors
funds
counties
funds
jurors
taxpayers
>>> 		

# Identify three-word prepositional phrases of the form IN + DET + NN (eg. in the lab).
>>> import nltk
>>> from nltk.corpus import brown
>>> def process(sentence):
	for (w1,t1),(w2,t2),(w3,t3) in nltk.trigrams(sentence):
		if (t1.startswith('IN') and t2.startswith('DT') and t3.startswith('NN')):
			print w1,w2,w3

			
>>> for tagged_sent in brown.tagged_sents():
	process(tagged_sent)

of this city
of this money
of these funds
in each county
for some time
in this county
on this question
with any relatives
in this case
of that court
of this court
in these cases
on each worker
on that date
for each illness
of those millions
.....

# What is the ratio of masculine to feminine pronouns?
>>> import nltk
>>> ms = ['he', 'him', 'his', 'himself']
>>> fs = ['she', 'her', 'hers', 'herself']
>>> mc = 0.0
>>> fc = 0.0
>>> for (word,tag) in nltk.corpus.brown.tagged_words():
	if(tag[:2] == 'PP'):
		if(word.lower() in ms): mc += 1
		if(word.lower() in fs): fc += 1
		
>>> print '%i maskulina pronomen (%s)\n%i feminina pronomen (%s)\n\n%.2f maskulina pronomen per 1 feminint' % (mc,', '.join(ms),fc,', '.join(fs),mc/fc)
39524 maskulina pronomen (he, him, his, himself)
12074 feminina pronomen (she, her, hers, herself)

3.27 maskulina pronomen per 1 feminint		


