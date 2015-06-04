# Точність та повнота
# Світлана Синиця

# Відкриваю файли
f1=open('C:\\Users\\Admin\\Downloads\\New file\\positive.txt') # позитивні слова
f2=open('C:\\Users\\Admin\\Downloads\\New file\\negative.txt') # негативні слова
f3=open('C:\\Users\\Admin\\Downloads\\New file\\neutral.txt') # нейтральні слова
f4=open('C:\\Users\\Admin\\Downloads\\New file\\Synytsia_seedwords.txt') # всі слова разом

# Збереження позитивних слів у список
pos_w=[]
for i in f1.readlines():
	pos_w.append(i[:-1])	
print ('pos', len(pos_w)) # Вивід на екран кількість позитивних слів

# Збереження негативних слів у список
neg_w=[]
for i in f2.readlines():
	neg_w.append(i[:-1])
print ('neg', len(neg_w)) # Вивід на екран кількість негативних слів

# Збереження нейтральних слів у список
neutr_w=[]
for i in f3.readlines():
	neutr_w.append(i[:-1])
print ('neutr', len(neutr_w)) # Вивід на екран кількість негативних слів

# Вивід всіх слів разом
gen_w=[]
for i in f4.readlines():
        gen_w.append(i[:-1])
print ('gen', len(gen_w)) # Вивід всіх слів на екран                    

# рахую повноту
print('recall_pos', len(pos_w)/float(len(gen_w))) # повнота позитивних
print('recall_neg', len(neg_w)/float(len(gen_w))) # повнота негативних
print('recall_neutr', len(neutr_w)/float(len(gen_w))) # повнота нейтральних


# Підрахунок загальної кількості слів у словнику
gen_dict=[]
with open('C:\\Users\\Admin\\Downloads\\New file\\rez_domen5.txt') as f:
       for i in f.readlines():
               gen_dict.append(i[:-1])
print ('gen_dict', len(gen_dict)) # Вивід всіх слів на екран


# Рахую загальну точність
print ("preciseness_gen", len(gen_w)/float(len(gen_dict)))

# Результати
'''
('pos', 210)
('neg', 125)
('neutr', 442)
('gen', 777)
('recall_pos', 0.2702702702702703)
('recall_neg', 0.16087516087516088)
('recall_neutr', 0.5688545688545689)
('gen_dict', 46417)
('preciseness_gen', 0.016739556627959583)
'''
