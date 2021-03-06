from PyPDF2 import PdfFileReader
import re
 
b = 'book-long.pdf' #input file name, must be in the same folder

c = '.txt' #output file format eg '.html'

print('READING: ['+b+']')

i = int(input('Insert page number: ')) #page number, also output filename

f = open(b,'rb')

print('PROCESSING...')

try:
    contents = PdfFileReader(f).getPage(i-1).extractText()

    o = open(str(i)+c,'w')
    o.write(contents.encode('utf-8'))
    o.close()
    
finally:
    f.close()
    
    print('COMPLETE: ['+str(i)+c+']')
    print
    
    cont = re.sub(r'\n','',contents)
    matched = re.sub(r'( [0-9]+)(\. )', r' \1\. ',cont)
    matches = re.findall('( [0-9]+\\\\\. )', matched)

    print('Amount of questions in page: '+str(len(matches)))
    
    n = 0
    questions = []

    for l in matches:

        if n < len(matches)-1: 
            question = re.findall(matches[n]+'(.*?)'+matches[n+1], cont)

        elif n == len(matches)-1:
            question = re.findall(matches[n]+'(.*)', cont)
        
        for m in question:
            questions.append(m)

        n = n+1

        #use 'questions[0]' to see each question
