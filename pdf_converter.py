from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from PyPDF2 import PdfFileWriter, PdfFileReader
from docx2pdf import convert
import img2pdf
from pdf2docx import Converter
from tkinter import filedialog, messagebox
from pdf2image.pdf2image import convert_from_path

win = Tk()
win.title(" PDF CONVERSION TOOLS")
win.iconbitmap("pdf.ico")
win.state("zoomed")

# canvas for layer
canvas = Canvas(win, width=1280, height=720, relief='raised')
canvas.pack()

pdf_pic1 = Image.open("free-pdf-converters.png")
pic_resize1 = pdf_pic1.resize((1280, 720))
my_img1 = ImageTk.PhotoImage(pic_resize1)

my_label1 = Label(canvas, image=my_img1)
my_label1.pack()

label1 = Label(win, text='PDF Converter', bg='lavender')
label1.config(font=('helvetica', 32))
canvas.create_window(580, 50, window=label1)


# first operation for select images
def select_images():
    global filenames
    filenames = askopenfilenames(filetypes=[("JPG", "*.jpg")], title="select files")


# function for create pdf from images
tasks = 0


def img_to_pdf():
    global tasks
    tasks = tasks + 1
    with open(f"Conversion No.{tasks}.pdf", "wb") as f:
        f.write(img2pdf.convert(filenames))
    showinfo("Done", "File successfully converted into PDF ")


# function for exit the application
def exit_application():
    message_box = messagebox.askquestion('exit application', 'are you sure! you want to exit the application',
                                         icon='warning')
    if message_box == 'yes':
        root.destroy()


# second operation
def select_pdf():
    global filenames1
    filenames1 = filedialog.askopenfilename(title="Select a PDF",
                                            filetype=(("PDF    Files", "*.pdf"), ("All Files", "*.*")))


def pdf_to_img():
    pages = convert_from_path(filenames1, dpi=200,
                              poppler_path=r'C:\Program Files\poppler-0.68.0_x86\poppler-0.68.0\bin')
    img_file = filenames1.replace(".pdf", "")
    count = 0
    for page in pages:
        count += 1
        jpg_files = img_file + str(count) + ".jpg"
        page.save(jpg_files, 'JPEG')
    showinfo("Done", "File successfully converted into Images ")


# third operation
def select_WORD():
    global filenames2
    filenames2 = askopenfilenames(filetypes=[("WORD", "*.docx")], title="select files")


def word_to_pdf():
    # convert(filenames2.name, r'C:\Users\ASUS\OneDrive\Desktop')
    # showinfo("Done", "Word File successfully converted into PDF")

    name = filenames2.replace(".docx", ".pdf")
    convert(filenames2, name)
    showinfo("Done", "Word File successfully converted into PDF")


# forth operation

def pdf_to_word():
    wordfile = filenames1.replace(".pdf", ".docx")
    cv = Converter(filenames1)
    cv.convert(wordfile, start=0, end=None)
    showinfo("Done", "File successfully converted into Word file ")
    cv.close()


