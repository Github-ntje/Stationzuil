from tkinter import *

def onclick():
    label["text"] = entry.get()

root = Tk()
root.geometry("100x100")
# root.config(bg='yellow')
# img = PhotoImage(file='C:/Users/Zeliha/Downloads/img_faciliteiten/img_lift.png')
# LBL = Label(image=img).pack()
label = Label(master=root,
              text='Welkom Naoual',

              background='LightPink3',

              foreground='gray1')

entry = Entry(master=root)
button = Button(master=root, text='Press', command=onclick)
label.pack()
entry.pack()
button.pack(pady=10)
root.mainloop()