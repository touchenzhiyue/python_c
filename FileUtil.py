# --*-- coding:utf-8 --*--
#文件操作工具类
# version 1.0
# 20181226

from PyPDF2 import PdfFileReader, PdfFileWriter

def PDF():
    readFile = "read.pdf"
    writeFile = "write.pdf"
    pdfReader = PdfFileReader(open(readFile,'rb'))
    pageCount = pdfReader.getNumPages() #获取pdf的页数
    print(pageCount)
    page = pdfReader.getPage(1) #返回第一页的pageobject
    pdfWriter = PdfFileWriter()
    pdfWriter.addBlankPage(page)
    pdfWriter.write(open(writeFile,'wb'))
