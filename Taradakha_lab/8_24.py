#Taradakha K 8_24
import nltk
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0] # Taking out the sentence we will work on
answer_list=[]
answer_list.insert(0,t.node)

def rec_tree(tree1): # Building a recursive function
    small_list=[]
    if not tree1.height()>3: # Checkig the heigth of the tree
        if tree1.height()<3:
            small_list.insert(0,tree1.node) # Inserting into sub-list
        else:
            small_list2=[]
            small_list.insert(0,tree1.node)
            for i in tree1:
                small_list2.insert(0,i.node) 
            small_list.insert(0,small_list2)
    else:
        small_list3=[]
        small_list.insert(0,tree1.node)
        for i in tree1:
            small_list3.insert(0,rec_tree(i))
        small_list.insert(0,small_list3)
    return small_list


for tree in t: # Wrigting down trees in backwards order
	answer_list.insert(0,rec_tree(tree))

print answer_list # Printing out recursive tree
t.draw() # Drawing the normal parsed sentense to compare
