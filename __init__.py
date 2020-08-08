

Bank={'Webmelat':'وبملت'}
Car={'saipa':'خساپا','khegostar':'خگستر'}

#test
import tkinter as tk
from tkinter import ttk
win=tk.Tk()
a=ttk.Label(win,text=Bank['Webmelat'])
a.grid()
b=ttk.Label(win,text=Car['saipa'])
b.grid()
win.mainloop()
#  model:
#a=input('صنعت:')
#b=input('نماد')
#c=print(a[b])
################################
    if str(firstprice) == '':
        messagebox.showerror('توجه', 'لطفا قیمت را وارد کنید')
        entrypricevariable.set(float('0'))
    else:
        print('str price = OK!')
    if float(firstprice) <= int(0):
        messagebox.showerror('توجه', 'قیمت وارد شده اشتباه است')
    else:
        print('float price = OK!')
    if str(profitvalue) == '':
        messagebox.showerror('توجه', 'لطفا درصد سود یا زیان احتمالی را وارد کنید')
    else:
        print('str profit = OK!')
    if float(profitvalue) > int(5):
        messagebox.showerror('توجه', 'دامنه ی نوسان قیمت در ایران بین مثبت و منفی 5 میباشد')
        entryprofitvariable.set(float('0'))
    elif 0.001 < float(profitvalue) < 0.09:
        messagebox.showwarning('توجه',
                               'توجه کنید نیازی به وارد کردن به صورت درصدی نیست مثال صحیح:5 و یا -3 مثال غلط:0.05 و '
                               'یا 0.09 ')
    else:
namesymbol=
namesymbol=
namesymbol=
namesymbol=
namesymbol=
