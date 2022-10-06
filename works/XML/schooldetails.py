import xml.etree.ElementTree as et
myroot=et.parse("school.xml")

val=myroot.getroot()
for i in val[0]:
    print(i[1].tag,':',i[-2].text)
    print(i[2].tag,':',i[-3].text)
    print(i[3].tag,':',i[-4].text)
    print('\n')

    
        