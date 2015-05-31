# Pushchinska_Iryna PRLs-11
# Chapter_9, Task_5

S -> NP[CASE=nom, AGR=?a] VP[AGR=?a]
NP[CASE=?c, AGR=?a] -> PRO[CASE=?c, AGR=?a]
NP[CASE=?c, AGR=?a] -> Det[CASE=?c, AGR=?a] N[CASE=?c, AGR=?a]
VP[AGR=?a] -> V[AGR=?a]
VP[AGR=?a] -> V[OBJCASE=?c, AGR=?a] NP[CASE=?c]
# Lexical Productions
# Singular determiners
# masc
Det[CASE=nom, AGR=[GND=masc,PER=3,NUM=sg]] -> 'der'
Det[CASE=dat, AGR=[GND=masc,PER=3,NUM=sg]] -> 'dem'
Det[CASE=acc, AGR=[GND=masc,PER=3,NUM=sg]] -> 'den'
Det[CASE=gen, AGR=[GND=masc,PER=3,NUM=sg]] -> 'des'
# fem
Det[CASE=nom, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'
Det[CASE=dat, AGR=[GND=fem,PER=3,NUM=sg]] -> 'der'
Det[CASE=acc, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'
Det[CASE=gen, AGR=[GND=fem,PER=3,NUM=sg]] -> 'der'
# neu
Det[CASE=nom, AGR=[GND=neu,PER=3,NUM=sg]] -> 'das'
Det[CASE=dat, AGR=[GND=neu,PER=3,NUM=sg]] -> 'dem'
Det[CASE=acc, AGR=[GND=neu,PER=3,NUM=sg]] -> 'das'
Det[CASE=gen, AGR=[GND=neu,PER=3,NUM=sg]] -> 'des'
# Plural determiners
Det[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'die'
Det[CASE=dat, AGR=[PER=3,NUM=pl]] -> 'den'
Det[CASE=acc, AGR=[PER=3,NUM=pl]] -> 'die'
Det[CASE=gen, AGR=[PER=3,NUM=pl]] -> 'der'
# Nouns
N[AGR=[GND=masc,PER=3,NUM=sg]] -> 'Hund'
N[CASE=nom, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunde'
N[CASE=dat, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunden'
N[CASE=acc, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunde'
N[AGR=[GND=fem,PER=3,NUM=sg]] -> 'Katze'
N[AGR=[GND=fem,PER=3,NUM=pl]] -> 'Katzen'
# Pronouns
PRO[CASE=nom, AGR=[PER=1,NUM=sg]] -> 'ich'
PRO[CASE=acc, AGR=[PER=1,NUM=sg]] -> 'mich'
PRO[CASE=dat, AGR=[PER=1,NUM=sg]] -> 'mir'
PRO[CASE=nom, AGR=[PER=2,NUM=sg]] -> 'du'
PRO[CASE=nom, AGR=[PER=3,NUM=sg]] -> 'er' | 'sie' | 'es'
PRO[CASE=nom, AGR=[PER=1,NUM=pl]] -> 'wir'
PRO[CASE=acc, AGR=[PER=1,NUM=pl]] -> 'uns'
PRO[CASE=dat, AGR=[PER=1,NUM=pl]] -> 'uns'
PRO[CASE=nom, AGR=[PER=2,NUM=pl]] -> 'ihr'
PRO[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'sie'
# Verbs
V[AGR=[ SUBCAT=intrans ,NUM=sg,PER=1]] -> 'komme'
V[AGR=[ SUBCAT=intrans ,NUM=sg,PER=2]] -> 'kommst'
V[AGR=[ SUBCAT=intrans ,NUM=sg,PER=3]] -> 'kommt'
V[AGR=[ SUBCAT=intrans ,NUM=pl, PER=1]] -> 'kommen'
V[AGR=[ SUBCAT=intrans ,NUM=pl, PER=2]] -> 'kommt'
V[AGR=[ SUBCAT=intrans ,NUM=pl, PER=3]] -> 'kommen'
V[AGR=[ SUBCAT=trans ,NUM=sg,PER=1]] -> 'sehe' | 'mag'
V[AGR=[ SUBCAT=trans, NUM=sg,PER=2]] -> 'siehst' | 'magst'
V[AGR=[ SUBCAT=trans, NUM=sg,PER=3]] -> 'sieht' | 'mag'
V[AGR=[ SUBCAT=trans, NUM=pl,PER=1]] -> 'sehen' | 'mögen'
V[AGR=[ SUBCAT=trans, NUM=pl,PER=2]] -> 'sieht' | 'mögt'
V[AGR=[ SUBCAT=trans, NUM=pl,PER=3]] -> 'sehen' | 'mögen'
V[AGR=[ SUBCAT=trans, NUM=sg,PER=1]] -> 'folge' | 'helfe'
V[AGR=[ SUBCAT=trans, NUM=sg,PER=2]] -> 'folgst' | 'hilfst'
V[AGR=[ SUBCAT=trans, NUM=sg,PER=3]] -> 'folgt' | 'hilft'
V[AGR=[ SUBCAT=trans, NUM=pl,PER=1]] -> 'folgen' | 'helfen'
V[AGR=[ SUBCAT=trans, NUM=pl,PER=2]] -> 'folgt' | 'helft'
V[AGR=[ SUBCAT=trans, NUM=pl,PER=3]] -> 'folgen' | 'helfen'


