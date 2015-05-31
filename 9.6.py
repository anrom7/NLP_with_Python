#Shepelevych PRLs-11
#
#9_6. Develop a feature-based grammar that will correctly describe the following
#Spanish noun phrases:
#(59) un cuadro hermos-o
#INDEF.SG.MASC picture beautiful-SG.MASC
#‘a beautiful picture’
#(60) un-os cuadro-s hermos-os
#INDEF-PL.MASC picture-PL beautiful-PL.MASC
#‘beautiful pictures’
#(61) un-a cortina hermos-a
#INDEF-SG.FEM curtain beautiful-SG.FEM
#‘a beautiful curtain’
#(62) un-as cortina-s hermos-as
#INDEF-PL.FEM curtain beautiful-PL.FEM
#‘beautiful curtains’


import nltk
from nltk import load_parser
#some spanish phrases 
token1 = 'un cuadro hermoso'.split()
token2 = 'unos cuadros hermosos'.split()
#define chart parser
cp = load_parser('grammars/book_grammars/spanish_new.fcfg', trace=2)
"""for tree in cp.nbest_parse(tokens):
     print tree"""
#results
tree1 = cp.nbest_parse(token1)
tree2 = cp.nbest_parse(token2)


"""
Spanish grammar

% start S
# Grammar Productions
S -> NP[CASE=nom, AGR=?a] 
NP[CASE=?c, AGR=?a] ->N[CASE=?c, AGR=?a] Adj[AGR=?a] 
NP[CASE=?c, AGR=?a] -> Det[CASE=?c, AGR=?a] N[CASE=?c, AGR=?a] Adj[AGR=?a]
# Lexical Productions
# masc
Det[CASE=indef, AGR=[GND=masc,NUM=sg]] -> 'un'
# fem
Det[CASE=indef, AGR=[GND=fem,NUM=sg]] -> 'una'
# Plural determiners
Det[CASE=indef, AGR=[ GND=masc , NUM=pl]] -> 'unos'
Det[CASE=indef, AGR=[ GND=fem, NUM=pl]] -> 'unas'
# Nouns
N[CASE=indef, AGR=[GND=masc,NUM=sg]] -> 'cuadro'
N[CASE=indef, AGR=[GND=masc,NUM=pl]] -> 'cuadros'
N[CASE=indef, AGR=[GND=fem,NUM=sg]] -> 'cortina'
N[CASE=indef, AGR=[GND=fem,NUM=pl]] -> 'cortinas'
# Adj
Adj[AGR=[GND=masc,NUM=sg]] -> 'hermoso'
Adj[AGR=[GND=masc,NUM=pl]] -> 'hermosos'
Adj[AGR=[GND=fem,NUM=sg]] -> 'hermosa'
Adj[AGR=[GND=fem,NUM=pl]] -> 'hermosas'

"""
