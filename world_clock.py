from tkinter import Label, Tk
import time
from datetime import datetime
import pytz
print("Enter country such as USA, India, Australia or Brazil")
location=input()

if location=="India":
    app_window = Tk()
    app_window.title("Digital Time")
    app_window.geometry("600x600")
    app_window.resizable(0,0)
    text_font= ("Boulder", 68, 'bold')
    background = "#F5F7F7"
    foreground= "#7473BF"
    border_width = 25
    label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
    label.grid(row=1, column=1)
    name=Label(app_window,text="Time in India",font=("Boulder", 25, 'bold'))
    name.place(x=20,y=200)
    def digital_clock():
        time_live = time.strftime("%H:%M:%S")
        label.config(text=time_live)
        label.after(200, digital_clock)
    digital_clock()
    app_window.mainloop()
if location=="USA":
    app_window = Tk()
    app_window.title("Digital Time")
    app_window.geometry("600x600")
    app_window.resizable(0,0)
    text_font= ("Boulder", 68, 'bold')
    background = "#F5F7F7"
    foreground= "#7473BF"
    border_width = 25
    label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
    label.grid(row=1, column=1)
    name=Label(app_window,text="Time in USA",font=("Boulder", 25, 'bold'))
    name.place(x=20,y=200)
    def digital_clock():
      a=pytz.timezone('America/Los_Angeles')
      t=datetime.now(a)
      c=t.strftime("%H:%M:%S")
      label.config(text=c)
      label.after(200, digital_clock)
    digital_clock()
    app_window.mainloop()
if location=="Australia":
    app_window = Tk()
    app_window.title("Digital Time")
    app_window.geometry("600x600")
    app_window.resizable(0,0)
    text_font= ("Boulder", 68, 'bold')
    background = "#F5F7F7"
    foreground= "#7473BF"
    border_width = 25
    label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
    label.grid(row=1, column=1)
    name=Label(app_window,text="Time in Australia",font=("Boulder", 25, 'bold'))
    name.place(x=20,y=200)
    def digital_clock():
      a=pytz.timezone('Australia/Victoria')
      t=datetime.now(a)
      c=t.strftime("%H:%M:%S")
      label.config(text=c)
      label.after(200, digital_clock)
    digital_clock()
    app_window.mainloop()
if location=="Brazil":
    app_window = Tk()
    app_window.title("Digital Time")
    app_window.geometry("600x600")
    app_window.resizable(0,0)
    text_font= ("Boulder", 68, 'bold')
    background = "#F5F7F7"
    foreground= "#7473BF"
    border_width = 25
    label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
    label.grid(row=1, column=1)
    name=Label(app_window,text="Time in Brazil",font=("Boulder", 25, 'bold'))
    name.place(x=20,y=200)
    def digital_clock():
      a=pytz.timezone('Brazil/East')
      t=datetime.now(a)
      c=t.strftime("%H:%M:%S")
      label.config(text=c)
      label.after(200, digital_clock)
    digital_clock()
    app_window.mainloop()
