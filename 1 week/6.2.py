from tkinter import *
from tkinter import ttk
root = Tk()
def calculate(*args):
    try:
        value1 = float(weight.get())
        value2 = float(height.get())
        res = round(float(value1 / value2 ** 2), 2)
        imt.set(res)
        if res <= 16:
            verdict = "Выраженный дефицит массы тела"
        elif 16 < res < 18.5:
            verdict = "Недостаточная (дефицит) масса тела"
        elif 18.5 <= res < 25:
            verdict = "Норма"
        elif 25 <= res < 30:
            verdict = "Избыточная масса тела (предожирение)"
        elif 30 <= res < 35:
            verdict = "Ожирение 1 степени"
        elif 35 <= res < 40:
            verdict = "Ожирение 2 степени"
        else:
            verdict = "Ожирение 3 степени"
        imt_verdict.set(verdict)

    except ValueError:
        pass

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

weight = StringVar()
height = StringVar()
weight_entry = ttk.Entry(mainframe, width=6, textvariable=weight)
height_entry = ttk.Entry(mainframe, width=6, textvariable=height)
weight_entry.grid(column=2, row=1, sticky=(W, E))
height_entry.grid(column=2, row=2, sticky=(W, E))

imt = StringVar()
ttk.Label(mainframe, textvariable=imt).grid(column=3, row=3, sticky=(W, E))
imt_verdict = StringVar()
ttk.Label(mainframe, textvariable=imt_verdict).grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Узнать результат", command=calculate).grid(column=3, row=5, sticky=W)

ttk.Label(mainframe, text="кг").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="м").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Введите ваш вес: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Введите ваш рост: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Индекс массы тела: ").grid(column=1, row=3, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", calculate)

root.mainloop()

