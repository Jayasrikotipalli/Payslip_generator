from tkinter import *
from tkinter import messagebox
import tempfile
import os

root=Tk()
root.title('PAYSLIP GENERATOR')
root.geometry('1280x1280')
bg_color='#2D9290'

# Variables

hours_worked =StringVar()
cost_per_hour = StringVar()
tax = StringVar()
netpay =StringVar()
over_time = StringVar()
gross_pay =StringVar()
Name = StringVar()
Adress = StringVar()
DOB = StringVar()
ID = StringVar()


#

def payslip():
    textarea.delete(1.0,END)
    textarea.insert(END,f'\nName : {Name.get()}\t')
    textarea.insert(END,f'\n\nID : {ID.get()}')
    textarea.insert(END,f'\n\nAdress : {Adress.get()}')
    textarea.insert(END,f'\n\nDOB : {DOB.get()}')
    textarea.insert(END,f'\n\nHours worked : {hours_worked.get()}')
    textarea.insert(END,f'\n\ncost per hour : {cost_per_hour.get()}')
    textarea.insert(END,f'\n\nover time : {over_time.get()}')
    textarea.insert(END,f'\n\nTax : {tax.get()}')
    textarea.insert(END,f'\n\nNet pay : {netpay.get()}')
    textarea.insert(END,f'\n\nGross pay : {gross_pay.get()}')
    

def reset():
    textarea.delete(1.0,END)
    hours_worked.set('') 
    cost_per_hour.set('')
    tax.set('')
    netpay.set('')
    over_time.set("")
    gross_pay.set("")
    Name.set("")
    Adress.set("")
    DOB("")
    ID("")

def print():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open(filename,'w').write(q)
    os.startfile(filename,'Print')


def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()

F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=920,y=90,width=430,height=800)
bill_title=Label(F2,text='payslip',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F2,orient=VERTICAL)
scrol_y.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol_y.set)
textarea.pack(fill=BOTH)
scrol_y.config(command=textarea.yview)



title=Label(root,pady=5,text="Payroll Manangement System",bd=12,bg=bg_color,fg='white',font=('times new roman', 35 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

F1 = LabelFrame(root, text='Employee Details', font=('times new romon', 18, 'bold'), fg='gold',bg=bg_color,bd=15,relief=RIDGE)
F1.place(x=5, y=90,width=900,height=2000)

# Labels

name =Label(F1, text='Name', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
name.grid(row=0,column=0,padx=20,pady=10)
n_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Name,justify=CENTER)
n_txt.grid(row=0,column=1,padx=20,pady=10)

id =Label(F1, text='ID', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
id.grid(row=0,column=2,padx=20,pady=10)
id_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=ID,justify=CENTER)
id_txt.grid(row=0,column=3,padx=20,pady=10)

adress =Label(F1, text='Adress', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
adress.grid(row=1,column=0,padx=20,pady=15)
a_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Adress,justify=CENTER)
a_txt.grid(row=1,column=1,padx=20,pady=15)

dob =Label(F1, text='DOB', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
dob.grid(row=1,column=2,padx=20,pady=15)
d_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=DOB,justify=CENTER)
d_txt.grid(row=1,column=3,padx=20,pady=15)

hours = Label(F1,text='hours_worked',font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
hours.grid(row=2,column=0,padx=20,pady=15)
h_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=hours_worked,justify=CENTER)
h_txt.grid(row=2,column=1,padx=20,pady=15)

cph = Label(F1,text='cost_per_hour',font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
cph.grid(row=5,column=0,padx=20,pady=15)
cp_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cost_per_hour,justify=CENTER)
cp_txt.grid(row=5,column=1,padx=20,pady=15)

t = Label(F1,text='tax',font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
t.grid(row=3,column=2,padx=20,pady=15)
ta_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=tax,justify=CENTER)
ta_txt.grid(row=3,column=3,padx=20,pady=15)

np = Label(F1,text='netpay',font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
np.grid(row=3,column=0,padx=20,pady=15)
np_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=netpay,justify=CENTER)
np_txt.grid(row=3,column=1,padx=20,pady=15)

ot = Label(F1,text='over time',font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
ot.grid(row=4,column=0,padx=20,pady=15)
ot_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=over_time,justify=CENTER)
ot_txt.grid(row=4,column=1,padx=20,pady=15)


gp = Label(F1,text='Gross pay',font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
gp .grid(row=2,column=2,padx=20,pady=15)
gp_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=gross_pay,justify=CENTER)
gp_txt.grid(row=2,column=3,padx=20,pady=15)


# Buttons

F3 =Frame(root,bg=bg_color,bd=15,relief=RIDGE)
F3.place(x=5, y=690,width=1270,height=150)

btn1 = Button(F3, text='Reset', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=reset)
btn1.grid(row=0,column=0,padx=20,pady=10)

btn2 = Button(F3, text='View payslip', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=payslip)
btn2.grid(row=0,column=1,padx=10,pady=10)


btn3 = Button(F3, text='Print', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=print)
btn3.grid(row=0,column=2,padx=10,pady=10)

btn4 = Button(F3, text='exit', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=exit)
btn4.grid(row=0,column=3,padx=10,pady=10)



root.mainloop()