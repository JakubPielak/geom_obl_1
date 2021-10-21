from tkinter import *
def Oblicz(XA, YA, XB, YB, XP, YP):
    try:
        XA = float(XA)
        YA = float(YA)
        XB = float(XB)
        YB = float(YB)
        XP = float(XP)
        YP = float(YP)
    except ValueError:
        return
    determinant = (XA * YB) + (XB * YP) + (XP * YA) - (XP * YB) - (XA * YP) - (XB * YA)
    Label(text = "{:.10f}".format(determinant)).grid(row = 1, column = 6)
    vector = ((XB - XA) * (YP - YA) - (XP - XA) * (YB - YA))
    Label(text = "{:.10f}".format(vector)).grid(row = 2, column = 6)
    roznica = determinant - vector
    Label(text = "{:.10f}".format(roznica)).grid(row = 3, column = 6)


root_window = Tk()
root_window.title("Geometria Obliczeniowa")
root_window.geometry("520x150")
root_window.configure(background="pink")
Label(text = "Nr").grid(row = 0, column = 0)
Label(text = "Wsp.X").grid(row = 0, column = 1)
Label(text = "Wsp.Y").grid(row = 0, column = 2)
Label(text = "A").grid(row = 1, column = 0)
Label(text = "B").grid(row = 2, column = 0)
Label(text = "P").grid(row = 3, column = 0)
wspXA = Entry()
wspXA.grid(row = 1, column = 1)
wspXB = Entry()
wspXB.grid(row = 2, column = 1)
wspXP = Entry()
wspXP.grid(row = 3, column = 1)
wspYA = Entry()
wspYA.grid(row = 1, column = 2)
wspYB = Entry()
wspYB.grid(row = 2, column = 2)
wspYP = Entry()
wspYP.grid(row = 3, column = 2)

fun = lambda:Oblicz(wspXA.get(), wspYA.get(), wspXB.get(), wspYB.get(), wspXP.get(), wspYP.get())

Button(command = fun, text = "Oblicz").grid(row = 2, column = 4)
Label_determinant = Label(text = "Wyznacznik równy:")
Label_determinant.grid(row = 1, column = 5)
Label_iloczynwek = Label(text = "Iloczyn wektorowy równy:")
Label_iloczynwek.grid(row = 2, column = 5)
Label_roznica = Label(text = "Różnica równa:")
Label_roznica.grid(row = 3, column = 5)
root_window.mainloop()
