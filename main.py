# import tkinter
from tkinter import *
from tkinter import ttk 

# colors
color1 = "#302d2d" # balck
color2 = "#feffff" # withe
color3 = "#38576b" # blue
color4 = "#eceff1" # grey
color5 = "#ffab40" # orange

window =Tk()
window.title("calculator")
window.geometry("235x310")
window.config(bg=color1)


# frame
frame_screen = Frame(window, width=235, height=50, bg=color3)
frame_screen.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)

# label
text_value = StringVar()

# all values variable
all_values = ''

# function
def into_value(value):
    global all_values
    all_values = all_values + str(event)

    #result in screen
    text_value.set(all_values)

# calc function
def calc():
    global all_values
    result = eval(all_values)
    print(result)

    text_value.set(str(result))

# clear function
def clear_screen():
    global all_values
    all_values =""
    text_value.set("")

app_label = Label(frame_screen, textvariable=text_value, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=color3, fg=color2)
app_label.place(x=0, y=0)


# button
b_1 = Button(frame_body, command = clear_screen ,text="C", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_body, command = lambda: into_value('%') ,text="%", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_body, command = lambda: into_value('/') ,text="/", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=176, y=0)

b_4 = Button(frame_body, command = lambda: into_value('7') ,text="7", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_body, command = lambda: into_value('8') ,text="8", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_body, command = lambda: into_value('9') ,text="9", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_body, command = lambda: into_value('*') ,text="*", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=176, y=52)

b_8 = Button(frame_body, command = lambda: into_value('4') ,text="4", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_body, command = lambda: into_value('5') ,text="5", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_body, command = lambda: into_value('6') ,text="6", width=5, height=2, bg=color4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_body, command = lambda: into_value('-') ,text="-", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=176, y=104)

b_12 = Button(frame_body, command = lambda: into_value('3') ,text="3", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_body, command = lambda: into_value('2') ,text="2", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_body, command = lambda: into_value('1') ,text="1", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_body, command = lambda: into_value('+') ,text="+", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=176, y=156)

b_16 = Button(frame_body, command = lambda: into_value('0') ,text="0", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_body, command = lambda: into_value('.') ,text=".", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_body, command = calc ,text="=", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=176, y=208)


window.mainloop()