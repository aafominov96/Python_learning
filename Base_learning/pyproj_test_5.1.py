import csv
'''
with open('test_TB_data.csv', 'r') as f:
    print('Первый прогон')
    read = csv.reader(f)
    for i in read:
        print(i)
        print(read.line_num)
    for i in read:
        print(read.line_num)
    print('STOP 1')
    print(f.read())
'''
count = 0
with open('test_TB_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    count_for = 0
    count_for_buf = 0
    for i in reader:
        if i['dataset'] == 'Budget':
            count += 1
            buf = i['definition']
            for j in range(1, len(buf)):
                if buf[j-1] == 'f' and buf[j] == 'o' and buf[j+1] == 'r':
                    count_for += 1
            print('В строке ' + str(reader.line_num) + ' слово for встречается ' + str(count_for) + ' раз')
            count_for_buf += count_for
            count_for = 0

print('Всего строк с пометкой "Бюджет": ', count)
print('Слово for встречается в этих строках ' + str(count_for_buf) + ' раз')