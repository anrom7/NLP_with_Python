#by Ivanna Rurych, AL-12
#chapter 5, Ex.3
#task:Tokenize and tag the following sentence:  They wind back the clock, while we chase  after  the  wind.  What  different  pronunciations  and  parts-of-speech  are involved?
import nltk
sent=nltk.word_tokenize("They wind back the clock, while we chase  after  the  wind")#tokenize the sentence
tagged=nltk.pos_tag(sent) #tag the sentence
cfd1 = nltk.ConditionalFreqDist(tagged)#find the same word, which belongs to different parts-of-speech
word1=cfd1['wind']
print tagged, word1
