import time
import tkinter

root = tkinter.Tk()
root.title('Clock @Ashok')
root.geometry('400x200')
root['bg'] = 'black'

def get_time():
    t = time.localtime()
    l.config(text=time.strftime('%H:%M:%S', t))
    l.after(1000, get_time)


l = tkinter.Label(root,font=('Courier',40,'bold'),pady=50,bg='black',fg='blue')
l.pack()
get_time()
root.mainloop()
