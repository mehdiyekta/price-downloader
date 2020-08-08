# این برنامه شاید روزی بتونه جایگزین مناسبی برای برنامه ی پر باگ
# TSE
# باشه. به هرحال من کامنت های مناسب و کد شفاف و قابل مطالعه ای رو مینویسم شاید عده ای استفاده کردن
# کد » مهدی یکتا
# code by >Mehdi Yekta
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import webbrowser
import bs4
import subprocess
import time
import socket
import re

# چک کردن اتصال به اينترنت
# در صورتي که به اينترنت متصل نباشه با يک ارور خارج ميشه از برنامه
# اگه بدون اينترنت صرفا ميخواي برنامه رو تست کني قسمت
# checkinternet()
# رو کامنت کن
realtimeofuser = time.asctime(time.localtime(time.time()))


def checkinternet():
    try:
        socket.setdefaulttimeout(5)
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        print('internet connection = "OK"')
    except Exception as errorinternetconnection_log:
        with open('log.txt', 'a') as logwriting:
            logwriting.write(
                str('-' * 15) + str(realtimeofuser) + str('-' * 15) + '\n''Error in internet connection:\n' + str(
                    errorinternetconnection_log) + '\n')
            logwriting.close()
        messagebox.showerror('عدم اتصال به اینترنت', 'لطفا از اتصال خود به اینترنت اطمینان حاصل فرمایید')
        exit()


checkinternet()
winmain = tk.Tk()
winmain.resizable(0, 0)
winmain.title('دانلود قیمت سهم ها از سازمان بورس')
labelnamad = ttk.Label(winmain, text=':لطفا نماد مورد نظرتان را وارد کنید')
labelnamad.grid(column=2, row=0)
textnamadvariable = tk.StringVar()
# def namesymboltext():
namesymbol = textnamadvariable.get()
labelnamesymbolcheck = ttk.Label(winmain, text='نامشخص', foreground='red')
labelnamesymbolcheck.grid(column=1, row=2)


def submitbutton():
    namesymbol = textnamadvariable.get()
    if namesymbol == '':
        messagebox.showerror('.توجه', 'لطفا نماد مورد نظر خود را در قسمت مربوطه وارد کنید')
    elif not re.match("^[آ-ی]*$", namesymbol):
        messagebox.showerror('توجه', 'فقط از حروف فارسی استفاده کنید')
        textnamadvariable.set('')
    else:
        labelnamesymbolcheck.config(text='تایید شد-' + str(namesymbol), foreground='green')
        with open('__init__.py', 'a') as writenamesymboloninit:
            writenamesymboloninit.write(str('namesymbol=\n'))
            writenamesymboloninit.close()
        if __name__ == '__main__':
            import priceholder
    # جای این قسمت برای کد بررسی اشتباهه چون بیشتر پارامتر ها برای اینکه بتونم کد بررسی رو بزنم پایین تر از این قرار دارن ولی خب تا وقتی کد بررسی رو نمیدونم
    # قصد جا به جا کردن این قسمت از برنامه و کد رو ندارم


textnamad = ttk.Entry(winmain, textvariable=textnamadvariable)
textnamad.grid(column=1, row=0)
buttonsearch = ttk.Button(winmain, text='بررسی', command=submitbutton)
buttonsearch.grid(column=0, row=0)
labeladdress = ttk.Label(winmain, text=':اطلاعات را در کجا مایلید ذخیره کنید؟')
labeladdress.grid(column=2, row=1)
textaddressvariable = tk.StringVar()
textaddressfilesave = ttk.Entry(winmain, textvariable=textaddressvariable)
textaddressfilesave.grid(column=1, row=1)
labelnamesymbol = ttk.Label(winmain, text=':نام شرکت مربوط به نماد')
labelnamesymbol.grid(column=2, row=2)


def savebuttoncode():
    getaddressfromstringvar = textaddressvariable.get()
    getfromtextsymbol = textnamadvariable.get()
    while True:
        if getfromtextsymbol == '':
            messagebox.showerror('توجه', 'لطفا نام نماد را وارد کنید')
            break
        else:
            getsymboltext = textnamadvariable.get()
            if getaddressfromstringvar != '':
                textaddressvariable.set('')
                messagebox.showwarning('توجه', 'لطفا از وارد کردن دستی آدرس بپرهیزید.')
                directory = filedialog.asksaveasfilename(defaultextension=".cvs", initialfile=getsymboltext, filetypes=(
                ("cvs file | (*.cvs)", "*.cvs"), ("TXT file | (*.txt)", "*.txt")))
                break
                # قسمت مربوط به سیو کردن فایل دانلود شده اینجا قرار میگیره
            else:
                labelnamesymbolcheckdata = labelnamesymbolcheck.cget("text")
                if labelnamesymbolcheckdata == 'نامشخص':
                    messagebox.showerror('توجه', '!لطفا ابتدا نماد را بررسی کنید')
                    break
                else:
                    messagebox.showwarning('توجه', 'محل ذخیره را انتخاب کنید')
                    directory = filedialog.asksaveasfilename(defaultextension=".cvs", initialfile=getsymboltext,
                                                             filetypes=(("cvs File | (*.cvs)", "*.cvs"),
                                                                        ("TXT File | (*.txt)", "*.txt")))
                    textaddressvariable.set(directory)
                    ##اینجا بعد از دستور 
                    ##if ---
                    ##اگر سیو فایل کد هاش به درستی انجام شد پیام زیر رو نشون میده
                    messagebox.showinfo('!موفقیت آمیز بود', 'فایل قیمت ها با موفقیت ذخیره شد')
                    # اگر موفقیت آمیز نبود پیام زیر
                    messagebox.showerror('ناموفق بود',
                                         'متاسفانه عملیات با مشکل مواجه شد لطفا اتصال اینترنت خود را چک کنید یا برنامه را از سایتی که دانلود کردید آپدیت کنید')
                    break


# اینجا چالشی هست که دوستش دارم اینکه بتونم وضعیت نماد رو مشخص کنم.
# باید اطلاعات رو از سایت
# TSE
# بگیره و توسط یک
# .config()
# جای متن قرمز رنگ و پیشفرض قرار بده و رنگ هم سبز بشه
buttonsave = ttk.Button(winmain, text='ذخیره', command=savebuttoncode)
buttonsave.grid(column=0, row=1)


def tsebuttoncode():
    webbrowser.open('http://www.tsetmc.com/')


buttontse = ttk.Button(winmain, text='TSETMC', command=tsebuttoncode)
buttontse.grid(column=1, row=3)


def exitbuttoncode():
    with open('log.txt', 'a') as logonexit:
        logonexit.write(('-' * 54) + '\n' + str('Clean Exit at: ') + str(realtimeofuser) + '\n')
        logonexit.close()
    exit()


buttonexit = ttk.Button(winmain, text='خروج', command=exitbuttoncode)
buttonexit.grid(column=0, row=3)
winmain.mainloop()
