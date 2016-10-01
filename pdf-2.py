from PyPDF2 import PdfFileReader

b = 'book-long.pdf'

print("READING: ["+b+"]")

i = int(input("Insert page number: "))-1

f = open(b,'rb')

r = []

n = 1
m = 0

try:
    contents = PdfFileReader(f).getPage(i).extractText()
    for l in contents:
        if l == str(n):
            #if l+1 == ".":
            print(n)
            n = n+1
        elif n >= 10:
            if l == str(m):
                print(n)
                n = n+1
                m = m+1
            

        o = open('output.html','w')
        o.write(contents.encode('utf-8')) #str(r).encode('utf-8')
        o.close()
finally:
        f.close()
        print("OPERATION COMPLETE.")
        while True:
                try:
                        ri = int(raw_input("Index? - "))
                        print("Index number "+str(ri)+" corresponds to \""+str(r[ri])+"\"")
                except ValueError:
                        print("Invalid input.")
                except IndexError:
                        print("Out of scope.")
