emptylist = []
ind = []
data = 3
stringlist_1 = ['T', 'u', 'r', 't', 'l', 'e']
stringlist_2 = ['P', 'o', 'i', 'n', 't']
print(stringlist_1, stringlist_2)
sumlist = [count1+count2 for count1 in stringlist_1 if count1 == 'T' for count2 in stringlist_2 if count2 != 'o' and count2 != 'i' ]
print(sumlist)
emptylist.append(sumlist)
print("Append: ", emptylist)
emptylist.extend(sumlist)
print("Extend: ", emptylist)
emptylist.insert(0,data)
print("Insert: ", emptylist)
emptylist.remove(sumlist)
print("Remove: ", emptylist)
del(emptylist)
testlist = [a for a in [1, 2, 3, 3, 4, 5, 6, 7, 6, 8, 5, 7, 8, 9, 7, 5, 4]]
print("Testlist: ", testlist)
print("In Testlist 6 is", testlist.count(6))
testlist.sort()
print("Sort Testlist:", testlist)
for i in testlist:
    if i == 6:
        ind.append(testlist.index(i))
for i in ind:
    testlist.pop(i)
print("Testlist without 6: ", testlist)
print("Cut Testlist", testlist[4:8:1])
cort = (2, 3, 4)
print("Cortege: ", cort)
print("Size of cortege:",cort.__sizeof__(),"byte")
