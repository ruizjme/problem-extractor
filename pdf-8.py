from PyPDF2 import PdfFileReader
import re
 
b = 'book-long.pdf' #input file name, must be in the same folder

c = '.txt' #output file format eg '.html'

print('READING: ['+b+']')

i = int(input('Insert page number: ')) #this here stores the page number, which is also the output file name

f = open(b,'rb')

n = 0

print('PROCESSING...')

try:
    contents = PdfFileReader(f).getPage(i-1).extractText()

    o = open(str(i)+c,'w')
    o.write(contents.encode('utf-8'))
    o.close()

    cont = re.sub(r'\n','',contents)
    
finally:
    f.close()
    print('COMPLETE: ['+str(i)+c+']')
    print

    matched = re.sub(r'( [0-9]+)(\. )', r' \1\. ',cont)
    matches = re.findall('( [0-9]+\\\\\. )', matched)

    print('Amount of questions in page: '+str(len(matches)))
    
    questions = []

    for l in matches:

        if n < len(matches)-1: 

            question = re.findall(matches[n]+'(.*?)'+matches[n+1], cont) #matches array is passing a string with a dot in it which finds any character. That dot need to be backslashed somehow.
        elif n == len(matches)-1:
            question = re.findall(matches[n]+'(.*)', cont)
        
        for m in question:
            questions.append(m)

        n = n+1

        #use this to query each question 'questions[0]'
        #find a way to include the last question, which does NOT lie between two wquestion numbers
