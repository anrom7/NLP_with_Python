## Khrystyna Maschakevich, AL-13, Chapter 7, Task 8. The task was to develop chunker
## with the help of regular expressions on the basis of RegexpChunk grammar.
import nltk
from nltk.corpus import conll2000 ##contains three chunk types: NP chunks; VP chunks; and PP chunks
cp = nltk.RegexpParser("") ## uses a set of regular expression patterns to specify the behavior of the parser
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])## as we are interested in the NP chunks right now, we can use the chunk_types argument to select them
## to evaluate the results we can use -print cp.evaluate(test_sents), 
## and get get following results
## ChunkParse score:
## IOB Accuracy:  43.4%
## Precision:      0.0%
## Recall:         0.0%
## F-Measure:      0.0%
