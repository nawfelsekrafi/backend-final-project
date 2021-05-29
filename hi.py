import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
from tkinter import scrolledtext as st

window = tk.Tk()
window.title("Authentication")
window.configure(background='black')
window.geometry('2600x900')
window.iconphoto(False, tk.PhotoImage(file='./assets/school-bus.png'))
class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""

    def load(self, im):

        if isinstance(im, str):
            im = Image.open(im)

        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


authentication = tk.Label(
    text="Authentication Operation is in Progress",
    foreground="white",
    background="black",
    font=("Arial Bold", 20)
).grid(row = 0,column = 2,sticky=tk.N, padx=100, pady=5 )
lbl = ImageLabel(window)
lbl.grid(row = 1,column = 2,padx=100)
lbl.load('./assets/loading.gif')

# Printing Students Names
text_area = st.ScrolledText(window,
                            foreground="white",
                            background="black",
                            width=25,
                            height=8,
                            font=("Times New Roman",
                                  15))

# Recognized Students
tk.Label(window,
         text = "Recognized Students",
         font = ("Times New Roman", 15),
         background = 'black',
         foreground = "#90ee90").grid(row = 2,column = 0, columnspan=2, padx=50, pady=5)
tab = ["Nawfel Sekrafi", "Marwen Shili", "Ahmed Hmoudi","Nawfel Sekrafi", "Marwen Shili", "Ahmed Hmoudi"]

for n in tab:
    text_area.insert(tk.INSERT,
                """
                 {fname}
                 """
                 .format(fname=n))


# Making the text read only
text_area.configure(state='disabled')
text_area.grid(row = 3,column = 0, sticky=tk.W, pady=5)

# Unrecognized Students
tk.Label(window,
         text = "Unrecognized Students",
         font = ("Times New Roman", 15),
         background = 'black',
         foreground = "red").grid(row = 2,column = 3, columnspan=2, padx=0, pady=5)

text_area1 = st.ScrolledText(window,
                            foreground="white",
                            background="black",
                            width=25,
                            height=8,
                            font=("Times New Roman",
                                  15))

for n in tab:
    text_area1.insert(tk.INSERT,
                """
                 {fname}
                 """
                 .format(fname=n))
# Making the text read only
text_area1.configure(state='disabled')
text_area1.grid(row = 3,column = 3,sticky=tk.W, pady=5)
"""
text = tk.Text(window)
img = Image.open("./images/23232355.jpg")
image = img.resize((200, 150), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(image)

text.image_create("current",image=photoImg)
text.grid(row=4,column=0)
"""
window.mainloop()

# lazem a square for cam video
# lazem
