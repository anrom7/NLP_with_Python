# vezdenko julia al-12  task8 chapter9
import nltk
# Entering the feature structures
fs1 = nltk.FeatStruct("[A = ?x, B= [C = ?x]]")
fs2 = nltk.FeatStruct("[B = [D = d]]")
fs3 = nltk.FeatStruct("[B = [C = d]]")
fs4 = nltk.FeatStruct("[A = (1)[B = b], C->(1)]")
fs5 = nltk.FeatStruct("[A = (1)[D = ?x], C = [E -> (1), F = ?x] ]")
fs6 = nltk.FeatStruct("[A = [D = d]]") 
fs7 = nltk.FeatStruct("[A = [D = d], C = [F = [D = d]]]")
fs8 = nltk.FeatStruct("[A = (1)[D = ?x, G = ?x], C = [B = ?x, E -> (1)] ]")
fs9 = nltk.FeatStruct("[A = [B = b], C = [E = [G = e]]]")
fs10 = nltk.FeatStruct("[A = (1)[B = b], C -> (1)]")
# Checking the results of the feature structures unifications with nltk
print 'Unification of the 1st and 2d feature structure:', fs1.unify(fs2)
print 'Unification of the 1st and 3d feature structure:', fs1.unify(fs3)
print 'Unification of the 4th and 5th feature structure:', fs4.unify(fs5)
print 'Unification of the 5th and 6th feature structure:', fs5.unify(fs6)
print 'Unification of the 5th and 7th feature structure:', fs5.unify(fs7)# These two feature structures won't unify
print 'Unification of the 8th and 9th feature structure:', fs8.unify(fs9)
print 'Unification of the 8th and 10th feature structure:', fs8.unify(fs10)
