import tkinter as tk
def calc():
    vhod = entry.get()
    try:
        res = eval(vhod)
        output.config(text="Ответ: " + str(res))
    except:
        output.config(text="Ошибка вычисления")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x200")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Вычислить", command=calc)
button.pack()

output = tk.Label(root, text="")
output.pack(pady=10)

root.mainloop()
