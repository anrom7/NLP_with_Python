# Pushchinska_Iryna PRLs-11
# Chapter_10, Task_1

#a)If Angus sings, it is not the case that Bertie sulks.
import nltk
lp = nltk.LogicParser()
AnS= lp.parse('AnS')
BeS= lp.parse('-BeS')
A= lp.parse('AnS & -BeS')
prover = nltk.Prover9()
print prover.prove(AnS, [A])

#b)Cyril runs and barks.
import nltk
lp = nltk.LogicParser()
CR=lp.parse('CR')
CB=lp.parse('CB')
B=lp.parse('CR & CB')
prover = nltk.Prover9()
print prover.prove(CB, [B])

#c)It will snow if it doesn’t rain.
import nltk
lp = nltk.LogicParser()
Snow=lp.parse('S')
Rain=lp.parse('-R')
Cond=lp.parse('S -> -R')
prover = nltk.Prover9()
print prover.prove(Rain, [Cond, Snow])

#d)It’s not the case that Irene will be happy if Olive or Tofu comes.
import nltk
lp = nltk.LogicParser()
InbH=lp.parse('-IwbH')
OoTc=lp.parse('OoTc')
Irene=lp.parse('-IwbH -> OoTc')
prover = nltk.Prover9()
print prover.prove(OoTc, [InbH, Irene])

#e)Pat didn’t cough or sneeze.
import nltk
lp = nltk.LogicParser()
Sneeze=lp.parse('-S')
Cough=lp.parse('-C')
Pat=lp.parse('-S | -C')
prover = nltk.Prover9()
print prover.prove(Pat, [Cough, Sneeze])

#f)If you don’t come if I call, I won’t come if you call.
import nltk
lp = nltk.LogicParser()
First=lp.parse('-A -> B')
Second=lp.parse('-C -> D')
End=lp.parse('(-A -> B)<->(-C -> D)')
prover = nltk.Prover9()
print prover.prove(End, [First, Second])
