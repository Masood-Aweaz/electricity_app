import tkinter
m=Tk()


def display():
    global m
    global mn
    global l
    global dic

    if int(mn.get()) in l:
        Label(m,text="Meter Number:"+str(mn.get())).pack()
        Label(m,text="Name:"+str(dic[int(mn.get())][0])).pack()
        Label(m,text="Comsumed Units:"+str(dic[int(mn.get())][1])).pack()
        Label(m,text="Electricity Charge:"+str(dic[int(mn.get())][2])).pack()
        Label(m,text="Total Amount(including tax):"+str(dic[int(mn.get())][3])).pack()




def gr():
    global m
    global mn
    global l
    Label(m,text="Meter Number ").pack()
    mn=StringVar()
    e1=Entry(m,textvariable=mn).pack()
    Button(m,text="GO",width=10,bg="green",command=display).pack()
    
        




m.title("Electricity Bill" )
m.geometry("400x400")
Button(m,text="BILL",width=25,height=1,bg="blue",command=gr).pack()

m.mainloop()
