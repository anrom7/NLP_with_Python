# Anna Karbivska, ALs-11
#9.6.3
#Write a function subsumes() that holds of two feature structures fs1 and fs2 just
#in case fs1 subsumes fs2.

import nltk
fs1 = nltk.FeatStruct(Category="Chas")
fs2 = nltk.FeatStruct(Category="Chas", Other_Category='Misce')# Defining the features
print fs1.subsumes(fs2) # Subsuming the features