def encrypt_decrypt_window():
    def f1():
        enc.deiconify()
        root1.wm_withdraw()
        enc_entpass.delete(0, END)
        enc_entfile.focus()

    def f2():
        dec.deiconify()
        root1.withdraw()
        dec_entpass.delete(0, END)
        dec_entfile.focus()

    def f3():
        new = filenames1.replace(".pdf", " encrypted.pdf")
        pdfWriter = PdfFileWriter()
        pdf = PdfFileReader(filenames1)

        for page_num in range(pdf.numPages):
            pdfWriter.addPage(pdf.getPage(page_num))

        passw = enc_entpass.get()
        pdfWriter.encrypt(passw)
        with open(new, 'wb') as f:
            pdfWriter.write(f)
            f.close()
        messagebox.showinfo('Success', 'File Encrypted !')

    def f4():
        # root1.iconify()
        enc.withdraw()

    def f5():
        filenames1
        new = filenames1.replace(" encrypted.pdf", " decrypted.pdf")
        out = PdfFileWriter()
        file = PdfFileReader(filenames1)
        password = dec_entpass.get()

        file.decrypt(password)
        for idx in range(file.numPages):
            page = file.getPage(idx)
            out.addPage(page)

        with open(new, "wb") as f:
            out.write(f)
        messagebox.showinfo('Success', 'File Decrypted !')

    def f6():
        dec.withdraw()

    # Home Page of encrypt and decrypt file
    root1 = Tk()
    root1.title("PDF Encrypt Decrypt")
    root1.state('zoomed')

    root_lbl = Label(root1, text="PDF Encrypt And Decrypt", font=('Times New Roman', 30), width=20)
    root_btnen = Button(root1, text="Encrypt File", font=('Times New Roman', 20), width=10, command=f1)
    root_btnde = Button(root1, text="Decrypt File", font=('Times New Roman', 20), width=10, command=f2)

    root1.configure(bg='slategray1')
    root_lbl.configure(bg='white')
    root_btnen.configure(bg='lavender')
    root_btnde.configure(bg='papaya whip')

    root_lbl.pack(pady=10)
    root_btnen.pack(pady=10)
    root_btnde.pack(pady=10)

    # Encrpyt Page
    enc = Toplevel(root1)
    enc.title("PDF Encrypt")

    enc_lbl = Label(enc, text="PDF Encryption", font=('Times New Roman', 30), width=20)
    enc_lblfile = Label(enc, text="Enter File Name", bg="LightBlue", font=('Arial', 20, 'bold'))
    enc_entfile = Button(enc, text="Select a PDF", font=('Times New Roman', 20), width=10, command=select_pdf)
    enc_lblpass = Label(enc, text="Enter Password ", bg="LightBlue", font=('Arial', 20, 'bold'))
    enc_entpass = Entry(enc, bd=5, font=('Arial', 20, 'bold'))
    enc_btn = Button(enc, text="Encrypt", font=('Times New Roman', 20), width=8, command=f3)
    enc_btnback = Button(enc, text="Back", font=('Times New Roman', 20), width=8, command=f4)

    enc.configure(bg='lavender')
    enc_lbl.configure(bg='white')
    enc_lblfile.configure(bg='lavender')
    enc_lblpass.configure(bg='lavender')
    enc_btn.configure(bg='lavender blush')
    enc_entfile.configure(bg='lavender blush')
    enc_btnback.configure(bg='slategray1')

    enc_lbl.pack(pady=10)
    enc_lblfile.pack(pady=10)
    enc_entfile.pack(pady=10)
    enc_lblpass.pack(pady=10)
    enc_entpass.pack(pady=10)
    enc_btn.pack(pady=10)
    enc_btnback.pack(pady=10)

    enc.withdraw()

    # Decrypt Page
    dec = Toplevel(root1)
    dec.title("PDF Decrypt")
    dec.frame()

    dec_lbl = Label(dec, text="PDF Decryption", font=('Times New Roman', 30), width=20)
    dec_lblfile = Label(dec, text="Enter File Name", bg="LightBlue", font=('Arial', 20, 'bold'))
    dec_entfile = Button(dec, text="Select a PDF", font=('Times New Roman', 20), width=10, command=select_pdf)
    dec_lblpass = Label(dec, text="Enter Password: ", bg="LightBlue", font=('Arial', 20, 'bold'))
    dec_entpass = Entry(dec, bd=5, font=('Arial', 20, 'bold'))
    dec_btn = Button(dec, text="Decrypt", font=('Times New Roman', 20), width=8, command=f5)
    dec_btnback = Button(dec, text="Back", font=('Times New Roman', 20), width=8, command=f6)

    dec.configure(bg='papaya whip')
    dec_lbl.configure(bg='white')
    dec_lblfile.configure(bg='papaya whip')
    dec_lblpass.configure(bg='papaya whip')
    dec_btn.configure(bg='lavender blush')
    dec_btnback.configure(bg='slategray1')
    dec_entfile.configure(bg='lavender blush')

    dec_lbl.pack(pady=10)
    dec_lblfile.pack(pady=10)
    dec_entfile.pack(pady=10)
    dec_lblpass.pack(pady=10)
    dec_entpass.pack(pady=10)
    dec_btn.pack(pady=10)
    dec_btnback.pack(pady=10)

    dec.withdraw()


