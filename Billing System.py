from tkinter import *
global pq
def genrateBill():                    #second window take user detail
     
    sec= Toplevel(window )
    
    sec.geometry("1536x864")
    
    name=Label(sec,text="Enter Custumer Name")
    name.grid(row="0" ,column="0",padx="20" ,pady="20")
    
    
    nameBox=Entry(sec ,textvariable= Name)
    nameBox.grid(row="0" , column="1")

     
    email=Label(sec,text="Enter Email")
    email.grid(row="1" ,column="0",padx="0")

    emailBox=Entry(sec ,textvariable=EmailId)
    emailBox.grid(row="1" ,column="1")
    
    
    mobile=Label(sec,text="Enter Mobile No")
    mobile.grid(row="0 ",column="2" ,padx="20")
    
    mobileBox=Entry(sec,textvariable=mobno)
    mobileBox.grid(row="0" ,column ="3" )
    

    address=Label(sec, text="Enter Addess")
    address.grid(row="1" ,column="2" ,padx ="20")
    
    addressBox=Entry(sec ,textvariable=Address)
    addressBox.grid(row="1" ,column="3")

    
    items=Label(sec, text="No Of Items")
    items.grid(row =2 ,column =0 ,pady=(15 ,0))
    
    itemBox=Scale(sec ,from_ =1 ,to=100 ,orient =HORIZONTAL ,length =200 )
    itemBox.grid(row =2 ,column= 1)
    #p= itemBox.get()
    
    
    genrate=Button(sec,text="Genrate Bill" ,command=insertData)   #button to insert items 
    genrate.place(x="260" ,y="150")

def insertData():                          #Window that take input of purchased item data
    insertwin =Toplevel() 
    insertwin.geometry('{}x{}'.format(insertwin.winfo_screenwidth(),insertwin.winfo_screenheight()))
    #this section only show the custimer details
    
    n=Label(insertwin,text="Name :",font="22px")
    n.grid(row="0", column ="0",sticky =W , padx=(50 ,0) ,pady =(50,0))

    c=Name.get()
    x=Label(insertwin,text=c,font="22px" )
    x.grid(row="0", column ="1",pady =(50,0) )
    
    y1=Label(insertwin,text="Mobile No :",font="22px")
    y1.grid(row="0", column ="2", padx=(50 ,0) ,pady =(50,0))
    y=mobno.get()
    y2=Label(insertwin,text=y,font="22px" )
    y2.grid(row="0", column ="3",sticky =W,pady =(50,0) )
    
    z=Label(insertwin,text="Address :",font="22px")
    z.grid(row="1", column ="0",sticky =W , padx=(50 ,0) ,pady =(50,0))
    z1=Address.get()
    z2=Label(insertwin,text=z1,font="22px" )
    z2.grid(row="1", column ="1",sticky =W ,pady =(50,0) )
    
    q=Label(insertwin,text="Email Id :",font="22px")
    q.grid(row="1", column ="2",sticky =W , padx=(50 ,0) ,pady =(50,0))
    q1=EmailId.get()
    q2=Label(insertwin,text=q1,font="22px" )
    q2.grid(row="1", column ="3",sticky =W ,pady =(50,0) )
    
    
     #this section only show the custimer details
    
    
window= Tk()                             # Main window of application
Name=StringVar()
mobno=StringVar()
Address=StringVar()
EmailId=StringVar()
p=IntVar()

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