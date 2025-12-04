from PyPDF2 import PdfMerger

def merge_pdfs(output, *files):
    merger = PdfMerger()

    for pdf in files:
        merger.append(pdf)

    merger.write(output)
    merger.close()

    print("PDF merged successfully!")

# Example
merge_pdfs("combined.pdf", "1.pdf", "2.pdf")
