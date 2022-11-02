import tkinter as tk
import tkinter.font as font

def test(txt):
    print(txt)

def create_button(txt, cmd, x, y):
    w=3
    h=4 if txt=="=" else 1
    rs =3 if txt=="=" else 1
    newB = tk.Button(root, text=txt, command=lambda:cmd(txt), width=w, height=h, font=font.Font(size=19))
    newB.grid(rowspan=rs, row=y, column=x)

def draw_layout():
    create_button("+", test, 1, 1)
    create_button("-", test, 2, 1)
    create_button("*", test, 3, 1)
    create_button("/", test, 4, 1)
    create_button("=", test, 4, 2)
    c = 0
    for i in range(3):
        for j in range(3):
            create_button(str(c), test, j+1, i+2)
            c += 1


root = tk.Tk()
root.geometry("400x193")
root.resizable(False, False)
root.title("Calculadora (Diego Flores #19211641)")

draw_layout()
root.mainloop()