
import nltk
from nltk.corpus import brown
verbs=['adore', 'love', 'like', 'prefer']#spysok diyesliv za umovoyu
text=nltk.corpus.brown.tagged_words(categories='news')#zminniy text prusvoila vsi slova z katehorii news
kk=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL') and w[1][1].startswith('V')]#dlya zminnoi kk zadala umovy,sho vydaye spysok bigram sliv+tag
kk
kk=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL') and w[1][1].startswith('V') and w[1][0] in verbs]#dlya ziyei zh zminnoi pereviryla umovu chu prysutni slova zi spysku verbs
kk
#pereviryla tsu zh umovu dlya inshuh katehoriy
text=nltk.corpus.brown.tagged_words(categories='romance')
kk=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL') and w[1][1].startswith('V') and w[1][0] in verbs]
text=nltk.corpus.brown.tagged_words(categories='religion')
kk=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL') and w[1][1].startswith('V') and w[1][0] in verbs]
#shob perekonatyc' sho umova pratsuye, perevirymo chu znahodyt' inshi slova sho prysutna v tsiy katehorii
text=nltk.corpus.brown.tagged_words(categories='news')
kk=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL') and w[1][1].startswith('V') and w[1][0]=='operated']
print kk
#umova vykonuyet'sya,prosto diyesliv zi spysky verbs nemaye u daniy katehorii
