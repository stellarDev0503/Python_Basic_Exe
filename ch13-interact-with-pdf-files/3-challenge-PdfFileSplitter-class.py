# 13.5 - Challenge: PdfFileSplitter Class
# Solution to challenge

from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter


class PdfFileSplitter:
    """Class for splitting a PDF into two files."""

    def __init__(self, pdf_path):
        # Open the PDF file with a new PdfFileReader instance
        self.pdf_reader = PdfFileReader(str(pdf_path))
        # Initialize the .writer1 and .writer2 attributes to None
        self.writer1 = None
        self.writer2 = None

    def split(self, breakpoint):
        """Split the PDF into two PdfFileWriter instances"""
        # Set .writer1 and .writer2 to new PdfFileWriter intances
        self.writer1 = PdfFileWriter()
        self.writer2 = PdfFileWriter()
        # Add all pages up to, but not including, the breakpoint
        # to writer1
        for page in self.pdf_reader.pages[:breakpoint]:
            self.writer1.addPage(page)
        # Add all the remaining pages to writer2
        for page in self.pdf_reader.pages[breakpoint:]:
            self.writer2.addPage(page)

    def write(self, filename):
        """Write both PdfFileWriter instances to files"""
        # Write the first file to <filename>_1.pdf
        with Path(str(filename) + "_1.pdf").open(mode="wb") as output_file:
            self.writer1.write(output_file)
        # Write the second file to <filename>_2.pdf
        with Path(str(filename) + "_2.pdf").open(mode="wb") as output_file:
            self.writer2.write(output_file)


pdf_splitter = PdfFileSplitter("ch13-interact-with-pdf-files/practice_files/Pride_and_Prejudice.pdf")
pdf_splitter.split(breakpoint=150)
pdf_splitter.write("pride_split")
