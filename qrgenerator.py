import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


def createQR(*args):
    
    data = app.text_entry.get()
    if data:
        img = qrcode.make(data)
        res_img = img.resize((280, 250))
        tkimage = ImageTk.PhotoImage(res_img)
        app.qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        app.qr_canvas.image = tkimage
    else:
        messagebox.showwarning("Warning", 'Enter Data in Entry First')


def saveQR():
    """Generate and save a QR code based on the entered data."""
    data = app.text_entry.get()
    if data:
        img = qrcode.make(data)
        res_img = img.resize((280, 250))

        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            res_img.save(path)
            messagebox.showinfo("Success", "QR Code is Saved ")
    else:
        messagebox.showwarning("Warning", 'Enter Data in Entry First')


class QRCodeGeneratorApp:
    """Tkinter application for generating and saving QR codes."""

    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")
        self.center_window()

        self.frame1 = tk.Frame(master, bd=2, relief=tk.RAISED)
        self.frame1.place(x=10, y=5, width=280, height=250)

        self.frame2 = tk.Frame(master, bd=2, relief=tk.SUNKEN)
        self.frame2.place(x=10, y=260, width=280, height=100)

        self.qr_canvas = tk.Canvas(self.frame1)
        self.qr_canvas.pack(fill=tk.BOTH)

        self.text_entry = ttk.Entry(self.frame2, width=26, font=("Sitka Small", 11), justify=tk.CENTER)
        self.text_entry.bind("<Return>", createQR)
        self.text_entry.place(x=5, y=5)

        self.btn_1 = ttk.Button(self.frame2, text="Create", width=10, command=createQR)
        self.btn_1.place(x=25, y=50)

        self.btn_2 = ttk.Button(self.frame2, text="Save", width=10, command=saveQR)
        self.btn_2.place(x=100, y=50)

        self.btn_3 = ttk.Button(self.frame2, text="Exit", width=10, command=master.quit)
        self.btn_3.place(x=175, y=50)

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x_position = (screen_width - 300) // 2
        y_position = (screen_height - 380) // 2

        self.master.geometry(f"300x380+{x_position}+{y_position}")


if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
