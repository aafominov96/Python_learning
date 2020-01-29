from lxml import etree as et

class Targeter:
    def __init__(self):
        self.records = []
        self.current_index = None
        self.current_node = None
        self.checker = 0
    def start(self, tag, attrib):
        if tag == 'person':
            self.records.append({
                'first_name': '',
                'second_name': '',
                'age': None
            })
            self.current_index = len(self.records) - 1
            self.checker = 1
        self.current_node = tag
    def end(self, tag):
        self.current_node = ''
    def data(self, data):
        if self.current_node in ['first_name', 'second_name', 'age'] and self.checker == 1:
            if self.current_node == 'age':
                self.checker = 0
            self.records[self.current_index][self.current_node] = data
    def close(self):
        return self.records

parser = et.XMLParser(target=Targeter())
infile = 'test_xml.xml'
results = et.parse(infile, parser)
for i in results:
    print(i)
