from tkinter import *
from tkinter import ttk
import time 

class Window:
    def __init__(self,window):
        self.window = window
        self.window.title("Algoritmos de planificacion")
        self.window.geometry("450x350")

        self.band_add = False

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
        window_add = Tk()
        window_add.title("Agregar")
        window_add.geometry("300x250")
        Label(window_add, text="Nombre de proceso").place(x=10,y=10)
        self.txtProcess = Entry(window_add, width=20)
        self.txtProcess.place(x=10,y=40)
        Label(window_add, text="Prioridad").place(x=10,y=70)
        self.txtPriority = Entry(window_add, width=10)
        self.txtPriority.place(x=10, y=100)
        Label(window_add, text="Tiempo").place(x=10,y=130)
        self.txtTime = Entry(window_add, width=10)
        self.txtTime.place(x=10, y=160)
        Label(window_add, text="Posicion").place(x=10, y=190)

        variable = StringVar()
        self.option = ttk.Combobox(window_add, width=17,textvariable=variable)
        self.option["values"] = ("Al final","Al principio")
        self.option.place(x=10,y=220)
        self.option.current(0)

        btnAdd_process = Button(window_add, text="Agregar",command=self.new_process)
        btnAdd_process.place(x=200,y=20)

        window_add.mainloop

    def new_process(self):
        self.new = self.txtProcess.get() + "," + self.txtPriority.get() + "," + self.txtTime.get()
        self.band_add = True

    def current_list(self,list_process):
        if self.option.get() == "Al final":
            list_process.append(self.new)
            return list_process
        elif self.option.get() == "Al principio":
            new_list_process = []
            new_list_process.append(self.new)
            new_list_process = new_list_process + list_process
            return new_list_process
             
    def Open_File(self):
        with open("procesos.txt","r") as file:
            list_process = file.readlines()
        return list_process
    
    def FIFO(self):
        List_Process_FIFO = self.Open_File()
        while len(List_Process_FIFO) != 0:
            if self.band_add:
                List_Process_FIFO = self.current_list(List_Process_FIFO)
                self.band_add = False
            process = List_Process_FIFO[0].split(",")
            load = ""
            lblprocess = Label(self.frame, text=process[0])
            lblprocess.place(x=10, y=3)
            self.update_process_data(process[0],process[1],process[2],True)
            self.window.update()
            for count in range(int(process[2])):
                lblLoad = Label(self.frame, text=load, bg="GREEN",fg="GREEN")
                lblLoad.place(x=200, y=3)
                load = load + " "
                self.window.update()
                time.sleep(1)
                lblLoad.destroy()
            self.update_process_data(process[0], process[1], process[2], False)
            lblprocess.destroy()
            self.window.update()
            List_Process_FIFO.pop(0)
        
    def update_process_data(self,name,priority,time,insert):
        if insert:
            self.lblprocess = Label(self.window, text=name)
            self.lblprocess.place(x=40,y=130)
            self.lblpriority = Label(self.window, text=priority)
            self.lblpriority.place(x=40, y=190)
            self.lbltime = Label(self.window, text=time)
            self.lbltime.place(x=40, y=250)
        else:
            self.lblprocess.destroy()
            self.lblpriority.destroy()
            self.lbltime.destroy()





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