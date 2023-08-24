from tkinter import *
from tkinter import messagebox


def send_message():
    msg = msg_entry.get()
    _msg_label.config(text=msg)
    msg_entry.delete(0,END)
    

root = Tk()
root.title("Pass the message")
root.geometry('700x500')
root.config(bg='cyan')

msg_label = Label(root,text="Type message to send",bg='cyan',font=('ariel',30,'bold'))
msg_label.pack(pady=25)

msg_entry = Entry(root,width=15,font=('ariel',20,'bold'))
msg_entry.pack(pady=10)
msg_entry.focus()

send_btn = Button(root,text="Click to send",font=('ariel',15,'bold'),bg='firebrick2',command=send_message)
send_btn.pack(pady=10)

last_msg_label = Label(root,text="Last message delivered",bg='cyan',font=('ariel',20,'bold'))
last_msg_label.pack(pady=10)

_msg_label = Label(root,text="",bg='cyan',fg='firebrick2',font=('ariel',20,'bold'))
_msg_label.pack(pady=15)




root.mainloop()