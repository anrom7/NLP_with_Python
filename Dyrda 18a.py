import nltk,re,pprint
t= nltk.corpus.brown.tagged_words()
st=nltk.ConditionalFreqDist((word.lower(),tag) for (word,tag) in t)
vse=0
zz=0
for w in st.conditions():
    if len (st[w])==1:
        zz+=1
        vse+=1
print zz*100/vse
