import tkinter as tk
from PIL import Image, ImageTk
from itertools import count


window = tk.Tk()
window.title("Authentication")
window.configure(background='white')


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
    foreground="black",
    background="white",
    width=100,
    height=2,
    font=("Arial Bold", 25)
).pack()
lbl = ImageLabel(window)
lbl.pack(fill=tk.Y)
lbl.load('./loading.gif')

window.mainloop()

# lazem a square for cam video
# lazem

