import nltk
fs0 = nltk.FeatStruct("[A=?x, B=?x]")
fs1 = nltk.FeatStruct(A='b')
fs2 = nltk.FeatStruct(B='5')
fs3 = fs2.unify(fs1) #Unify feature structure 2 with feature structure 1
print fs3
print fs2.subsumes(fs3) #Feature structure 2 subsumes feature structure 3
fs4 = fs1.unify(fs0) #Unify feature structure 1 with feature structure 0
print fs4
print fs1.subsumes(fs4) #Feature structure 1 subsumes feature structure 4
fs5 = fs4.unify(fs3) #Can't unify feature structure 4 with feature structure 3
print fs5 #The result is - 'None'
print fs1.subsumes(fs5) #Error, because feature structure 5 does not exist
