import csv
import random as r
import matplotlib.pyplot as mpl

class test_dialect(csv.Dialect):
    quoting = csv.QUOTE_NONE
    quotechar = "*"
    delimiter = " "
    lineterminator = "\n"

try:
    with open('test_csv_random.csv', 'r') as f:
        cont = f.read()
        sniffer = csv.Sniffer()
        dialect = None
        dialect = sniffer.sniff(cont)
    with open('test_csv_random.csv', 'r') as f:
        reader = csv.DictReader(f, dialect=dialect)
        content__num = []
        for row in reader:
            content__num.append(row['num'])
        content__num.sort()
    with open('test_csv_random_sort.csv', 'w') as f:
        writer = csv.DictWriter(f,
                                fieldnames=['id', 'sort_num'],
                                dialect=dialect)
        writer.writeheader()
        for i in range(0, len(content__num), 1):
            writer.writerow({
                'id': i+1,
                'sort_num': content__num[i]
            })
    stat_mass = [0, 0, 0, 0, 0]
    for searcher in content__num:
        if searcher == '1':
            stat_mass[0] += 1
        if searcher == '2':
            stat_mass[1] += 1
        if searcher == '3':
            stat_mass[2] += 1
        if searcher == '4':
            stat_mass[3] += 1
        if searcher == '5':
            stat_mass[4] += 1
    print(stat_mass)
    mpl.plot(stat_mass, marker='o')
    mpl.show()
except:
    csv.register_dialect('new_dialect', test_dialect)
    with open('test_csv_random.csv', 'w') as f:
        writer = csv.DictWriter(f,
                                fieldnames=['id', 'num'],
                                dialect='new_dialect'
                                )
        writer.writeheader()
        for i in range(1, 500, 1):
            writer.writerow({'id': i, 'num': r.randrange(1, 6)})
