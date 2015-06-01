import nltk
#Create a matrix as a list of lists in Python, and initialize 
#it with the lexical categories of each token in the init_wfst() function
def init_wfst(tokens, grammar):
    numtokens = len(tokens)
    wfst = [[None for i in range(numtokens+1)] for j in range(numtokens+1)]
    for i in range(numtokens):
        print i
        productions = grammar.productions(rhs=tokens[i])
        print productions
        wfst[i][i+1] = productions[0].lhs()
    return wfst
#Sentence and grammar
tokens = "I shot an elephant in my pajamas".split() 
groucho_grammar = nltk.parse_cfg("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")
wfst0 = init_wfst(tokens, groucho_grammar)
#A function which completes cells in the WFST
def complete_wfst(wfst, tokens, grammar, trace=False):
    index = dict((p.rhs(), p.lhs()) for p in grammar.productions()) #A list where the left and right 
	                                                                #sides of all grammar rules are written
    numtokens = len(tokens) #The number of words in the sentence
    for span in range(2, numtokens+1):
        for start in range(numtokens+1-span):
            end = start + span
            for mid in range(start+1, end):
                nt1, nt2 = wfst[start][mid], wfst[mid][end] #The elements of the initial completed matrix
                if nt1 and nt2 and (nt1,nt2) in index:
                    wfst[start][end] = index[(nt1,nt2)]
                    if trace:
                        print "[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" % \
(start, nt1, mid, nt2, end, start, index[(nt1,nt2)], end)
    return wfst
#By setting trace to True when calling the function complete_wfst(), we see tracing 
#output that shows the WFST being constructed
def complete_wfst(wfst, tokens, grammar, trace=True):
    index = dict((p.rhs(), p.lhs()) for p in grammar.productions())
    numtokens = len(tokens)
    for span in range(2, numtokens+1):
        for start in range(numtokens+1-span):
            end = start + span
            for mid in range(start+1, end):
                nt1, nt2 = wfst[start][mid], wfst[mid][end]
                if nt1 and nt2 and (nt1,nt2) in index:
                    wfst[start][end] = index[(nt1,nt2)]
                    if trace:
                        print "[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" % \
(start, nt1, mid, nt2, end, start, index[(nt1,nt2)], end)
    return wfst
#Define a utility function display() to pretty-print the WFST
def display(wfst, tokens):
    print '\nWFST ' + ' '.join([("%-4d" % i) for i in range(1, len(wfst))])
    for i in range(len(wfst)-1):
        print "%d " % i,
        for j in range(1, len(wfst)):
            print "%-4s" % (wfst[i][j] or '.'),
        print
display(wfst0, tokens)
wfst1 = complete_wfst(wfst0, tokens, groucho_grammar)
display(wfst1, tokens)
#In WFST we didn't use any parsng functions, but we have built what is basicly a primitive chart parser . 
#WFST is limited, it's not a true parser and is inadequate to solve problems of ambiguities with PP (prepositional phrases).
