## Khrystyna Maschakevich, AL-13, Chapter 7, Task 10. The task was to study errors of
## bigram chunker and experiment with trigram chunker
import nltk
#import nltk.chunk
from nltk.corpus import conll2000 ##contains three chunk types: NP chunks; VP chunks; and PP chunks
cp = nltk.RegexpParser("") ## uses a set of regular expression patterns to specify the behavior of the parser
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
## as we are interested in the NP chunks right now, we can use the chunk_types argument to select them
## we can get evalueted results using - print cp.evaluate(test_sents)

grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar) ## use the above mentioned  grammar
print cp.evaluate(test_sents)

class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):  
## a constructor , which is called when we build a new UnigramChunker
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.BigramChunker(train_data) 
##  we simply change the class name to BigramChunker, and modify line to construct a BigramTagger rather than a UnigramTagger

    def parse(self, sentence): 
##  the parse method , which is used to chunk new sentences.
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)  

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
bigram_chunker = BigramChunker(train_sents)
## we can get the results of bigram chunker using - print bigram_chunker.evaluate(test_sents)             	