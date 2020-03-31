import tkinter as tk

# create basic GUI window
window=Tk()

# creating button
button=Button()
button.pack()
button["text"] = "Tips in Python"

# button interactions
def click():
    print("Hello Python!")

def click_and_show_in_window():
    content = '''Beautiful is better than ugly.
                Explicit is better than implicit.
                Simple is better than complex.
                Complex is better than complicated.'''
    Label(window, text = content, fg="red").pack()

button["command"]=click_and_show_in_window

# prevent window closeing
window.mainloop()
