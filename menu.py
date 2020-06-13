import app
import tkinter as tk
from sys import exit

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Worker Database")
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.text = tk.Text(self.frame, height = 30, width = 105)
        self.text.pack(side = tk.BOTTOM, padx = 10, pady = 10)

        self.button1 = tk.Button(self.frame, text ="Input data", command = lambda : self.newwindow())
        self.button1.pack(side = tk.LEFT, padx = 105, pady = 10)
        
        self.button2 = tk.Button(self.frame, text ="Show data", command = lambda : self.output())
        self.button2.pack(side = tk.LEFT, padx = 105, pady = 10)
        
        self.button3 = tk.Button(self.frame, text ="End program", command = lambda : self.end())
        self.button3.pack(side = tk.LEFT, padx = 105, pady = 10)

    def newwindow(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = InputWindow(self.newWindow)

    def formatoutput(self, a):
        l = a[-1]
        if len(l) == 0: a.pop()
        i = []
        for x in a:
            j = "{q} has worked {w} hours and earned ${e}, ${r} of which is taxed leaving ${t}.".format(
                q = x[0],
                w = x[1],
                e = x[2],
                r = x[3],
                t = x[4]
            )
            i.append(j)
        b = (str(i).replace("', '", "\n")).strip("[']")
        return b

    def output(self):
        content = app.dataimport("data.csv")
        tempcontent = app.dataimport("temp.csv")
        for x in tempcontent: content.append(x)
        finalstr = self.formatoutput(content)
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", finalstr) 

    def end(self):
        app.clear()
        exit()

class InputWindow():
    def __init__(self, master):
        self.master = master
        self.master.title("Input data")
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.entry1 = tk.Entry(self.master)
        self.entry1.pack(side = tk.TOP, padx = 40, pady = 10)

        self.entry2 = tk.Entry(self.master)
        self.entry2.pack(side = tk.TOP, padx = 40, pady = 10)

        self.button1 = tk.Button(self.master, text="Submit", command = lambda : self.getdata())
        self.button1.pack(side = tk.TOP, padx = 40, pady = 10)

    def getdata(self):  
        inputname = self.entry1.get()
        inputhours = self.entry2.get()
        app.userinput(inputname,inputhours)
        self.closewindow()

    def closewindow(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
