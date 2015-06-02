# Відкрити файли з позитивними і негативними словами
f1=open('C:/Users/Ira/Desktop/2015/positive.txt', encoding='utf-8')
f2=open('C:/Users/Ira/Desktop/2015/negative.txt', encoding='utf-8')
pos_w=[]
# Збереження позитивних слів у список
for i in f1.readlines():
	pos_w.append(i[:-1])
# Вивід на екран кількість позитивних слів	
print ('pos', len(pos_w))	
neg_w=[]
# Збереження негативних слів у список
for i in f2.readlines():
	neg_w.append(i[:-1])
# Вивід на екран кількість негативних слів
print ('neg', len(neg_w))
rez=[]
# Відкрити файли зі згенерованим словником
f3=open('C:/Users/Ira/Desktop/2015/rez_domen5.txt', encoding='utf-8')
# Збереження у список слів та їх тональності зі словника, якщо це слово
# є у списку позитивних слів 
for i in f3.readlines():
	#print (i.split(',')[0])
	if i.split(',')[0] in pos_w:
		#print (i.split(',')[0])
		rez.append(i.split(',')[:2])
# Вивід на екран кількості слів зі словника, які є серед позитивних слів
print ('rez', len(rez))
# Вивід на екран відношення кількості слів зі словника
# до кількості позитивних слів
print ('Recall_pos', len(rez)/len(pos_w))
# Відкриття і запис у файл слів зі словника, які є серед позитивних слів
z=open('C:/Users/Ira/Desktop/2015/pos_domen_rez5.txt','w')
for i in rez:
	z.write(str(i)+'\n')
z.close()
rez=[]
# Відкрити файли зі згенерованим словником
f3=open('C:/Users/Ira/Desktop/2015/rez_domen5.txt', encoding='utf-8')
# Збереження у список слів та їх тональності зі словника, якщо це слово
# є у списку негативних слів 
for i in f3.readlines():
	#print (i.split(',')[0])
	if i.split(',')[0] in neg_w:
		#print (i.split(',')[0])
		rez.append(i.split(',')[:2])
# Вивід на екран кількості слів зі словника, які є серед негативних слів		
print ('rez', len(rez))
# Вивід на екран відношення кількості слів зі словника
# до кількості негативних слів
print ('Recall_neg', len(rez)/len(neg_w))
# Відкриття і запис у файл слів зі словника, які є серед негативних слів
z=open('C:/Users/Ira/Desktop/2015/neg_domen_rez5.txt','w')
for i in rez:
	z.write(str(i)+'\n')
z.close()
		
	
