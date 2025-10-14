from docx import Document
doc=Document("sdc ccna lan answeres.docx")
for para in doc.paragraphs:
	print(para.text)
