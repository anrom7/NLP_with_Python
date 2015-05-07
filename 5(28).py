#by Ivanna Rurych
#AL-12
#Chapter 5, Ex. 28
#task: Experiment with taggers using the simplified tagset (or make one of your own by discarding all but the first character of each tag name). Such a tagger has fewerdistinctions to make, but much less information on which to base its work. Discussyour findings.
import nltk 
with_simplified_tagset = nltk.corpus.brown.tagged_words(categories='news', simplify_tags=True) #Use the simplified tagset to the tagged Brown Corpus
word_tag_fd = nltk.FreqDist(with_simplified_tagset) # which of these tags are the most common in the 'news' category 
determiner=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('DT')] #Sort the Determiner which have the tag with the first letter 'DT' by frequency
print 'With simplified tagset %s\n'% determiner[:25] #Print the list of these pronouns with tags
without_simplified_tagset = nltk.corpus.brown.tagged_words(categories='news', simplify_tags=False) #Don't use the simplified tagset
word_tag_fd = nltk.FreqDist(without_simplified_tagset) # define the most common tags  in the 'nesw' category of the Brown Corpus, Don't use the simplified tagset
determiner1=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('DT')] #Once more sort the pronouns which have the tag with the first letter 'P' by frequency
print 'Without simplified tagset %s\n'% determiner1[:25] #Once more print the list of pronouns with tags
#do the same sorting the pronouns which have the tag with the first letter 'P' by frequency
with_simplified_tagset1 = nltk.corpus.brown.tagged_words(categories='news', simplify_tags=True)
word_tag_fd1 = nltk.FreqDist(with_simplified_tagset)
pronoun=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('P')]
print 'With simplified tagset %s\n'% pronoun[:25]
without_simplified_tagset = nltk.corpus.brown.tagged_words(categories='news', simplify_tags=False)
word_tag_fd1 = nltk.FreqDist(without_simplified_tagset)
pronoun1=[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('P')]
print 'Without simplified tagset %s\n'% pronoun1[:25]
#The 3th list of pronouns (with simplified tagset) contains except pronouns also prepositions. 
#The 4th list of pronouns (without simplified tagset) contains only prepositions. 
#So, the more complicated tagset is, the better and more correct results it gives.
 
