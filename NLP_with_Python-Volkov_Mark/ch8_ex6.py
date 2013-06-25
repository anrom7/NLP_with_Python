# error
#presented by Volkov Mark PRLc 11
# Chapter 8, Ex.6
+import nltk
+k = nltk.Tree (' (S (NP Ann) (VP cought (NP flu)))')
+def traverse (k):
+    try:                   # building a recursive funtion
+        k.node
+    except  Attribute Error :
+        print k,
+    else:
+        print '(', k.node,
+        for child in k:
+               traverse(child) # traversing a treebank 
+        print ')',
+print k.height()  # output
+nltk.Tree.draw (k)
+
