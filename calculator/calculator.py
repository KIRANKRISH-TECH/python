import tkinter as tk

def click_button(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")


display = tk.Entry(root, width=16, font=("Arial", 24), bd=4, relief=tk.RIDGE, justify='right')
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        action = clear_display
    else:
        action = lambda x=text: click_button(x)
    tk.Button(root, text=text, width=4, height=2, font=("Arial", 18), command=action).grid(row=row, column=col, sticky="nsew")


tk.Button(root, text='=', width=4, height=2, font=("Arial", 18), command=calculate).grid(row=5, column=0, columnspan=4, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

