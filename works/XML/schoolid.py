import xml.etree.ElementTree as et
myroot=et.parse("school.xml")
val=myroot.getroot()

for i in val[0]:
    if i.attrib["id"]=='5':
        print(i[0].text)
        print(i[1].text)
        print(i[2].text)
        print(i[3].text)
        print(i[4].text)
        print(i[5].text)