from tkinter import *
from tkinter import ttk
import time 

class Process_Window:
    def __init__(self,window):
        self.window = window
        self.window.title("Algoritmos de planificacion")
        self.window.geometry("600x260")

        self.band_add = False
        self.stop_process = False
        self.list_new_processes = []
        self.process_support = []

        btnStop = Button(self.window, text="Finalizar", command=self.stop)
        btnStop.place(x=500,y=0)

        bar_menu = Menu(self.window)

        menu_process = Menu(bar_menu)
        menu_process.add_command(label="Round Robin",command=self.menu_Round_Robin)
        menu_process.add_command(label="SJF",command=self.menu_SJF)
        menu_process.add_command(label="FIFO",command=self.menu_FIFO)
        menu_process.add_command(label="Prioridad",command=self.menu_priority)
        bar_menu.add_cascade(label="Algoritmos", menu=menu_process)

        menu_Add = Menu(bar_menu)
        menu_Add.add_command(label="Agregar",command=self.window_new_process)
        bar_menu.add_cascade(label="Procesos",menu=menu_Add)
        self.window.config(menu=bar_menu)

        self.frame = LabelFrame(self.window,text="PROCESO EN EJECUCION")
        self.frame.place(x=20, y=20,width=290,height=235)
        
        self.table = ttk.Treeview(self.window, columns=("col1"))
        self.table.column("#0", width=133)
        self.table.column("col1", width=133, anchor=CENTER)

        self.table.heading("#0", text="Proceso", anchor=CENTER)
        self.table.heading("col1", text="Estado", anchor=CENTER)

        self.table.place(x=320, y=28)
    
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
    
    def menu_Round_Robin(self):
        lblProcess = Label(self.frame, text="---> Round_Robin <---",fg="BLUE")
        lblProcess.place(x=20,y=20)
        while not self.stop_process:
            List_Round_Robin = self.Open_File()
            List_Round_Robin = self.current_list(List_Round_Robin)
            self.Round_Robin(List_Round_Robin)
            self.change_list()
        lblProcess.destroy()
        self.stop_process = False
        self.delete_table_date()

    def menu_SJF(self):
        lblProcess = Label(self.frame, text="---> SJF <---", fg="BLUE")
        lblProcess.place(x=20, y=20)
        while not self.stop_process:
            List_SJF = self.Open_File()
            List_SJF = self.current_list(List_SJF)
            self.SJF(List_SJF)
            self.change_list()
        self.stop_process = False
        lblProcess.destroy()
        self.delete_table_date()
    
    def menu_FIFO(self):
        lblProcess = Label(self.frame, text="---> FIFO <---", fg="BLUE")
        lblProcess.place(x=20, y=20)
        while not self.stop_process:
            List_FIFO = self.Open_File()
            List_FIFO = self.current_list(List_FIFO)
            self.FIFO(List_FIFO)
            self.change_list()
        self.stop_process = False
        lblProcess.destroy()
        self.delete_table_date()
    
    def menu_priority(self):
        lblProcess = Label(self.frame, text="---> Prioridad <---", fg="BLUE")
        lblProcess.place(x=20, y=20)
        while not self.stop_process:
            List_priority = self.Open_File()
            List_priority = self.current_list(List_priority)
            self.priority(List_priority)
            self.change_list()
        self.stop_process = False
        lblProcess.destroy()
        self.delete_table_date()

    def stop(self):
        self.stop_process = True

    def new_process(self):
        new = self.txtProcess.get() + "," + self.txtPriority.get() + "," + self.txtTime.get() + "," + self.option.get()
        self.list_new_processes.append(new)

        self.txtProcess.delete(0,END)
        self.txtPriority.delete(0,END)
        self.txtTime.delete(0,END)
        self.band_add = True

    def current_list(self,list_process):
        self.process_support = self.process_support + self.list_new_processes
        while len(self.list_new_processes) != 0:
            new_list_process = []
            new_process = self.list_new_processes[0].split(",")
            new = new_process[0] + "," + new_process[1] + "," + new_process[2]
            new_list_process.append(new)

            if new_process[3] == "Al final":
                list_process = list_process + new_list_process

            elif new_process[3] == "Al principio":
                list_process = new_list_process + list_process

            self.list_new_processes.pop(0)
        return list_process
    
    def change_list(self):
        self.list_new_processes = self.process_support
             
    def Open_File(self):
        with open("procesos.txt","r") as file:
            list_process = file.readlines()
        return list_process
    
    def Round_Robin(self, List_Process_Round_Robin):
        while len(List_Process_Round_Robin) != 0:
            if self.band_add:
                List_Process_Round_Robin = self.current_list(List_Process_Round_Robin)
                self.band_add = False
            process = List_Process_Round_Robin[0].split(",")
            time_process = int(process[2])
            self.destroy_or_insert_label(process[0], process[1], process[2], True)
            self.window.update()

            for count_time in range(3):
                if time_process == 0:
                    break
                else:
                    time_process -= 1
                
                self.process_counting(count_time, True)
                time.sleep(1)

            if time_process > 0:
                List_Process_Round_Robin.append(
                    process[0]+", "+process[1]+", "+str(time_process))
            else:
                self.insert_table(process[0])

            self.destroy_or_insert_label(process[0], process[1], process[2], False)
            self.process_counting(count_time, False)
            List_Process_Round_Robin.pop(0)
            if self.stop_process:
                break

    def SJF(self, List_Process_SJF):
        times = self.sort_process(List_Process_SJF,2)
        number_process = len(List_Process_SJF)
        while len(List_Process_SJF) != 0:
            if self.band_add:
                List_Process_SJF = self.current_list(List_Process_SJF)
                times = self.sort_process(List_Process_SJF,2)
                self.band_add = False

            for count_process in range(number_process+1):
                process = List_Process_SJF[count_process].split(",")

                if times[0] == int(process[2]):
                    self.destroy_or_insert_label(process[0], process[1], process[2], True)
                    self.window.update()

                    for count in range(times[0]):
                        self.process_counting(count, True)
                        time.sleep(1)
                    self.insert_table(process[0])
                    break       
            self.destroy_or_insert_label(process[0], process[1], process[2], False)
            self.process_counting(count, False)
            List_Process_SJF.pop(count_process)
            number_process = len(List_Process_SJF)
            times.pop(0)
            if self.stop_process:
                break
    
    def FIFO(self, List_Process_FIFO):
        
        while len(List_Process_FIFO) != 0:
            if self.band_add:
                List_Process_FIFO = self.current_list(List_Process_FIFO)
                self.band_add = False

            process = List_Process_FIFO[0].split(",")
            self.destroy_or_insert_label(process[0], process[1], process[2], True)
            self.window.update()
            for count in range(int(process[2])):

                self.process_counting(count, True)
                time.sleep(1)
            
            self.insert_table(process[0])
            self.destroy_or_insert_label(process[0], process[1], process[2], False)
            self.process_counting(count, False)
            List_Process_FIFO.pop(0)
            if self.stop_process:
                break

    def priority(self, List_Process_priority):
        
        list_priority = self.sort_process(List_Process_priority, 1)
        number_process = len(List_Process_priority)

        while len(List_Process_priority) != 0:
            if self.band_add:
                List_Process_priority = self.current_list(List_Process_priority)
                self.band_add = False

            for count_process in range(number_process+1):
                process = List_Process_priority[count_process].split(",")

                if list_priority[0] == int(process[1]):
                    self.destroy_or_insert_label(process[0], process[1], process[2], True)

                    for count in range(int(process[2])):
                        self.process_counting(count,True)
                        time.sleep(1)
                    self.insert_table(process[0])
                    break
            
            self.destroy_or_insert_label(process[0], process[1], process[2], False)
            self.process_counting(count, False)
            List_Process_priority.pop(count_process)
            number_process = len(List_Process_priority)
            list_priority.pop(0)
            if self.stop_process:
                break
    
    def sort_process(self, list_SJF, time_or_priority):
        sort_process = []
        for count_time in range(len(list_SJF)):
            process = list_SJF[count_time].split(",")
            sort_process.append(int(process[time_or_priority]))
        sort_process.sort()
        return sort_process
        
    def destroy_or_insert_label(self,name,priority,time,insert):
        if insert:
            self.lblprocess = Label(self.frame, text=f"Proceso: {name}")
            self.lblprocess.place(x=20, y=50)

            self.lblpriority = Label(self.frame, text=f"Prioridad : {priority}")
            self.lblpriority.place(x=20, y=80)

            self.lbltime = Label(self.frame, text=f"Tiempo: {time}")
            self.lbltime.place(x=20, y=110)
            
        else:
            self.lblprocess.destroy()
            self.lblpriority.destroy()
            self.lbltime.destroy()
        self.window.update()
    
    def process_counting(self,count_time,insert):
        if insert:
            self.lblcount_time = Label(self.frame, text=f"Tiempo de ejecucion: {count_time + 1}")
            self.lblcount_time.place(x=20,y=140)
        else:
            self.lblcount_time.destroy()
        self.window.update()
    
    def insert_table(self, process):
        self.table.insert("",END,text=process,values="Finalizado")
    
    def delete_table_date(self):
        registry = self.table.get_children()
        for count_registry in registry:
            self.table.delete(count_registry)
        
if __name__ == "__main__":
    ventana = Tk()
    apliaction = Process_Window(ventana)
    ventana.mainloop()