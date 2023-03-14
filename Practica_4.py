from tkinter import *
from tkinter import ttk
import time 

class Window:
    def __init__(self,window):
        self.window = window
        self.window.title("Algoritmos de planificacion")
        self.window.geometry("450x350")

        self.frame = LabelFrame(self.window,text="PROCESO EN EJECUCION")
        self.frame.place(x=20, y=50,width=410,height=60)
       
        btnStart = Button(self.window, text="Iniciar",command=self.Imprimir).place(x=30,y=10)
        
        table = ttk.Treeview(self.window, columns=("col1"))
        table.column("#0",width=133)
        table.column("col1", width=133,anchor=CENTER)

        table.heading("#0", text="Proceso",anchor=CENTER)
        table.heading("col1", text="Estado", anchor=CENTER)

        table.place(x=160, y=120)

        Label(self.window, text="-----> Proceso <-----",fg="BLUE").place(x=20,y=120)

        Label(self.window, text="-----> Prioridad <-----",fg="BLUE").place(x=20, y=180)
        
        Label(self.window, text="-----> Tiempo <-----",fg="BLUE").place(x=20, y=240)

        self.Loading = "."

    def Imprimir(self):
        list_process = self.Open_File()
        self.FIFO()
             
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
                lblLoad = Label(self.frame, text=f"{load} segundo: {count + 1}", bg="GREEN",fg="BLACK")
                lblLoad.place(x=200, y=3)
                load = load + self.Loading
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