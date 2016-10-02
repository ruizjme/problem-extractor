from PyPDF2 import PdfFileReader

b = 'book-long.pdf'

print('READING: ['+b+']')

i = int(input('Insert page number: ')) #this here stores the page number

f = open(b,'rb')

r = []

n = 1
m = 0

try:
    contents = PdfFileReader(f).getPage(i-1).extractText()
    for l in contents:

        o = open(str(i)+'.txt','w')
        o.write(contents.encode('utf-8')) #str(r).encode('utf-8')
        o.close()
finally:
        f.close()
        print('COMPLETE: ['+str(i)+'.txt]')
