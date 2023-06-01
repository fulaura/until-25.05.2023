import tkinter as tk
import tkinter.filedialog as fd
import os
import PyPDF2
import epub
import xml.etree.ElementTree as ET

# Function to read a book in FB2 format
def read_fb2(file_path):
    with open(file_path, 'r') as f:
        fb2_data = f.read()

    fb2_root = ET.fromstring(fb2_data)
    book_title = fb2_root.find('.//title').text
    book_text = fb2_root.find('.//body').text

    return book_title, book_text

# Function to read a book in PDF format
def read_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        book_title = pdf_reader.getDocumentInfo().title
        book_text = ''
        for i in range(pdf_reader.getNumPages()):
            book_text += pdf_reader.getPage(i).extractText()

    return book_title, book_text

# Function to read a book in EPUB format
def read_epub(file_path):
    book = epub.read_epub(file_path)
    book_title = book.get_metadata('DC', 'title')[0][0]
    book_text = ''
    for item in book.get_items():
        if item.get_type() == epub.ITEM_DOCUMENT:
            book_text += item.get_content().decode('utf-8')

    return book_title, book_text

# Function to handle file selection and reading
def select_and_read():
    file_path = fd.askopenfilename(
        title='Select a book file',
        filetypes=[('FB2 Files', '*.fb2'), ('PDF Files', '*.pdf'), ('EPUB Files', '*.epub')]
    )

    if file_path:
        # Determine the file format of the book and call the appropriate reader function
        if file_path.endswith('.fb2'):
            book_title, book_text = read_fb2(file_path)
        elif file_path.endswith('.pdf'):
            book_title, book_text = read_pdf(file_path)
        elif file_path.endswith('.epub'):
            book_title, book_text = read_epub(file_path)
        else:
            print('Unsupported file format.')
            return

        print(f'\n{book_title}\n')
        animation = ['|', '/', '-', '\\']
        index = 0
        for line in book_text.splitlines():
            print(line)
            print(animation[index % len(animation)], end='\r')
            index += 1

# Main function to create the GUI
def main():
    window = tk.Tk()
    window.title('Book Reader')
    window.geometry('300x200')

    select_button = tk.Button(
        window,
        text='Select a book file',
        command=select_and_read
    )
    select_button.pack(pady=20)

    window.mainloop()

if __name__ == '__main__':
    main()
import tkinter as tk
import tkinter.filedialog as fd
import os
import PyPDF2
import epub
import xml.etree.ElementTree as ET

# Function to read a book in FB2 format
def read_fb2(file_path):
    with open(file_path, 'r') as f:
        fb2_data = f.read()

    fb2_root = ET.fromstring(fb2_data)
    book_title = fb2_root.find('.//title').text
    book_text = fb2_root.find('.//body').text

    return book_title, book_text

# Function to read a book in PDF format
def read_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        book_title = pdf_reader.getDocumentInfo().title
        book_text = ''
        for i in range(pdf_reader.getNumPages()):
            book_text += pdf_reader.getPage(i).extractText()

    return book_title, book_text

# Function to read a book in EPUB format
def read_epub(file_path):
    book = epub.read_epub(file_path)
    book_title = book.get_metadata('DC', 'title')[0][0]
    book_text = ''
    for item in book.get_items():
        if item.get_type() == epub.ITEM_DOCUMENT:
            book_text += item.get_content().decode('utf-8')

    return book_title, book_text

# Function to handle file selection and reading
def select_and_read():
    file_path = fd.askopenfilename(
        title='Select a book file',
        filetypes=[('FB2 Files', '*.fb2'), ('PDF Files', '*.pdf'), ('EPUB Files', '*.epub')]
    )

    if file_path:
        # Determine the file format of the book and call the appropriate reader function
        if file_path.endswith('.fb2'):
            book_title, book_text = read_fb2(file_path)
        elif file_path.endswith('.pdf'):
            book_title, book_text = read_pdf(file_path)
        elif file_path.endswith('.epub'):
            book_title, book_text = read_epub(file_path)
        else:
            print('Unsupported file format.')
            return

        print(f'\n{book_title}\n')
        animation = ['|', '/', '-', '\\']
        index = 0
        for line in book_text.splitlines():
            print(line)
            print(animation[index % len(animation)], end='\r')
            index += 1

# Main function to create the GUI
def main():
    window = tk.Tk()
    window.title('Book Reader')
    window.geometry('300x200')

    select_button = tk.Button(
        window,
        text='Select a book file',
        command=select_and_read
    )
    select_button.pack(pady=20)

    window.mainloop()

if __name__ == '__main__':
    main()
