#Viktoriia Palianytsia, AL-11, chapter 7, exercise 2
import nltk
sentence=[("many","JJ"),("researchers","NNS"),("two","CD"),("weeks","NNS"), ("both","DT"),("new","JJ"),("positions","NNS")] 
#Sentences that should be chunked.
chunk_grammar = "NP: {<DT>*<JJ>*<CD>*<NN.*>+}" #Define a simple grammar with a single regular expression rule
chunk_parser=nltk.RegexpParser(chunk_grammar) #Create a chunk parser
result=chunk_parser.parse(sentence) #Test chunk parser on our example sentence
print result  #The result is a tree, which we can either print, 
result.draw() #or display graphically
from nltk.corpus import conll2000 #Access the data of the CoNLL-2000 Chunking Corpus. The corpus contains 270k words of 
                                  #Wall Street Journal text, divided into “train” and “test” portions, annotated with 
								  #part-of-speech tags and chunk tags in the IOB format.
c_parser = nltk.RegexpParser(chunk_grammar) #Once more create a chunk parser
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP']) #We are interested in the NP chunks right now.  
                                                                     #So we can use the chunk_types argument to select them.
print c_parser.evaluate(test_sents) #Evaluate chunker on the data for testing
