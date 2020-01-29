import csv

class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_NONE
    quotechar = "*"
    delimiter = " "
    lineterminator = "\n"
csv.register_dialect('test_dialect', CustomDialect)
try:
    # Детектирование диалекта
    sniffer = csv.Sniffer()
    dialect = None
    with open('test_csv.csv', 'r') as f:
        cont = f.read()
        dialect = sniffer.sniff(cont)
    # Открыть csv как массивы строк
    with open('test_csv.csv', 'r') as f:
        read = csv.reader(f, dialect=dialect)
        print('Line nums', read.line_num)
        print('Dialect', read.dialect)
        for row in read:
            print(row)
    # Открыть сsv как набор словарей
    with open('test_csv.csv', 'r') as f:
        read = csv.DictReader(f, dialect=dialect)
        print('Line nums', read.line_num)
        print('Dialect', read.dialect)
        for row in read:
            print(row)
            print(row['price'] + ' with line_num ' + str(read.line_num))
    # Записать в сsv строку как массив
    with open('test_csv_write.csv', 'w') as f:
        write = csv.writer(f, dialect=dialect)
        write.writerow(['field,1', 'field2', 'field3'])
    # Запись в сsv с помощью словарей
except:
    print("ERROR TRY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
finally:
    with open('test_csv.csv', 'w') as f:
        writer = csv.DictWriter(f,
                                fieldnames=['number', 'name', 'price'],
                                dialect='test_dialect'
                                )
        writer.writeheader()
        writer.writerow({
            'number': '5',
            'name': 'fifth',
            'price': 500
        })
        writer.writerow({
            'number': '6',
            'name': 'sixth',
            'price': 110
        })
