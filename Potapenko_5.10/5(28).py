import nltk
#Use the simplified tagset to the tagged Brown Corpus
with_simplified_tagset = nltk.corpus.brown.tagged_words(categories='editorial', simplify_tags=True) 
#Define which of these tags are the most common in the 'editorial' category of the Brown Corpus
word_tag_fd = nltk.FreqDist(with_simplified_tagset) 
#Sort the pronouns which have the tag with the first letter 'P' by frequency
pronoun=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('P')] 
#Print the list of these pronouns with tags
print 'With simplified tagset %s\n'% pronoun[:20] 
#The simplified tagset is not used
without_simplified_tagset = nltk.corpus.brown.tagged_words(categories='editorial', simplify_tags=False) 
#Once more define the most common tags  in the 'editorial' category of the Brown Corpus
word_tag_fd = nltk.FreqDist(without_simplified_tagset) 
#Once more sort the pronouns which have the tag with the first letter 'P' by frequency
pronoun1=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('P')] 
#Once more print the list of pronouns with tags
print 'Without simplified tagset %s\n'% pronoun1[:20] 
#The first list of pronouns (with simplified tagset) contains except pronouns also prepositions. 
#The second list of pronouns (without simplified tagset) contains only prepositions. 
#So, the more complicated tagset is, the better and more correct results it gives.
 
