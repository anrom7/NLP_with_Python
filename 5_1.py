##5_1
import nltk
def tag_text(text):
	tokens=nltk.word_tokenize(text)
	tagged_words=nltk.pos_tag(tokens)#tag dlja kownogo slova
	return tagged_words

if __name__=='__main__':
    phrases=["British Left Waffles on Falkland Islands.","Juvenile Court to Try Shooting Defendant."]
    for ph in phrases:
        print "Phrase: %s" % (ph)
        print "Tagged words: %s" % (tag_text(ph))#show our results

