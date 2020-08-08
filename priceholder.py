import tkinter as tk
from tkinter import ttk
import time

# import __init__
realtimeofuser = time.asctime(time.localtime(time.time()))
winprice = tk.Tk()
winprice.title("جدول قیمت ها")
winprice.resizable(0, 0)
labelintro = ttk.Label(winprice, text=':جدول معرفی قیمت سهم')
labelintro.grid(column=3, row=0)
# namesymbol=
# labelsymboltext=ttk.Label(winprice,text=namesymbol)
# labelsymboltext.grid(column=2,row=0)
labelpricebeggining = ttk.Label(winprice, text=':قیمت شروع(اولیه)در بازار')
labelpricebeggining.grid(column=3, row=1)
labelpricebegginingnumber = ttk.Label(winprice, text="در این قسمت قیمت اولیه ی سهام قرار میگیرد", foreground='Green')
labelpricebegginingnumber.grid(column=2, row=1)
labelpriceopening = ttk.Label(winprice, text=':قیمت باز شدن سهم')
labelpriceopening.grid(column=3, row=2)
labelpriceopeningnumber = ttk.Label(winprice, text='در این قسمت قیمت باز شدن سهم در بازار قرار میگیرد',
                                    foreground='Green')
labelpriceopeningnumber.grid(column=2, row=2)
labelpricelast = ttk.Label(winprice, text=':قیمت نهایی یا پایانی')
labelpricelast.grid(column=3, row=3)
labelpricelastnumber = ttk.Label(winprice, text='دراین قسمت قیمت نهایی سهم نمایش داده میشود', foreground='green')
labelpricelastnumber.grid(column=2, row=3)
labelpriceclosing = ttk.Label(winprice, text=':قیمت بسته شدن سهم')
labelpriceclosing.grid(column=3, row=4)
labelpriceclosingnumber = ttk.Label(winprice, text='در این قسمت قیمت بسته شدن سهم قرار میگیرد', foreground='green')
labelpriceclosingnumber.grid(column=2, row=4)


def calculatecode():
    import calculator


buttoncalculator = ttk.Button(winprice, text='محاسبه گر', command=calculatecode)
buttoncalculator.grid(column=3, row=5)


def buttonexitcode():
    with open('log.txt', 'a') as logwriting:
        logwriting.write('\n' + 'Exit at ' + str(realtimeofuser) + '\n' + str('-' * 53))
        logwriting.close()
    exit()


buttonexit = ttk.Button(winprice, text='خروج', command=buttonexitcode)
buttonexit.grid(column=0, row=5)
winprice.mainloop()
