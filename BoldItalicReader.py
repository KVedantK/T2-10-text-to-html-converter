from docx import *

#Reads a document in docx format
document = Document('base.docx')

#opens a file in html format
f = open('base.html', 'a')
bolds=[]
italics=[]

#Reads a document para wise checks each word for bold adds <b></b> and for itlaic adds <i></i>
for para in document.paragraphs:
    for run in para.runs:
        if run.italic :
            italics.append(run.text)
            f.write('<i>'+run.text+'</i>')
        if run.bold :
            bolds.append(run.text)
            f.write('<b>'+run.text+'</b>')
        else:
            f.write(run.text)
f.close()
boltalic_Dict={'bold_phrases':bolds,
            'italic_phrases':italics}

