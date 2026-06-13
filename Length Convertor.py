from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("Length Convertor")
root.geometry("400x400")
frame=Frame(master=root, height=200, width=360, bg='white')

lbl1=Label(frame, text="length in inches", bg="light green", fg="black", width="12")

length_entry=Entry(frame)

def display():
    inch=length_entry.get()
    inches=int(inch)
    cm=inches*2.547
    answer="Your answer is "+str(cm)
    textbox.insert(END, answer)

def msg():
    messagebox.showwarning("Succesful", "This is accurate because 1 inch is equal to 2.547 cm")

textbox=Text(bg="light blue")

btn2=Button(root, text="Accuracy", command=msg, bg='pink' )

btn=Button(text="Convert", command=display, bg='blue', fg="white")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
length_entry.place(x=150, y=20)
btn.place(x=130, y=210)
btn2.place(x=130, y=240)
textbox.place(y=280)

root.mainloop()