def open_Tools_window():
    win.wm_withdraw()
    global root
    root = Tk()
    root.title("Tools window")
    # root.geometry("500x500")
    root.state('zoomed')
    root['bg'] = 'slategray1'

    # label
    label_1 = Label(root, text="Images To PDF Converter ", bg="papaya whip", fg="black",
                    font=("times new roman", 20, "bold"))
    label_1.place(x=450, y=0)
    label_2 = Label(root, text="PDF To Images Converter ", bg="papaya whip", fg="black", font=("times new roman", 20,
                                                                                               "bold"))
    label_2.place(x=450, y=130)
    label_3 = Label(root, text="Docx/Word file to PDF ", bg="papaya whip", fg="black", font=("times new roman", 20,
                                                                                             "bold"))
    label_3.place(x=450, y=260)
    label_4 = Label(root, text="PDF To Word Converter ", bg="papaya whip", fg="black",
                    font=("times new roman", 20, "bold"))
    label_4.place(x=450, y=390)

    # buttons for first operation
    button_01 = Button(root, text="Select Images", fg="black", font=("times new roman", 15, "bold"),
                       command=select_images, cursor="hand2")
    button_01.place(x=300, y=60)

    button_02 = Button(root, text="Img To PDF", fg="dark green", font=("times new roman", 15, "bold"),
                       command=img_to_pdf, cursor="hand2")
    button_02.place(x=550, y=60)

    button_03 = Button(root, text="Exit Application", fg="red", font=("times new roman", 15, "bold"),
                       command=exit_application, cursor="hand2")
    button_03.place(x=770, y=60)

    # buttons for second operation
    button_04 = Button(root, text="Select pdf", fg="black", font=("times new roman", 15, "bold"), command=select_pdf,
                       cursor="hand2")
    button_04.place(x=300, y=190)

    button_05 = Button(root, text="PDF To Images", fg="dark green", font=("times new roman", 15, "bold"),
                       command=pdf_to_img, cursor="hand2")
    button_05.place(x=550, y=190)

    button_06 = Button(root, text="Exit Application", fg="red", font=("times new roman", 15, "bold"),
                       command=exit_application, cursor="hand2")
    button_06.place(x=770, y=190)

    # buttons for third operation
    button_07 = Button(root, text="Select A Word file", fg="black", font=("times new roman", 15, "bold"),
                       command=select_WORD, cursor="hand2")
    button_07.place(x=300, y=320)

    button_08 = Button(root, text="Word To PDF", fg="dark green", font=("times new roman", 15, "bold"),
                       command=word_to_pdf, cursor="hand2")
    button_08.place(x=550, y=320)

    button_09 = Button(root, text="Exit Application", fg="red", font=("times new roman", 15, "bold"),
                       command=exit_application, cursor="hand2")
    button_09.place(x=770, y=320)

    # buttons for forth operation
    button_10 = Button(root, text="Select A pdf", fg="black", font=("times new roman", 15, "bold"),
                       command=select_pdf, cursor="hand2")
    button_10.place(x=300, y=450)

    button_11 = Button(root, text="PDF to Word ", fg="dark green", font=("times new roman", 15, "bold"),
                       command=pdf_to_word, cursor="hand2")
    button_11.place(x=550, y=450)

    button_12 = Button(root, text="Exit Application", fg="red", font=("times new roman", 15, "bold"),
                       command=exit_application, cursor="hand2")
    button_12.place(x=770, y=450)

    button_13 = Button(root, text="Encrypt and decrypt file", fg="black", bg='papaya whip', font=("times new roman", 22,
                                                                                                "bold"),
                       command=encrypt_decrypt_window, cursor="hand2")
    button_13.place(x=450, y=530)


toolsButton = Button(text="     Tools     ", command=open_Tools_window, bg='slategray1', fg='Blue4',
                     font=('helvetica', 20, 'bold'))
canvas.create_window(580, 350, window=toolsButton)

win.mainloop()
