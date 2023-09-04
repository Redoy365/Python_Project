from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile

root = Tk()
root.geometry('500x300')

def open_file():
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
	if file is not None:
		content = file.read()
		print(content)

btn = Button(root, text ='Open', command = lambda:open_file())
btn.pack(side = TOP, pady = 10)

mainloop()
