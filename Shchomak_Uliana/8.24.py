# Уляна Щомак ПРЛс-12 

import nltk
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
answer_list=[]
answer_list.insert(0,t.node)
def rec_tree(tree1): #будуємо рекурсивну функцію
    small_list=[]
    if not tree1.height()>3: # перевіряємо висоту дерева
        if tree1.height()<3:
            small_list.insert(0,tree1.node) # вставляємо в субліст
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
for tree in t:# записуємо дерево у зворотньому порядку
    answer_list.insert(0,rec_tree(tree))
    print answer_list #вивід рекурсивного дерева
    t.draw()# виводимо звичайний розбір речення для порівняння
