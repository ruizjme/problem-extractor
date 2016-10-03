from PyPDF2 import PdfFileReader
import re

b = 'book-long.pdf'

print('READING: ['+b+']')

i = int(input('Insert page number: ')) #this here stores the page number

f = open(b,'rb')

try:
    contents = PdfFileReader(f).getPage(i-1).extractText()

    o = open(str(i)+'.txt','w')
    o.write(contents.encode('utf-8'))
    o.close()
finally:
    f.close()
    print('COMPLETE: ['+str(i)+'.txt]')
    matches = re.findall("([0-9]+\. )", contents)
    print(matches)
