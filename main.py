# A Desktop program where you can upload images and add a watermark.

from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
from tkinter import filedialog, simpledialog

PURPLE = "#3E065F"


# watermark creator
def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)
    # make the image editable
    drawing = ImageDraw.Draw(photo)
    black = (3, 8, 12)
    font = ImageFont.load_default()
    drawing.text(pos, text, fill=black, font=font)
    # photo.show()
    photo.save(output_image_path)


class GUI:
    def __init__(self):
        self.window = Tk()
        self.filename = ""

        self.window.geometry("1920x1080")
        self.window.config(padx=10, pady=10)
        self.window.title("Watermarker")

        upload_button = Button(self.window, text="Upload an Image", command=self.upload)
        save_button = Button(self.window, text="Save Watermarked Image", command=self.save)
        exit_button = Button(self.window, text="Quit", command=self.window.quit)
        text_button = Button(self.window, text="Choose WM Text", command=self.text_ask)

        upload_button.grid(column=1, row=3)
        text_button.grid(column=2, row=3)
        save_button.grid(column=3, row=3)
        exit_button.grid(column=4, row=3)

        self.window.mainloop()

    # watermarking function
    def watermark(self, filename):
        img = filename
        watermark_text(img, f'{img}_watermarked.png',
                       text=self.wm_text,
                       pos=(5, 0))

    def upload(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select an Image")
        self.image_label = Label(self.window, text=self.filename).grid(column=1, row=1)
        self.user_image = ImageTk.PhotoImage(Image.open(self.filename))
        self.my_image_label = Label(image=self.user_image).grid(column=1, row=2)

    def text_ask(self):
        self.wm_text = simpledialog.askstring("Input", "What is the watermark text?", parent=self.window)

    def save(self):
        # watermark the image
        self.watermark(self.filename)
        # show watermarked image
        self.watermarked_image = ImageTk.PhotoImage(Image.open(f"{self.filename}_watermarked.png"))
        self.wm_image_label = Label(image=self.watermarked_image, text=self.filename).grid(column=3, row=2)


GUI()
