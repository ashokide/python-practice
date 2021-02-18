import time
from tkinter import *
from tkinter import messagebox

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

window = Tk()
window.title('Whatsapp Automation')
window.geometry('300x150')

name = StringVar()
message = StringVar()
iterate = IntVar()


def whatsappAutomation():
    try:
        userName = name.get()
        msg = message.get()
        count = iterate.get()
        root = wd.Chrome(executable_path=r'F:\pythonProjects\projects\chromedriver.exe')
        root.get('https://web.whatsapp.com/')
        root.maximize_window()
        time.sleep(10)

        user = root.find_element_by_xpath('//span[@title="{}"]'.format(userName))
        user.click()

        for i in range(1, count):
            msg_box = root.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
            msg_box.send_keys(msg)
            msg_box.send_keys(Keys.RETURN)
            # time.sleep(1)

    except Exception as e:
        messagebox.showinfo('Error Occurred', e)
        root.close()
        window.quit()

    finally:
        root.close()

    lblName.configure(text=' ')
    lblMsg.configure(text=' ')
    lblCount.configure(text=' ')
    messagebox.showinfo('Success', 'Message Sent Successfully')
    window.quit()


lblName = Label(window, text='Name:', font=('Arial', 10))
lblName.grid(row=0, column=0)
lblMsg = Label(window, text='Message:', font=('Arial', 10))
lblMsg.grid(row=1, column=0)
lblCount = Label(window, text='Count:', font=('Arial', 10))
lblCount.grid(row=2, column=0)

Label(window,text='©Ashok',bg='black',fg='white',width=20,anchor=CENTER).grid(row=5,column=1)

Entry(window, text=name).grid(row=0, column=1)
Entry(window, text=message).grid(row=1, column=1)
Entry(window, text=iterate).grid(row=2, column=1)
Button(window, text='Send Message', font=('Arial', 12), command=whatsappAutomation).grid(row=3, column=1)

window.mainloop()
