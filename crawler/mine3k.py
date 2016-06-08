from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
import time

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

st= time.time()
#http://pythonscraping.com/pages/warandpeace/chapter1.pdf
#pdfFile = urlopen("c://redis.pdf");

#rsrcmgr = PDFResourceManager()
#retstr = StringIO()
#laparams = LAParams()
#device = TextConverter(rsrcmgr, retstr, laparams=laparams)

#process_pdf(rsrcmgr, device, pdfFile)
#device.close()

#content = retstr.getvalue() 
#retstr.close()
#st = time.time()

#print(content)
#print("spantime:",(st-st4))





#fp= open('c://redis.pdf', 'rb')
fp = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
parser = PDFParser(fp)

doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize('')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
st2 = time.time()
print("sss=>",(st2-st))
for page in doc.get_pages():
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            print(lt_obj.get_text())
print("sss2=>",(time.time()-st2))
print("sss3=>",(time.time()-st))
