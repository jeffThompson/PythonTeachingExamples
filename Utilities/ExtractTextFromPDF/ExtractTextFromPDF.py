import PyPDF2			# https://github.com/mstamy2/PyPDF2

input_file = 'test.pdf'

content = ''
pdf = PyPDF2.PdfFileReader(file(input_file, 'rb'))
for i in range(0, pdf.getNumPages()):
	content += pdf.getPage(i).extractText() + ' \n'
	content = " ".join(content.replace(u"\xa0", u" ").strip().split())

print content