d1['I'] = 'PRP'
d1['read'] = 'VBP'
d1['book'] = 'NN'
# Adding entries to d1.
d2 = {}
d2['red'] = 'VBD'
d2['one'] = 'CD'
# Adding entries to d2.
print(d1)
print(d2)
d1.update(d2)
print(d1)
# Adding d2 items to d1.
