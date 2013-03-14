Python 2.6.6 (r266:84297, Aug 24 2010, 18:46:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 2.6.6      
>>> import nltk
>>> from nltk.corpus import brown
>>> patterns = [
    (r'.*ing$', 'VBG'), # gerund
    (r'.*ed$', 'VBP'), # simple past
    (r'.*es$', 'VB3'), # 3rd singular present
    (r'.*ould$', 'MD'), # modals
    (r'.*\'s$', 'NN$'), # possessive nouns
    (r'.*s$', 'NNP'), # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
    (r'.*', 'NN') # nouns 
    ]

>>> regexp_tagger = nltk.RegexpTagger(patterns)
>>> regexp_tagger.tag(brown.sents()[9])
[('The', 'NN'), ('City', 'NN'), ('Purchasing', 'VBG'), ('Department', 'NN'), (',', 'NN'), ('the', 'NN'), ('jury', 'NN'), ('said', 'NN'), (',', 'NN'), ('``', 'NN'), ('is', 'NNP'), ('lacking', 'VBG'), ('in', 'NN'), ('experienced', 'VBP'), ('clerical', 'NN'), ('personnel', 'NN'), ('as', 'NNP'), ('a', 'NN'), ('result', 'NN'), ('of', 'NN'), ('city', 'NN'), ('personnel', 'NN'), ('policies', 'VB3'), ("''", 'NN'), ('.', 'NN')]
>>> brown_test=brown.tagged_sents()[:100]
>>> print 'Regular expressions Tagger:'
Regular expressions Tagger:
>>> print 'Accuracy: %4.1f%%' % (
    100.0 * regexp_tagger.evaluate(brown.tagged_sents()[100:1000]))

Accuracy: 16.8%
>>> two_tagger=nltk.UnigramTagger(brown_test, backoff=regexp_tagger)
>>> print 'Regular expressions Tagger + Unigram tagger:'
Regular expressions Tagger + Unigram tagger:
>>> print 'Accuracy: %4.1f%%' % (
    100.0 * two_tagger.evaluate(brown.tagged_sents()[100:1000]))

Accuracy: 68.1%
>>> 
