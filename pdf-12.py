#!/usr/bin/python

from PyPDF2 import PdfFileReader
import re
 
b = 'book-long.pdf' # input file name, must be in the same folder
c = '.txt' # output file format eg '.html'

# Extract page contents to analyse
def extract_text(pg):
    '''
    Scrape the page 'pg' to get the contents
    '''
    f = open(b, 'rb')

    contents = PdfFileReader(f).getPage(pg - 1).extractText()

    o = open(str(pg) + c, 'w')
    o.write(unicode(contents).encode('utf-8','ignore'))
    o.close()
    f.close()
    print 'Page ' + str(pg) + ' scraped.'
    return contents

# Extract questions from page
def extract_questions(pg):

    '''
    Scrape the page 'pg' and save all questions in a new document
    '''
    f = open(b,'rb')

    contents = PdfFileReader(f).getPage(pg-1).extractText()
    cont = re.sub(r'\n','',contents)
    matched = re.sub(r'( \d+)(\. )', r' \1\. ',cont)
    matches = re.findall('( \d+\\\\\. )', matched)
    
    n = 0
    questions = {}

    for l in matches:
    
        if n < len(matches)-1: 
            question = re.findall(matches[n]+'(.*?)'+matches[n+1], cont)

        elif n == len(matches)-1:
            question = re.findall(matches[n]+'(.*)', cont)
            
        questions[matches[n]] = question[0]
    
        n = n+1

    o = open(str(pg)+c,'w')
    o.write(str(questions).encode('utf-8'))
    o.close()
    f.close()
    print 'Page '+str(pg)+' contains '+str(len(matches))+' questions.'
    return questions

# TODO: Extract chapter information and tags
def contents_page(pg):
    f = open(b, 'rb')

    contents = PdfFileReader(f).getPage(pg - 1).extractText()

    o = open(str(pg) + c, 'w')
    o.write(contents.encode('utf-8','ignore'))
    o.close()
    f.close()

    print 'Page of contents done.'
    return contents

# TODO: Extract author and book title information


# TODO: Extract answer and match it to the question

# TODO: Parse questions and prepare SQL
def dict_to_sql(pg, d):
    o = open(str(pg) +'.sql', 'w')
    SQL = ''

    for i in d.values():
        SQL +=   '''
        INSERT INTO `t_questions` (`q_id`, `question`, `answer`, `figure`)
        VALUES (
            NULL,
            '%s',
            '?',
            ''
            );
        '''%(i)

    o.write(SQL.encode('utf-8', 'ignore'))
    o.close()

# MAIN FUNCTION
def main():
        pg = int(input('Insert page number: '))
        dict_to_sql(pg, extract_questions(pg))
        #contents_page(int(8))


if __name__ == '__main__':
    main()