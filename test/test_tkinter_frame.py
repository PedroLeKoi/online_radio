
#from tkinter import *
import Tkinter



class Application(Tkinter.Frame):
    """docstring"""
    
    def __init__(self, master=None):
        """docstring"""
        
        Tkinter.Frame.__init__(self, master)
        
        self.grid()
        self.master.title("Grid Manager")
        
        # Variables
        lst_btns = []
        
        for int_row in range(6):
            self.master.rowconfigure(int_row, weight=1)
        for int_col in range(5):
            self.master.columnconfigure(int_col, weight=1)
            lst_btns.append(
                Tkinter.Button(master, text="Button {0}".format(int_col))
            )
            lst_btns[int_col].grid(
                row=6,
                column=int_col,
                sticky=Tkinter.E+Tkinter.W
            )
        
        # Frame upper left corner
        frm_up_le = Tkinter.Frame(master, bg="red")
        frm_up_le.grid(
            column=0,
            columnspan=2,
            row=0, 
            rowspan=3,
            sticky=Tkinter.W+Tkinter.E+Tkinter.N+Tkinter.S
        )
        # Frame lower left corner
        frm_low_le = Tkinter.Frame(master, bg="blue")
        frm_low_le.grid(
            column=0,
            columnspan=2,
            row=3,
            rowspan=3,
            sticky=Tkinter.W+Tkinter.E+Tkinter.N+Tkinter.S
        )
        # Frame right
        frm_ri = Tkinter.Frame(master, bg="green")
        frm_ri.grid(
            column=2,
            columnspan=3,
            row=0,
            rowspan=6,
            sticky=Tkinter.W+Tkinter.E+Tkinter.N+Tkinter.S
        )



root = Tkinter.Tk()
root.geometry("400x200+200+200")

app = Application(master=root)
app.mainloop()
