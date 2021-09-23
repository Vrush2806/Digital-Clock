from tkinter import Label,Tk
import time
app_window=Tk()
app_window.title("DIGITAL CLOCK")
app_window.geometry("420x150")
app_window.resizable(1,1)  #for fixed window size (1,1)

text_font=("Calibri",68,'bold')
background="blue"
foreground="orange"
border_width=30

label=Label(app_window,font=text_font,bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)

def clock():
    time_live=time.strftime("%H:%M:%S")  #strftime() returns string of date-time
    label.config(text=time_live)
    label.after(200,clock)   #time in milli seconds & function which shall be called

clock()
app_window.mainloop()
