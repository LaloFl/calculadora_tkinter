import tkinter as tk
import tkinter.font as font

def calc(txt, elX, elY):
    resStr = ""
    x = elX.get('1.0', 'end-1c')
    y = elY.get('1.0', 'end-1c')
    try:
        x = float(x)
        y = float(y)
    except Exception:
        return False
        
    if txt == "Suma (+)":
        resStr = f"{x} + {y} = {x + y}"
    elif txt == "Resta (-)":
        resStr = f"{x} - {y} = {x - y}"
    elif txt == "Multiplicación (*)":
        resStr = f"{x} * {y} = {x * y}"
    elif txt == "División (/)":
        resStr = f"{x} / {y} = {x / y}"
    else:
        return False
    
    _ = tk.Label(root, text="Resultado", font=font.Font(size=14, weight="bold"))
    _.place(x=30, y=150)

    _ = tk.Label(root)
    _.place(x=140, y=152, width=400, height=200)

    lblRes = tk.Label(root, text=resStr, font=font.Font(size=13))
    lblRes.place(x=140, y=152)
    

def create_button(txt, x, y, w, h, cmd, elX, elY):
    newB = tk.Button(root, text=txt, command=lambda:cmd(txt, elX, elY), font=font.Font(size=10, weight="bold"))
    newB.place(x=x, y=y, width=w, height=h)
    return newB

def create_input(lbl, x, y, w, h):
    newL = tk.Label(root, text=lbl)
    newL.place(x=x, y=y, width=30)
    root.update()
    lblw = newL.winfo_width()
    newI = tk.Text(root)
    newI.place(x=x+lblw, y=y, width=w, height=h)
    return newI

def draw_layout():
    title = tk.Label(root, text="Calculadora básica", font=font.Font(size=20, weight="bold"))
    title.place(x=10, y=10)

    txtX = create_input(lbl="X = ", x=10, y=70, w=80, h=22)
    txtY = create_input(lbl="Y = ", x=10, y=100, w=80, h=22)

    btnSum = create_button(txt="Suma (+)", x=140, y=70, w=120, h=25, cmd=calc, elX=txtX, elY=txtY)
    btnRes = create_button(txt="Resta (-)", x=270, y=70, w=120, h=25, cmd=calc, elX=txtX, elY=txtY)
    btnMul = create_button(txt="Multiplicación (*)", x=140, y=100, w=120, h=25, cmd=calc, elX=txtX, elY=txtY)
    btnDiv = create_button(txt="División (/)", x=270, y=100, w=120, h=25, cmd=calc, elX=txtX, elY=txtY)

root = tk.Tk()
root.geometry("400x193")
root.resizable(False, False)
root.title("Calculadora (Diego Flores #19211641)")

draw_layout()
root.mainloop()