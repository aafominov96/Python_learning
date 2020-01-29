i_min = 0
i = 5
i_max = 10
while i>i_min and i<i_max:
    i+=1
    print(i)
    if i == 7:
        break
else:
    print("Цикл завершен")
text = "Hey man"
check_1 = 0
check_2 = 0
check_3 = 0
for j in text:
    if j == "y" or j == "a":
        check_1 = 1
        continue
    if j == "p" :
        check_2 = 1
        break
    print(j, end =' Ok \n')
else:
    check_3 = 1
print(check_1,check_2,check_3)
