import qrcode
import tkinter
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

t1 = ""
t2 = ""
create = ""
recup = ""

def launch():

    def create():
        img = qrcode.make(t1.get())

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        qr.add_data(t1.get())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        img.save("qr_code.png")

        if (b1['state'] == NORMAL):
            b1['state'] = DISABLED
        else:
            b1['state'] = DISABLED

        qr1 = Image.open("qr_code.png")
        resize_image = qr1.resize((157, 157))
        qrrcode = ImageTk.PhotoImage(resize_image)
        image1 = tkinter.Label(image=qrrcode)
        image1.image = qrrcode
        image1.place(x=190, y=148)

    # label 0
    lbl0=Label(text='QR MAKER', font=("bold", 24))
    lbl0.place(x=190, y=12)
    # label 1
    lbl1=Label(text='Please write your Text/Link to convert into a QR Code', font=(10))
    lbl1.place(x=90, y=65)
    # label 2
    l = LabelFrame(window, text="Result", padx=50, pady=68)
    l.pack(fill="both", expand="yes")
    l.place(x=189, y=135)
    Label(l, text="No Result.").pack()

    # text 1
    t1=Entry(bd=2, width=80)
    t1.place(x=35, y=95)

    # boutton 1
    tb = font.Font(size=14)
    b1=Button(text='Convert', command=create)
    b1.place(x=177, y=340)
    b1['font'] = tb
    # boutton 2
    b2=Button(text='Reset', command=reset)
    b2.place(x=290, y=340)
    b2['font'] = tb

def reset():
    launch()

window=Tk()
mywin=launch()
window.title("QR Maker by Astraa")
window.geometry('550x390')
window.mainloop()