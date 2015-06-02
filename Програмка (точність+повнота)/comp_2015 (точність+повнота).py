def space2underline(word):
	""" Замінити всі пробіли на підкреслення"""
	word2 = ""
	# Замінити всі пробіли на підкреслення
	for ch in word:
		if ch == " ":
			ch = "_"
		word2 +=ch        
	return word2

# Відкрити файли з позитивними і негативними словами
f1=open('C:/Users/Ira/Desktop/2015/positive.txt', encoding='utf-8')
f2=open('C:/Users/Ira/Desktop/2015/negative.txt', encoding='utf-8')
pos_w=[]
# Збереження позитивних слів у список
for i in f1.readlines():
	pos_w.append(space2underline(i[:-1]))
# Вивід на екран кількість позитивних слів	
print ('pos', len(pos_w))	
neg_w=[]
# Збереження негативних слів у список
for i in f2.readlines():
	neg_w.append(space2underline(i[:-1]))
# Вивід на екран кількість негативних слів
print ('neg', len(neg_w))
pos=[]
neg=[]
# Відкрити файли зі згенерованим словником
f3=open('C:/Users/Ira/Desktop/2015/rez_domen5.txt', encoding='utf-8')
# Збереження у список слів та їх тональності зі словника, якщо це слово
# є у списку позитивних слів чи негативних слів
for i in f3.readlines():
	#print (i.split(',')[0])
	if i.split(',')[0] in pos_w:
		#print (i.split(',')[0])
		pos.append(i.split(',')[:2])
	if i.split(',')[0] in neg_w:
		#print (i.split(',')[0])
		neg.append(i.split(',')[:2])
# Вивід на екран кількості слів зі словника, які є серед позитивних слів
print ('pos in dict', len(pos))
# Вивід на екран відношення кількості слів зі словника
# до кількості позитивних слів
print ('Recall_pos', len(pos)/len(pos_w))
# Відкриття і запис у файл слів зі словника, які є серед позитивних слів
z=open('C:/Users/Ira/Desktop/2015/pos_domen_rez5.txt','w')
for i in pos:
	z.write(str(i)+'\n')
z.close()
# Вивід на екран кількості слів зі словника, які є серед негативних слів		
print ('neg in dict', len(neg))
# Вивід на екран відношення кількості слів зі словника
# до кількості негативних слів
print ('Recall_neg', len(neg)/len(neg_w))
# Відкриття і запис у файл слів зі словника, які є серед негативних слів
z=open('C:/Users/Ira/Desktop/2015/neg_domen_rez5.txt','w')
for i in neg:
	z.write(str(i)+'\n')
z.close()

# точність / повнота (240 ст.)
		
	
