import tkinter

counter = 0
# create a gui
window = tkinter.Tk()
window.title('Text Disappearing App')
window.geometry("500x500")
window.configure(bg="pink")


# create the clearing method
def text_disappeared():
    textbox.delete(1.0, tkinter.END)
    textbox.insert(tkinter.END, "")


# create the disappear method
def writing_stopped():
    global counter, text
    if text == textbox.get(1.0, tkinter.END):
        if counter == 10:
            window.after(1000, text_disappeared)
            counter = -1
        window.after(1000, writing_stopped)
        counter += 1
    else:
        window.after(1000, writing_stopped)
        text = textbox.get(1.0, tkinter.END)
        counter = 0


# create an text box
text = ""
textbox = tkinter.Text(window, height=20, width=65)
textbox.grid(row=2, column=1, padx=10, pady=10)

#create a label
label = tkinter.Label(window, text="If you stop writing, you lose everything!")
label.grid(row=5, column= 1)

window.after(1000, func=writing_stopped)
window.mainloop()
