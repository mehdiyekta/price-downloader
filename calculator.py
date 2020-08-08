import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

wincalc = tk.Tk()
wincalc.title('محاسبه گر')
labelaskprice = ttk.Label(wincalc, text=':قیمت اولیه (سر به سر) را وارد کنید')
labelaskprice.grid(column=5, row=0)
entrypricevariable = tk.IntVar()
entryprice = ttk.Entry(wincalc, textvariable=entrypricevariable)
entryprice.grid(column=4, row=0)
labelaskprofit = ttk.Label(wincalc, text=':درصد سود احتمالی را وارد کنید')
labelaskprofit.grid(column=3, row=0)
entryprofitvariable = tk.IntVar()
entryprofit = ttk.Entry(wincalc, textvariable=entryprofitvariable)
entryprofit.grid(column=2, row=0)
labelresult = ttk.Label(wincalc, text=':سود روز اول')
labelresult.grid(column=4, row=1)
labelresultvalue = ttk.Label(wincalc, text='0.0')
labelresultvalue.grid(column=3, row=1)


def calculate():
    firstprice = entrypricevariable.get()
    profitvalue = entryprofitvariable.get()
    if firstprice<=0 :
        messagebox.showerror('خطا','قیمت نمیتواند صفر باشد')
    elif profitvalue==0:
        print('value= \'0\'')
        messagebox.showwarning('توجه','برنامه خود به خود رقم سود را تبدیل میکند اگر دستی تبدیل کردید لطفا مجددا اقدام کنید')
        print(profitvalue)
    elif profitvalue>5:
        messagebox.showerror('خطا','دامنه ی نواسن در بورس ایران بین 5 و -5 میباشد')
    elif profitvalue<-5:
        messagebox.showerror('خطا','دامنه ی نواسن در بورس ایران بین 5 و -5 میباشد')
    elif 0.01<profitvalue<0.09 :
        messagebox.showwarning('توجه','برنامه خود به خود رقم سود را تبدیل میکند اگر دستی تبدیل کردید لطفا مجددا اقدام کنید')
    else:
        calcofprofitvalue = (firstprice * profitvalue) / 100
        labelresultvalue.config(text=calcofprofitvalue)


buttoncalculate = ttk.Button(wincalc, text='محاسبه', command=calculate)
buttoncalculate.grid(column=1, row=2)


def exitcalc():
    with open('log.txt', 'a') as loger:
        loger.write('-' * 53 + '\n' + 'clean exit\n nothing to review ;\')\'' +'\n')
        loger.close()
    exit()


buttonexit_calc = ttk.Button(wincalc, text='خروج', command=exitcalc)
buttonexit_calc.grid(column=2, row=2)
wincalc.mainloop()
