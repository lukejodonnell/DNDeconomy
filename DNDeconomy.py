import tkinter
import sys
class App:

    def __init__(self, master):

        frame = tkinter.Frame(master)
        frame.pack()

        self.button = tkinter.Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=tkinter.LEFT)

        self.hi_there = tkinter.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tkinter.LEFT)

    def say_hi(self):
        print("hi there, everyone!")
#here are my edits ian is dumb and I am cool
root = tkinter.Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below


print("hello")

