from tkinter import *
import random
import time


w=Tk()

w.title("Restaurent Managemet System")
w.configure(bg="powder blue")

###################### Frames ####################################################################


TopFrame=Frame(w,width=1700,height=100,bg='powder blue')
TopFrame.pack(side=TOP)


LeftFrame=Frame(w,width=800,height=600,bg='powder blue')
LeftFrame.pack(side=LEFT,pady=(50,10))

RightFrame=Frame(w,width=300,height=900,bg='powder blue')
RightFrame.pack(side=RIGHT,pady=(10,50))


##Database



import mysql.connector as m

con=m.connect(host="127.0.0.1",user="root",password="H@rd2Cr@ck",database="rms")
c=con.cursor()
c.execute("create table if not exists selling_data(ref_no int,Large_fries int,Burger_Meal int,F_O_Meal int,Chicken_meal int,Cheese_meal int,Drinks int,Cost_of_Meal int,Service_charge float,State_tax float,Sub_total float,Total float)")


def resett():
    
    v1.set('')
    v2.set('')
    v3.set('')
    v4.set('')
    v5.set('')
    v6.set('')
    v7.set('')
    v8.set('')
    v9.set('')
    v10.set('')
    v11.set('')
    v12 .set('')

def Submit():
    global v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12

    x1=int(v1.get())
    x2=int(v2.get())
    x3=int(v3.get())
    x4=int(v4.get())
    x5=int(v5.get())
    x6=int(v6.get())
    x7=int(v7.get())
    x8=int(v8.get())
    x9=float(v9.get())
    x10=float(v10.get())
    x11=float(v11.get())
    x12=float(v12.get())
    
    c.execute("insert into selling_data values(%d,%d,%d,%d,%d,%d,%d,%d,%f,%f,%f,%f)"%(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12))
    con.commit()
    resett()

###############################  Top Part  ###################################################################

name=Label(TopFrame,text='Restaurent Management System',font=('arial',30,'bold'),fg='Steel Blue',bg='powder blue',bd=10,anchor='w')
name.grid(row=0,column=0)

LocalTime=time.asctime(time.localtime(time.time()))

time=Label(TopFrame,text=LocalTime,font=('arial',20,'bold'),fg='steel blue',bg='powder blue',bd=10,anchor='w')
time.grid(row=1,column=0)

####################################  Left Part: order details ######################################################


##### Methods #####
'''
f=open('ref_number.txt','r+')
    ref=f.read()
    ref_number =int(ref,10)
    f.truncate(0)
    f.seek(0)
    f.write(ref_number)'''
    
   
ref_number=1001

def genref():
    global ref_number
    
    
    v1.set(ref_number)
    
    ref_number +=1
    
    




def  total():

    genref()
    #default values    
    n2= 60  * int(v2.get())
    n3= 50  * int(v3.get())
    n4= 90  * int(v4.get())
    n5= 100 * int(v5.get())
    n6= 80  * int(v6.get())
    n7= 30  * int(v7.get())
    
    ttl=n2+n3+n4+n5+n6+n7
    v8.set(ttl)
    
    sc=ttl*0.001
    a=round(sc,2)
    v9.set(a)

    st=ttl*0.05
    v10.set(st)

    subtotal=ttl+sc+st
    v11.set(subtotal)

    totalcost=round(subtotal,0)
    v12.set(totalcost)

    


    

def quitt():
    import sys as s
    s.exit()



###################################

L1=Label(LeftFrame,text="Refrence No",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')
L2=Label(LeftFrame,text="Large Fries ",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')
L3=Label(LeftFrame,text="Burger Meal",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')
L4=Label(LeftFrame,text="Filet-o-Meal",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')
L5=Label(LeftFrame,text="Chicken Meal",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')
L6=Label(LeftFrame,text="Cheese Meal",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')
L7=Label(LeftFrame,text="Drinks",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')
L8=Label(LeftFrame,text="Cost of Meal",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')
L9=Label(LeftFrame,text="Service Charge",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')
L10=Label(LeftFrame,text="State Tax",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')
L11=Label(LeftFrame,text="Sub Total",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')
L12=Label(LeftFrame,text="Total",font=('arial',20,'bold'),fg='steel blue',bg='powder blue')

#v6=StringVar(w, value='0')

v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()
v7=StringVar()
v8=DoubleVar()
v9=DoubleVar()
v10=DoubleVar()
v11=DoubleVar()
v12=DoubleVar()


E1=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v1)
E2=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v2)
E3=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v3)
E4=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v4)
E5=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v5)
E6=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v6)
E7=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v7)
E8=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v8)
E9=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v9)
E0=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v10)
E11=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v11)
E12=Entry(LeftFrame,font=("arial",15,"bold"),bg='powder blue',fg='black',justify="right",bd=8,textvariable=v12)


B1=Button(LeftFrame,text='Total',font=("arial",15,"bold"),bg='powder blue',fg='black',width=7,bd=7,command=total)
B2=Button(LeftFrame,text='Reset',font=("arial",15,"bold"),bg='powder blue',fg='black',width=7,bd=7,command=resett)
B3=Button(LeftFrame,text='Quit',font=("arial",15,"bold"),bg='powder blue',fg='black',width=7,bd=7,command=quitt)
B4=Button(LeftFrame,text='Submit',font=("arial",15,"bold"),bg='powder blue',fg='black',width=7,bd=7,command=Submit)



