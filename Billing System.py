 
from tkinter import *

def genrateBill():                    #second window take user detail
     
    sec= Toplevel(window )
    
    sec.geometry("600x200")
    
    name=Label(sec,text="Enter Custumer Name")
    name.grid(row="0" ,column="0",padx="20" ,pady="20")
    
    
    nameBox=Entry(sec ,textvariable= pin)
    nameBox.grid(row="0" , column="1")

     
    email=Label(sec,text="Enter Email")
    email.grid(row="1" ,column="0",padx="0")

    emailBox=Entry(sec)
    emailBox.grid(row="1" ,column="1")
    Emailadd=emailBox.get()
    
    mobile=Label(sec,text="Enter Mobile No")
    mobile.grid(row="0 ",column="2" ,padx="20")
    
    mobileBox=Entry(sec)
    mobileBox.grid(row="0" ,column ="3" )
    Mobile=mobileBox.get()

    address=Label(sec, text="Enter Addess")
    address.grid(row="1" ,column="2" ,padx ="20")
    
    addressBox=Entry(sec)
    addressBox.grid(row="1" ,column="3")
    Address=addressBox.get()
    
    items=Label(sec, text="Enter No Of Items")
    items.place(x="180" ,y="100")
    
    itemBox=Entry(sec)
    itemBox.place(x="325" ,y="100")
    
    
    genrate=Button(sec,text="Genrate Bill" ,command=insertData)   #button to insert items 
    genrate.place(x="260" ,y="150")

def insertData():
    thirdwin =Toplevel()
    
    thirdwin.geometry("600x250")
    c=pin.get()
    x=Label(thirdwin,text=c)
    x.pack()

    
window= Tk()                             # Main window of application
pin=StringVar()                        

window.geometry("400x200")
window.title("Billing System")
hading =Label(window,
              text="Billing System",
              pady="20",
              font="24")
button =Button(window,text ="Genrate Bill" ,width ='30' ,padx ="20",command=genrateBill)   #button for going to second window
sale   =Button(window,
               text ="Show sales" ,
               width="30",
               padx="20")
hading.pack()
button.pack()
sale.pack(pady="20")
window.mainloop()