#Chapter 5
#Exercise 23
#Author Sofiya Zaliska ALs-11
#Consider the regular expression tagger developed in the exercises in the previous
#section. Evaluate the tagger using its accuracy() method, and try to come up with
#ways to improve its performance. Discuss your findings. How does objective evaluation
#help in the development process?
import nltk
from nltk.corpus import brown
patterns = [
    (r'.*ing$', 'VBG'), # gerund
    (r'.*ed$', 'VBP'), # simple past
    (r'.*es$', 'VB3'), # 3rd singular present
    (r'.*ould$', 'MD'), # modals
    (r'.*\'s$', 'NN$'), # possessive nouns
    (r'.*s$', 'NNP'), # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
    (r'.*', 'NN') # nouns
    ]
regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown.sents()[4])
[('The', 'NN'), ('jury', 'NN'), ('said', 'NN'), ('it', 'NN'), ('did', 'NN'), ('find', 'NN'),
 ('that', 'NN'), ('many', 'NN'), ('of', 'NN'), ("Georgia's", 'NN$'), ('registration', 'NN'),
 ('and', 'NN'), ('election', 'NN'), ('laws', 'NNP'), ('``', 'NN'), ('are', 'NN'),
 ('outmoded', 'VBP'), ('or', 'NN'), ('inadequate', 'NN'), ('and', 'NN'), ('often', 'NN'), ('ambiguous', 'NNP'), ("''", 'NN'), ('.', 'NN')]
brown_test=brown.tagged_sents()[:100]
print 'Regular expressions Tagger:'
print 'Accuracy: %4.1f%%' % (100.0 * regexp_tagger.evaluate(brown.tagged_sents()[100:1000]))
#Accuracy: 16.8%

two_tagger=nltk.UnigramTagger(brown_test, backoff=regexp_tagger)
print 'Regular expressions Tagger + Unigram tagger:'
print 'Accuracy: %4.1f%%' % (100.0 * two_tagger.evaluate(brown.tagged_sents()[100:1000]))
#Accuracy: 67.9%
# objective evaluation helps to improve our investigations