L1.grid(row=1,column=1,padx=(10,10),pady=(10,10))
L2.grid(row=2,column=1,padx=(10,10),pady=(10,10))
L3.grid(row=3,column=1,padx=(10,10),pady=(10,10))
L4.grid(row=4,column=1,padx=(10,10),pady=(10,10))
L5.grid(row=5,column=1,padx=(10,10),pady=(10,10))
L6.grid(row=6,column=1,padx=(10,10),pady=(10,10))


E1.grid(row=1,column=2,padx=(10,10),pady=(10,10))
E2.grid(row=2,column=2,padx=(10,10),pady=(10,10))
E3.grid(row=3,column=2,padx=(10,10),pady=(10,10))
E4.grid(row=4,column=2,padx=(10,10),pady=(10,10))
E5.grid(row=5,column=2,padx=(10,10),pady=(10,10))
E6.grid(row=6,column=2,padx=(10,10),pady=(10,10))


L7.grid(row=1,column=3,padx=(10,10),pady=(10,10))
L8.grid(row=2,column=3,padx=(10,10),pady=(10,10))
L9.grid(row=3,column=3,padx=(10,10),pady=(10,10))
L10.grid(row=4,column=3,padx=(10,10),pady=(10,10))
L11.grid(row=5,column=3,padx=(10,10),pady=(10,10))
L12.grid(row=6,column=3,padx=(10,10),pady=(10,10))

E7.grid(row=1,column=4,padx=(10,10),pady=(10,10))
E8.grid(row=2,column=4,padx=(10,10),pady=(10,10))
E9.grid(row=3,column=4,padx=(10,10),pady=(10,10))
E0.grid(row=4,column=4,padx=(10,10),pady=(10,10))
E11.grid(row=5,column=4,padx=(10,10),pady=(10,10))
E12.grid(row=6,column=4,padx=(10,10),pady=(10,10))

B1.grid(row=7,column=3,padx=(20,20),pady=(20,20))
B2.grid(row=7,column=4,padx=(20,20),pady=(20,20))
B3.grid(row=7,column=1,padx=(20,20),pady=(20,20))
B4.grid(row=7,column=2,padx=(20,20),pady=(20,20))



#################################### Right part: Calculator ########################################################

####  Methods  #####

expression=""

def btnclk(n):
    global expression
    expression=expression+str(n)
    v.set(expression)

    
def calculate():
    global expression
    result=eval(expression)
    v.set(result)
    
def clear():
    global expression
    expression=""
    v.set(expression)

#############################################

v=StringVar()

E=Entry(RightFrame,font=("arial",20,"bold"),bg='powder blue',fg='black',justify="right",textvariable=v,bd=20)
B1=Button(RightFrame,text="1",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk(1))
B2=Button(RightFrame,text="2",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk(2))
B3=Button(RightFrame,text="3",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk(3))
B4=Button(RightFrame,text="4",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk(4))
B5=Button(RightFrame,text="5",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk(5))
B6=Button(RightFrame,text="6",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk(6))
B7=Button(RightFrame,text="7",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk(7))
B8=Button(RightFrame,text="8",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk(8))
B9=Button(RightFrame,text="9",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk(9))
B0=Button(RightFrame,text="0",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk(0))
B_Plus=Button(RightFrame,text="+",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk('+'))
B_Minus=Button(RightFrame,text="-",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk("-"))
B_Mul=Button(RightFrame,text="x",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk("*"))
B_Div=Button(RightFrame,text="/",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=lambda:btnclk("/"))
B_Clear=Button(RightFrame,text="C",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=clear)
B_Equal=Button(RightFrame,text="=",bg='powder blue',fg='black',font=("arial",15,"bold"),width=3,bd=10,command=calculate)

# positions

E.grid(row=1,column=1,columnspan=4,padx=(10,10),pady=(10,10))
B1.grid(row=2,column=1,padx=(10,10),pady=(10,10))
B2.grid(row=2,column=2,padx=(10,10),pady=(10,10))
B3.grid(row=2,column=3,padx=(10,10),pady=(10,10))
B4.grid(row=3,column=1,padx=(10,10),pady=(10,10))
B5.grid(row=3,column=2,padx=(10,10),pady=(10,10))
B6.grid(row=3,column=3,padx=(10,10),pady=(10,10))
B7.grid(row=4,column=1,padx=(10,10),pady=(10,10))
B8.grid(row=4,column=2,padx=(10,10),pady=(10,10))
B9.grid(row=4,column=3,padx=(10,10),pady=(10,10))
B0.grid(row=5,column=2,padx=(10,10),pady=(10,10))
B_Equal.grid(row=5,column=3,padx=(10,10),pady=(10,10))
B_Clear.grid(row=5,column=1,padx=(10,10),pady=(10,10))

B_Plus.grid(row=2,column=4,padx=(10,10),pady=(10,10))
B_Minus.grid(row=3,column=4,padx=(10,10),pady=(10,10))
B_Mul.grid(row=4,column=4,padx=(10,10),pady=(10,10))
B_Div.grid(row=5,column=4,padx=(10,10),pady=(10,10))


w.mainloop()




###############################################################  End  ##################################################################






