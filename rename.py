import os
import tkinter as tk
import tkinter.filedialog

root = tk.Tk()
root.title("The Renamer")
root.iconphoto(False, tk.PhotoImage(file='C:/Users/Lenovo/Documents/LearnCode/The Renamer/icon.png'))

def setTextInput(text):
    loc.delete(0, 'end')
    loc.insert(0, text)

def selector():
    global path
    path = tk.filedialog.askdirectory()
    setTextInput(path)

def rename():
    try:
        global temp
        temp=os.listdir(path)
        temp1=[]
        ext=""
        for i,txt in enumerate(temp):
            ext=txt[txt.rfind('.'):]
            temp1.append("Episode "+str(i+1)+ext)
        for u,v in zip(temp,temp1):
            src=path+"\\"+u
            dest=path+"\\"+v
            os.rename(src,dest)
    except:
        setTextInput("Select a Location First")
    
def undo():
    try:
        temp1=[]
        ext=""
        for i,txt in enumerate(temp):
            ext=txt[txt.rfind('.'):]
            temp1.append("Episode "+str(i+1)+ext)
        for u,v in zip(temp1,temp):
            src=path+"\\"+u
            dest=path+"\\"+v
            os.rename(src,dest)
    except:
        setTextInput("There is nothing to undo")
        
loc=tk.Entry(root, width=60, bd=2)
loc.grid(row=0,column=0,columnspan=3,ipady=5)
select = tk.Button(root, text="Select Location", width=20, bd=4, command=selector).grid(row=0,column=3)
rename = tk.Button(root, text="Rename", width=40, pady=10, bd=4, command=rename).grid(row=1,column=0,columnspan=2)
undo = tk.Button(root, text="Undo", width=40, pady=10, bd=4, command=undo).grid(row=1,column=2,columnspan=2)
root.attributes('-topmost', True)



root.mainloop()