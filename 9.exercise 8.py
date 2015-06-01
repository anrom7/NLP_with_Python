#Fedorchak V, ALs-11
#Chapter 9,Task 8

import nltk
#Write the feature structures
fs1 = nltk.FeatStruct("[T = ?s, R= [K = ?s]]")
fs2 = nltk.FeatStruct("[R = [L = l]]")
fs3 = nltk.FeatStruct("[R = [K = l]]")
fs4 = nltk.FeatStruct("[T = (1)[R = r], K->(1)]")
fs5 = nltk.FeatStruct("[T = (1)[L = ?s], K = [I -> (1), V = ?s] ]")
fs6 = nltk.FeatStruct("[T = [L = l]]") 
fs7 = nltk.FeatStruct("[T = [L = l], K = [V = [L = l]]]")
fs8 = nltk.FeatStruct("[T = (1)[L = ?s, Z = ?s], K = [R = ?s, I -> (1)] ]")
fs9 = nltk.FeatStruct("[T = [R = r], K = [I = [Z = i]]]")
fs10 = nltk.FeatStruct("[T = (1)[R = r], K -> (1)]")
# With the help of nltk check the results of structures unifications
print 'Unification of the 1st and 2d feature structure:', fs1.unify(fs2)
print 'Unification of the 1st and 3d feature structure:', fs1.unify(fs3)
print 'Unification of the 4th and 5th feature structure:', fs4.unify(fs5)
print 'Unification of the 5th and 6th feature structure:', fs5.unify(fs6)
print 'Unification of the 5th and 7th feature structure:', fs5.unify(fs7)
print 'Unification of the 8th and 9th feature structure:', fs8.unify(fs9)
print 'Unification of the 8th and 10th feature structure:', fs8.unify(fs10)
