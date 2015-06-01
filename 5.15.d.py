
import nltk
from nltk.corpus import brown
taggedw=brown.tagged_words() # Зі слів корпусу Brown відбираємо ті у яких теги починаються з NN і робимо частотний аналіз
tags=[t for w,t in taggedw if t.startswith('NN')] 
fd=nltk.FreqDist(tags)
print fd.items()[10:]

# This tags are simple tags with modifiers.
# Each tag consists of a base tag and optional modifiers. 
# The modifiers include multiple tags separated by plus-signs (eg. EX+BEZ),
# multiple tags concatenated in the case of negation (eg. BEZ*),
# the prefix modifier FW- for foreign words (e.g. FW-JJ),
# the suffix modifier -NC for citations (e.g. NN-NC),
# the suffix -HL for words in headlines (e.g. NN-HL-TL in titles (e.g. NNS-TL).

