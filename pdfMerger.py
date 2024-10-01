from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["data/file1.pdf", "data/file2.pdf", "data/file3.pdf"]:
    merger.append(pdf)

merger.write("data/merged-pdf.pdf")
merger.close()