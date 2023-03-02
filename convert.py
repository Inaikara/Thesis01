import PyPDF2
filenames=['cover.pdf','manuscript.pdf']
merger=PyPDF2.PdfFileMerger()
for filename in filenames:
    merger.append(PyPDF2.PdfFileReader(filename))
merger.write('课设报告.pdf')