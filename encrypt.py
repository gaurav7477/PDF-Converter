from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader


def f1():
    enc.deiconify()
    root.withdraw()
    enc_entfile.delete(0, END)
    enc_entpass.delete(0, END)
    enc_entfile.focus()


def f2():
    dec.deiconify()
    root.withdraw()
    dec_entfile.delete(0, END)
    dec_entpass.delete(0, END)
    dec_entfile.focus()


def f3():
    pdfWriter = PdfFileWriter()
    pdf = PdfFileReader(enc_entfile.get())

    for page_num in range(pdf.numPages):
        pdfWriter.addPage(pdf.getPage(page_num))

    passw = enc_entpass.get()
    pdfWriter.encrypt(passw)
    newPdfName = str(enc_entfile.get()) + 'encrypted'
    with open(newPdfName, 'wb') as f:
        pdfWriter.write(f)
        f.close()
    messagebox.showinfo('Success', 'File Encrypted !')


def f4():
    root.deiconify()
    enc.withdraw()


def f5():
    temp = dec_entfile.get()
    out = PdfFileWriter()
    file = PdfFileReader(temp)
    password = dec_entpass.get()

    if file.isEncrypted:
        file.decrypt(password)
        for idx in range(file.numPages):
            page = file.getPage(idx)
            out.addPage(page)

        with open(temp, "wb") as f:
            out.write(f)

        messagebox.showinfo('Success', 'File Decrypted !')
    else:
        messagebox.showerror('Error', 'Already Decrypted !')


def f6():
    root.deiconify()
    dec.withdraw()


# Home Page
root = Tk()
root.title("PDF Encrypt Decrypt")
root.geometry("500x500+400+100")

root_lbl = Label(root, text="PDF Encrypt And Decrypt", font=('Times New Roman', 30), width=20)
root_btnen = Button(root, text="Encrypt File", font=('Times New Roman', 20), width=10, command=f1)
root_btnde = Button(root, text="Decrypt File", font=('Times New Roman', 20), width=10, command=f2)

root.configure(bg='slategray1')
root_lbl.configure(bg='white')
root_btnen.configure(bg='lavender')
root_btnde.configure(bg='papaya whip')

root_lbl.pack(pady=10)
root_btnen.pack(pady=10)
root_btnde.pack(pady=10)

# Encrpyt Page
enc = Toplevel(root)
enc.title("PDF Encrypt")
enc.geometry("500x500+400+100")

enc_lbl = Label(enc, text="PDF Encryption", font=('Times New Roman', 30), width=20)
enc_lblfile = Label(enc, text="Enter File Name", bg="LightBlue", font=('Arial', 20, 'bold'))
enc_entfile = Entry(enc, bd=5, font=('Arial', 20, 'bold'))
enc_lblpass = Label(enc, text="Enter Password ", bg="LightBlue", font=('Arial', 20, 'bold'))
enc_entpass = Entry(enc, bd=5, font=('Arial', 20, 'bold'))
enc_btn = Button(enc, text="Encrypt", font=('Times New Roman', 20), width=8, command=f3)
enc_btnback = Button(enc, text="Back", font=('Times New Roman', 20), width=8, command=f4)

enc.configure(bg='lavender')
enc_lbl.configure(bg='white')
enc_lblfile.configure(bg='lavender')
enc_lblpass.configure(bg='lavender')
enc_btn.configure(bg='lavender blush')
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
dec = Toplevel(root)
dec.title("PDF Decrypt")
dec.geometry("500x500+400+100")

dec_lbl = Label(dec, text="PDF Decryption", font=('Times New Roman', 30), width=20)
dec_lblfile = Label(dec, text="Enter File Name", bg="LightBlue", font=('Arial', 20, 'bold'))
dec_entfile = Entry(dec, bd=5, font=('Arial', 20, 'bold'))
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

dec_lbl.pack(pady=10)
dec_lblfile.pack(pady=10)
dec_entfile.pack(pady=10)
dec_lblpass.pack(pady=10)
dec_entpass.pack(pady=10)
dec_btn.pack(pady=10)
dec_btnback.pack(pady=10)

dec.withdraw()

root.mainloop()
