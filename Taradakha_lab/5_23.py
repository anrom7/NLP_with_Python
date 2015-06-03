# Taradakha K 5_23

import nltk
from nltk.corpus import brown
patterns = [
    (r'.*ing$', 'VBG'), # gerunds
    (r'.*ed$', 'VBD'), # simple past
    (r'.*es$', 'VBZ'), # 3rd singular present
    (r'.*ould$', 'MD'), # modals
    (r'.*\'s$', 'NN$'), # possessive nouns
    (r'.*s$', 'NNS'), # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
    (r'.*', 'NN') # nouns (default)
    ]
regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown.sents()[10])
print regexp_tagger.tag(brown.sents()[10]) #sentence
brown_test=brown.tagged_sents()[:50]
100.0 * regexp_tagger.evaluate(brown.tagged_sents()[50:500])
print 100.0 * regexp_tagger.evaluate(brown.tagged_sents()[50:500]) #Accuracy of Regular expressions Tagger
two_tagger=nltk.UnigramTagger(brown_test, backoff=regexp_tagger)
100.0 * two_tagger.evaluate(brown.tagged_sents()[50:500])
print 100.0 * two_tagger.evaluate(brown.tagged_sents()[50:500]) #Accuracy of Regular expressions Tagger + Unigram tagger
