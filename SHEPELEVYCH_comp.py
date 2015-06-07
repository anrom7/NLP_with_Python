Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
# Відкрити файли з позитивними і негативними словами
>>> f1=open('E:\КУРСОВА КЛ\positive1.txt', encoding='utf-8')
>>> f2=open('E:/КУРСОВА КЛ/negative1.txt', encoding='utf-8')
>>> f_neutr=open('E:/КУРСОВА КЛ/neutral.txt', encoding='utf-8')
# кількість всіх слів
>>> w_count = 0
# Збереження нейтральних слів у список
>>> neutr_w=[]
>>> for i in f_neutr.readlines():
    neutr_w.append(i[:-1])

    
>>> print ('neutr', len(neutr_w)) # Вивід на екран кількість негативних слів
neutr 421
>>> w_count += len(neutr_w)
>>> pos_w=[]
# Збереження позитивних слів у список
>>> for i in f1.readlines():
	 pos_w.append(i[:-1])

# Вивід на екран кількість позитивних слів	 
>>> print ('pos', len(pos_w))

pos 142
>>> w_count += len(pos_w)
>>> neg_w=[]
# Збереження негативних слів у список
>>> for i in f2.readlines():
    neg_w.append(i[:-1])

# Вивід на екран кількість негативних слів    
>>> print ('neg', len(neg_w))
neg 58
>>> w_count += len(neg_w)
>>> print ('w_count ' + str(w_count))
w_count 621
>>> rez=[]
# Відкрити файли зі згенерованим словником
>>> f3=open('E:/КУРСОВА КЛ/rez_domen5.txt', encoding='utf-8')
# Збереження у список слів та їх тональності зі словника, якщо це слово
# є у списку позитивних слів
>>> for i in f3.readlines():
    #print (i.split(',')[0])
    if i.split(',')[0] in neutr_w:
        #print (i.split(',')[0])
        rez.append(i.split(',')[:2])

 # Вивід на екран кількості слів зі словника, які є серед позитивних слів       
>>> print ('rez_neutral', len(rez))
rez_neutral 1
>>> print ('Precision_neutral', len(rez)/w_count )
Precision_neutral 0.001610305958132045
# Вивід на екран відношення кількості слів зі словника
# до кількості позитивних слів
>>> print ('Recall_neutr', len(rez)/len(neutr_w))
Recall_neutr 0.0023752969121140144
>>> rez=[]
# Відкрити файли зі згенерованим словником
>>> f3=open('E:/КУРСОВА КЛ/rez_domen5.txt', encoding='utf-8')
# Збереження у список слів та їх тональності зі словника, якщо це слово
# є у списку позитивних слів
>>> for i in f3.readlines():
    #print (i.split(',')[0])
    if i.split(',')[0] in pos_w:
        #print (i.split(',')[0])
        rez.append(i.split(',')[:2])

 # Вивід на екран кількості слів зі словника, які є серед позитивних слів       
>>> print ('rez_pos', len(rez))
rez_pos 35
# Вивід на екран відношення кількості слів зі словника
# до кількості позитивних слів
>>> print ('Recall_pos', len(rez)/len(pos_w))
Recall_pos 0.24647887323943662
>>> print ('Precision_pos', len(rez)/w_count )
Precision_pos 0.05636070853462158
# Відкриття і запис у файл слів зі словника, які є серед позитивних слів
>>> z=open('E:/КУРСОВА КЛ/pos_domen_rez5.txt','w')
>>> for i in rez:
    z.write(str(i)+'\n')

    
21
20
17
20
17
22
17
16
14
18
18
19
18
18
17
16
16
17
15
14
15
21
14
20
16
16
20
17
15
19
17
18
18
17
17
>>> z.close()
>>> rez=[]
# Відкрити файли зі згенерованим словником
>>> f3=open('E:/КУРСОВА КЛ/rez_domen5.txt', encoding='utf-8')
# Збереження у список слів та їх тональності зі словника, якщо це слово
# є у списку негативних слів
>>> for i in f3.readlines():
    #print (i.split(',')[0])
    if i.split(',')[0] in neg_w:
        #print (i.split(',')[0])
        rez.append(i.split(',')[:2])

 # Вивід на екран кількості слів зі словника, які є серед негативних слів       
>>> print ('rez_neg', len(rez))
rez_neg 18
# Вивід на екран відношення кількості слів зі словника
# до кількості негативних слів
>>> print ('Recall_neg', len(rez)/len(neg_w))
Recall_neg 0.3103448275862069
>>> print ('Precision_neg', len(rez)/w_count )
Precision_neg 0.028985507246376812
#Відкриття і запис у файл слів зі словника, які є серед негативних слів
>>> z=open('E:/КУРСОВА КЛ/neg_domen_rez5.txt','w')
>>> for i in rez:
    z.write(str(i)+'\n')

    
16
14
19
21
16
19
13
16
16
14
15
12
18
23
15
18
18
18
>>> z.close()
>>> 
