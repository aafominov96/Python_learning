from xml.etree import ElementTree as et
'''Чтение из xml'''
tree = et.parse('test_xml.xml')
root = tree.getroot()
'''children = root.getchildren()'''

for group in root:
    print("Group: ", group.attrib)
    for student in group:
        print('{}: {}'.format(student.tag, student.text))
'''Создание xml'''
root = et.Element('MAIN_ELEM')
for i in range(10):
    sub_element = et.SubElement(root, 'value{}'.format(i))
    sub_element.text = str(i * 10)
print(et.dump(root))

data = [
    {'x': 10, 'y': 20, 'z': 30},
    {'x': 'zello', 'y': 40, 'z': True}
]
root = et.Element('records')
for item in data:
    record = et.SubElement(root, 'record')
    for key, value in item.items():
        e = et.SubElement(record, key)
        e.text = str(value)
tree = et.ElementTree(root)
tree.write('test_xml_created.xml', encoding='utf-8')