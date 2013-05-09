import nltk
from nltk.corpus import brown
brown_reviews=brown.tagged_sents(categories='reviews') #returns a list of tagged sentences
brown_sents=brown.sents(categories='reviews') # and have pure sents without tags
unigram_tagger=nltk.UnigramTagger(brown_reviews) # build unigram tagger
print unigram_tagger.tag(brown_sents[3]) # check 3rd sentence
print unigram_tagger.evaluate(brown_reviews) # evaluation

print 'there is no untagged word in this sentence, but this might happen when the tagger has not seen the word before so this word will receive tag of None'
