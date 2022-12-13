list = ['Hello', 'How are you']
list2 = ['Sir', 'Madam']
list3 = []   # Empty list
# Hello Sir Hello Madam Goodafternoon Sir Goodafternoon Madam
for i in list:
    for j in list2:
        list3.append(i + ' ' + j)
print(list3)