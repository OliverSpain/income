import app
import tkinter as tk
from sys import exit

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Worker Database")
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.text = tk.Text(self.frame, height = 15, width = 50)
        self.text.pack(side = tk.BOTTOM, padx = 10, pady = 10)

        self.button1 = tk.Button(self.frame, text ="Input data", command = lambda : self.newwindow())
        self.button1.pack(side = tk.LEFT, padx = 40, pady = 10)
        
        self.button2 = tk.Button(self.frame, text ="Show data", command = lambda : self.output())
        self.button2.pack(side = tk.LEFT, padx = 40, pady = 10)
        
        self.button3 = tk.Button(self.frame, text ="End program", command = lambda : self.end())
        self.button3.pack(side = tk.LEFT, padx = 40, pady = 10)

    def newwindow(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = InputWindow(self.newWindow)

    def output(self):
        content = app.dataimport("data.csv")
        content.append(app.dataimport("temp.csv"))
        strip = ((str(content).replace("), (", "\n")).replace("'", "")).strip("()[], ")
        final = strip.replace("), [(", "\n")
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", final) 

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
