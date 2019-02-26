import tkinter
import sys
import tkinter.messagebox
class App:

    def __init__(self, master):
		
        frameMaster = tkinter.Frame(master)
        frameMaster.pack()

        frame1 = tkinter.Frame(frameMaster)
        frame1.pack(side = tkinter.LEFT)

        frame2 = tkinter.Frame(frameMaster)
        frame2.pack(side = tkinter.LEFT)

        self.button = tkinter.Button(frame1, text = "QUIT", fg = "red", command=frame1.quit)
        self.button.pack(side = tkinter.TOP)

        self.hi_there = tkinter.Button(frame1, text = "Hello", command=self.say_hi)
        self.hi_there.pack(side = tkinter.TOP)
        
        self.iLikeOnions = tkinter.Button(frame1, text = "onions?", command = self.onions)
        self.iLikeOnions.pack(side = tkinter.TOP)
        
        self.extraQuitButton = tkinter.Button(frame2, text = "SUPER QUIT", fg = "red", command = self.superQuit)
        self.extraQuitButton.pack(side = tkinter.TOP)
        
        self.iLikeCabbage = tkinter.Button(frame2, text = "cabbage?", command = self.cabbage)
        self.iLikeCabbage.pack(side = tkinter.TOP)
        
        self.mushroomKetchup = tkinter.Button(frame2, text = "mushroom ketchup?", command = self.mushroomKetchup)
        self.mushroomKetchup.pack(side = tkinter.TOP)

    def say_hi(self):
        print("hi there, everyone!")
        
    def onions(self):
        tkinter.messagebox.showwarning("I Like Onions!!!!", "Do YOU like onions?")
        
    def cabbage(self):
	    tkinter.messagebox.showwarning("Status of Cabbage", "Cabbage is okay I guess, if you are into that")

    def mushroomKetchup(self):
        tkinter.messagebox.showwarning("Mushroom Ketchup is a real thing", "Disgusting")
        
    def superQuit(self):
	    tkinter.messagebox.showwarning("OKAY FINE GOSH!!!", "QUIT WHY DON'T YOU FRICKING LOSER")
	    tkinter.messagebox.showwarning("HOW MUCH I NEED YOU", "NONE AT ALL, I DON'T NEED YOU")
	    tkinter.messagebox.showwarning("I AM ACTUALLY MAD", "THERE WAS A PERFECTLY ACCEPTABLE NORMAL QUIT BUTTON")
	    tkinter.messagebox.showwarning("DON'T COME CRAWLING BACK TO ME", "WE ARE FREAKING DONE")
	    tkinter.messagebox.showwarning("wait...", "...... hold on..")
	    tkinter.messagebox.showwarning("...", "........")
	    tkinter.messagebox.showwarning("...oh no", ".........I don't know how to quit")
	    tkinter.messagebox.showwarning("oops", "this is embarassing")
	    tkinter.messagebox.showwarning("solutions?", "I guess just use the other quit button")
	    tkinter.messagebox.showwarning("Well bye", "Don't come back")

root = tkinter.Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below

