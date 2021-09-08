from tkinter import *
import random
from tkinter.ttk import Separator
import webbrowser


def randomize():
    a1 = format(random.randint(0, 99), '02d')
    ranNumber1.config(text=a1)
    a1 = format(random.randint(0, 99), '02d')
    ranNumber2.config(text=a1)
    a1 = format(random.randint(0, 99), '02d')
    ranNumber3.config(text=a1)
    a1 = format(random.randint(0, 99), '02d')
    ranNumber4.config(text=a1)
    a1 = format(random.randint(0, 99), '02d')
    ranNumber5.config(text=a1)
    a1 = format(random.randint(0, 99), '02d')
    ranNumber6.config(text=a1)


    # This function does something now^^
    # Rendering a top level about window. I'll consider
    # refactoring it
def about_window():
    file_win = Toplevel(window)
    file_win.title("About")
    file_win.geometry("400x100")
    file_win.resizable(False, False)

    about_win = Label(file_win, wraplength=380, text="I wrote this just for fun. It just randomizes 6 numbers that are no larger than 2 digits")
    about_win.config(font=('', 10), fg="black")
    about_win.place(rely=0.1, relx=0.03)

    about_separator = Separator(file_win, orient='horizontal')
    about_separator.place(relx=0, rely=0.65, relwidth=1)

    auth_name = Label(file_win, text="Written by Andrew:")
    auth_name.config(font=('', 10), fg="black")
    auth_name.place(rely=0.70, relx=0.03)

    github_repo = Label(file_win, text="https://github.com/itsportspe/randomgenpy", cursor="hand2")
    github_repo.config(font=('', 10), fg="blue")
    github_repo.place(rely=0.70, relx=0.33)
    github_repo.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/itsportspe/randomgenpy"))


window = Tk()

# This is the menu bar at the top of the app
menubar = Menu(window)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about_window)
menubar.add_cascade(label="Help", menu=helpmenu)
# End menu bar

window.title("Random Number Generator")
window.geometry("660x150")
window.resizable(False, False)
button = Button(window, text="Randomize")
button.config(command=randomize)
ranNumber1 = Label(window, text="")
ranNumber1.config(font=('', 55))
ranNumber1.place(x=10, y=10)

ranNumber2 = Label(window, text="")
ranNumber2.config(font=('', 55))
ranNumber2.place(x=110, y=10)

ranNumber3 = Label(window, text="")
ranNumber3.config(font=('', 55))
ranNumber3.place(x=220, y=10)

ranNumber4 = Label(window, text="")
ranNumber4.config(font=('', 55))
ranNumber4.place(x=330, y=10)

ranNumber5 = Label(window, text="")
ranNumber5.config(font=('', 55))
ranNumber5.place(x=440, y=10)

ranNumber6 = Label(window, text="")
ranNumber6.config(font=('', 55))
ranNumber6.place(x=550, y=10)

separator = Separator(window, orient='horizontal')
separator.place(relx=0, rely=0.65, relwidth=1)
button.place(relx=0.45, rely=0.74)

github_repo = Label(window, text="GitHub", cursor="hand2")
github_repo.config(font=('', 10), fg="blue")
github_repo.place(rely=0.747, relx=0.91)
github_repo.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/itsportspe/randomgenpy"))

# hello_message = tkinter.Message(window,)
window.config(menu=menubar)
window.mainloop()
