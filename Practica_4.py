from tkinter import *
from tkinter import ttk
import time 

class Window:
    def __init__(self,window):
        self.window = window
        self.window.title("Algoritmos de planificacion")
        self.window.geometry("450x350")

        self.Open_File()

        bar_menu = Menu(self.window)

        menu_process = Menu(bar_menu)
        menu_process.add_command(label="Round Robin")
        menu_process.add_command(label="SJF")
        menu_process.add_command(label="FIFO",command=self.FIFO)
        menu_process.add_command(label="Prioridad")
        bar_menu.add_cascade(label="algoritmos", menu=menu_process)

        menu_Add = Menu(bar_menu)
        menu_Add.add_command(label="Agregar",command=self.Add_Process)
        bar_menu.add_cascade(label="Procesos",menu=menu_Add)
        self.window.config(menu=bar_menu)

        self.frame = LabelFrame(self.window,text="PROCESO EN EJECUCION")
        self.frame.place(x=20, y=20,width=410,height=60)
        
        table = ttk.Treeview(self.window, columns=("col1"))
        table.column("#0",width=133)
        table.column("col1", width=133,anchor=CENTER)

        table.heading("#0", text="Proceso",anchor=CENTER)
        table.heading("col1", text="Estado", anchor=CENTER)

        table.place(x=160, y=100)

        Label(self.window, text="-----> Proceso <-----",fg="BLUE").place(x=20,y=100)

        Label(self.window, text="-----> Prioridad <-----",fg="BLUE").place(x=20, y=160)
        
        Label(self.window, text="-----> Tiempo <-----",fg="BLUE").place(x=20, y=220)
    
    def Add_Process(self):
        pass

    def Imprimir(self):
        pass
             
    def Open_File(self):
        with open("procesos.txt","r") as file:
            self.list_process = file.readlines()
    
    def FIFO(self):
        List_Process_FIFO = self.list_process
        while len(List_Process_FIFO) != 0:
            process = List_Process_FIFO[0].split(",")
            load = ""
            lblprocess = Label(self.frame, text=process[0])
            lblprocess.place(x=10, y=3)
            self.window.update()
            for count in range(int(process[2])):
                lblLoad = Label(self.frame, text=load, bg="GREEN",fg="GREEN")
                lblLoad.place(x=200, y=3)
                load = load + " "
                self.window.update()
                time.sleep(1)
                lblLoad.destroy()
            lblprocess.destroy()
            self.window.update()
            List_Process_FIFO.pop(0)

    def Process(self):
        Carga = "."
        for i in range(10):
            lbl = Label(self.frame , text=Carga, bg="GREEN", fg="GREEN").grid(column=0, row=0)
            Carga = Carga + Carga
            self.window.update()
            time.sleep(1)

        


if __name__ == "__main__":
    ventana = Tk()
    apliaction = Window(ventana)
    ventana.mainloop()