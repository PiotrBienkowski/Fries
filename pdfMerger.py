from PyPDF2 import PdfMerger


pdfs = []

for i in range(201, 351):
    pdfs.append('folder_pdf_3/fr_' + str(i) + '.pdf')


merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result3.pdf")
merger.close()