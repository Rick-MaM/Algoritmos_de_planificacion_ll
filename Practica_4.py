from tkinter import *
from tkinter import ttk
import time 

class Window:
    def __init__(self,window):
        self.window = window
        self.window.title("Algoritmos de planificacion")
        self.window.geometry("450x350")

        self.band_add = False
        self.list_new_processes = []

        bar_menu = Menu(self.window)

        menu_process = Menu(bar_menu)
        menu_process.add_command(label="Round Robin",command=self.Round_Robin)
        menu_process.add_command(label="SJF",command=self.SJF)
        menu_process.add_command(label="FIFO",command=self.FIFO)
        menu_process.add_command(label="Prioridad",command=self.priority)
        bar_menu.add_cascade(label="Algoritmos", menu=menu_process)

        menu_Add = Menu(bar_menu)
        menu_Add.add_command(label="Agregar",command=self.window_new_process)
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

        Label(self.window, text=">Tiempo de ejecucion<",fg="BLUE").place(x=20, y=280)
    
    def window_new_process(self):
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
        new = self.txtProcess.get() + "," + self.txtPriority.get() + "," + self.txtTime.get()
        self.list_new_processes.append(new)
        self.band_add = True

    def current_list(self,list_process):
        if self.option.get() == "Al final":
            list_process = list_process + self.list_new_processes
            return list_process
        elif self.option.get() == "Al principio":
            new_list_process = []
            new_list_process = self.list_new_processes + list_process
            return new_list_process
             
    def Open_File(self):
        with open("procesos.txt","r") as file:
            list_process = file.readlines()
        return list_process
    
    def Round_Robin(self):
        List_Process_Round_Robin = self.Open_File()
        quantum = 3
        while len(List_Process_Round_Robin) != 0:

            process = List_Process_Round_Robin[0].split(",")
            time_process = int(process[2])
            self.update_process_data(process[0], process[1], process[2], True)
            self.window.update()

            for count_time in range(quantum):
                if time_process == 0:
                    break
                else:
                    time_process -= 1
                
                lblTime = Label(self.window, text=count_time + 1)
                lblTime.place(x=40, y=310)
                self.window.update()
                time.sleep(1)

            if time_process > 0:
                List_Process_Round_Robin.append(
                    process[0]+", "+process[1]+", "+str(time_process))
            else:
                pass

            self.update_process_data(process[0], process[1], process[2], False)
            lblTime.destroy()
            self.window.update()
            List_Process_Round_Robin.pop(0)

    def SJF(self):
        List_Process_SJF = self.Open_File()
        times = self.sort_process(List_Process_SJF,2)
        number_process = len(List_Process_SJF)
        while len(List_Process_SJF) != 0:
            if self.band_add:
                List_Process_SJF = self.current_list(List_Process_SJF)
                times = self.sort_process(List_Process_SJF,2)
                self.band_add = False
                self.list_new_processes = []

            for count_process in range(number_process+1):
                process = List_Process_SJF[count_process].split(",")

                if times[0] == int(process[2]):
                    self.update_process_data(process[0], process[1], process[2], True)
                    self.window.update()

                    for count in range(times[0]):
                        lblTime = Label(self.window, text=count + 1)
                        lblTime.place(x=40, y=310)
                        self.window.update()
                        time.sleep(1)
                    break
            self.update_process_data(process[0], process[1], process[2], False)
            lblTime.destroy()
            self.window.update()
            List_Process_SJF.pop(count_process)
            number_process = len(List_Process_SJF)
            times.pop(0)
    
    def FIFO(self):
        List_Process_FIFO = self.Open_File()
        while len(List_Process_FIFO) != 0:
            if self.band_add:
                List_Process_FIFO = self.current_list(List_Process_FIFO)
                self.band_add = False
                self.list_new_processes = []

            process = List_Process_FIFO[0].split(",")
            self.update_process_data(process[0],process[1],process[2],True)
            self.window.update()
            for count in range(int(process[2])):

                lblTime = Label(self.window, text=count + 1)
                lblTime.place(x=40,y=310)
                self.window.update()
                time.sleep(1)

            self.update_process_data(process[0], process[1], process[2], False)
            lblTime.destroy()
            self.window.update()
            List_Process_FIFO.pop(0)

    def priority(self):
        List_Process_priority = self.Open_File()
        list_priority = self.sort_process(List_Process_priority, 1)
        number_process = len(List_Process_priority)

        while len(List_Process_priority) != 0:
            if self.band_add:
                List_Process_priority = self.current_list(List_Process_priority)
                self.band_add = False
                self.list_new_processes = []

            for count_process in range(number_process+1):
                process = List_Process_priority[count_process].split(",")

                if list_priority[0] == int(process[1]):
                    self.update_process_data(process[0], process[1], process[2], True)
                    self.window.update()

                    for count in range(int(process[2])):

                        lblTime = Label(self.window, text=count + 1)
                        lblTime.place(x=40, y=310)
                        self.window.update()
                        time.sleep(1)
                    break
            
            self.update_process_data(process[0], process[1], process[2], False)
            lblTime.destroy()
            
            self.window.update()
            List_Process_priority.pop(count_process)
            number_process = len(List_Process_priority)
            list_priority.pop(0)
    
    def sort_process(self, list_SJF, time_or_priority):
        sort_process = []
        for count_time in range(len(list_SJF)):
            process = list_SJF[count_time].split(",")
            sort_process.append(int(process[time_or_priority]))
        sort_process.sort()
        return sort_process
        
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

if __name__ == "__main__":
    ventana = Tk()
    apliaction = Window(ventana)
    ventana.mainloop()