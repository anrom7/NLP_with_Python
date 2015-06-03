#Iryna Kupyak, PRLs-12, chapter 9, exercise 8
import nltk
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
print 'fs1 and fs2'
print fs1.unify(fs2) #здійснюємо функцію уніфікації до заданих структур та виводимо на екран
print '-------------------------------------'
print 'fs1 and fs3'
print fs1.unify(fs3)
print '-------------------------------------'
print 'fs4 and fs5'
print fs4.unify(fs5)
print '-------------------------------------'
print 'fs5 and fs6'
print fs5.unify(fs6)
print '-------------------------------------'
print 'fs5 and fs7'
print fs5.unify(fs7)
print '-------------------------------------'
print 'fs8 and fs9',
print fs8.unify(fs9)
print '-------------------------------------'
print 'fs8 and fs10'
print fs8.unify(fs10)


