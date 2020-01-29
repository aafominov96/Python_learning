d = {'Name': "Artyom", 'Age': 22}
print("All dictionary", d)
print("Key 'Name': ", d['Name'])
d_1 = dict(Name = "Artyom", Age = 22)
print("All dictionary 2: ", d_1)
d_2 = dict([("Name", "Artyom"), ("Age", 22)])
print("All dictionary 3: ", d_2)
d_3 = dict.fromkeys(['Name', 'Age', 'Work'], 0)
print("All dictionary 4: ", d_3)
d_4 = {a: a**2 for a in range (7)}
print("All dictionary 5: ", d_4)
test_dict = dict.fromkeys(['Name', 'Age', 'Sex'], 0)
test_dict['Name'] = "Artyom"
test_dict['Age'] = 22
test_dict['Sex'] = "Men"
print("Test dictionary #1: ", test_dict)
copydict = test_dict.copy()
test_dict.clear()
Name = copydict.get('Name')
print(Name)
Items = copydict.items()
print(Items)
Keys = copydict.keys()
print(Keys)
PopName = copydict.pop('Name')
print(PopName, copydict)
PopItem = copydict.popitem()
print(PopItem, copydict)
copydict.update({'Name': "Artyom"})
print(copydict)

mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for_dict = {'Test'+str(a): a+1 for a in range(1, 10, 1)}
for_dict_2 = {b: a+1 for a in range(1, 10, 1) for b in mass}
print(for_dict)
print(for_dict_2)
