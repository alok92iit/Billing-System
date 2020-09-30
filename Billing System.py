from tkinter import *
def genrateBill():                    #second window take user detail
    global sec 
    sec= Toplevel(window )
    
    sec.geometry("800x250")
    frame1=LabelFrame(sec  ,text="Customer  Details.. " , padx=10 ,pady=10  )
    frame1.pack(padx=10 ,pady= 10 ,fill=BOTH )
    
    name=Label(frame1,text="Enter Custumer Name")
    name.grid(row="0" ,column="0",padx="20" ,pady="20")
    
    
    nameBox=Entry(frame1,textvariable= Name)
    nameBox.grid(row="0" , column="1")

     
    email=Label(frame1,text="Enter Email")
    email.grid(row="1" ,column="0",padx="0")

    emailBox=Entry(frame1 ,textvariable=EmailId)
    emailBox.grid(row="1" ,column="1")
    
    
    mobile=Label(frame1,text="Enter Mobile No")
    mobile.grid(row="0 ",column="2" ,padx="20")
    
    mobileBox=Entry(frame1,textvariable=mobno)
    mobileBox.grid(row="0" ,column ="3" )
    

    address=Label(frame1, text="Enter Addess")
    address.grid(row="1" ,column="2" ,padx ="20")
    
    addressBox=Entry(frame1 ,textvariable=Address)
    addressBox.grid(row="1" ,column="3")

    
    items=Label(frame1, text="No Of Items")
    items.grid(row =2 ,column =0 ,pady=(15 ,0))
    
    #slider which will take number of products as a input
    
    global itemBox
 
    itemBox=Scale(frame1 ,from_ =1 ,to=100 ,orient =HORIZONTAL ,length =200 )
    itemBox.grid(row =2 ,column= 1)
    #p= itemBox.get()
    
    global ok
    ok=Button(frame1,text="Ok" ,command=insertData ,padx=25 ,width =20)   #button to insert items 
    ok.grid(row=2,column=2 , pady=(15,0),padx=(35,0) )


def insertData():
    ok.config(state=DISABLED)  #confif() to change coniguration of ok button to Disable ok button of frame1
    sec.geometry('{}x{}'.format(sec.winfo_screenwidth(),sec.winfo_screenheight())) #create window of monitor size
    c=itemBox.get()
    
    frame=LabelFrame(sec  ,text="products Details.. " ) #Box inner padding
    frame.pack(padx=10 ,pady= 10 ,fill=BOTH ,expand=1)
    
    #for adding scroll bar in frame wedget
    
    my_canvas=Canvas(frame)
    my_canvas.pack(side=LEFT,fill=BOTH ,expand =1)

    scroll=Scrollbar(frame ,orient =VERTICAL ,command =my_canvas.yview)
    scroll.pack(fill=Y ,side=RIGHT)

    my_canvas.configure(yscrollcommand=scroll.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)

    my_canvas.create_window((0,0) ,window= second_frame )
    
    # Heading of the table field 
    
    sn0=Label(second_frame ,text ="S.No",font='Times 12 bold').grid(row =0 ,column= 0)
    product=Label(second_frame  ,text="Product Name",font='Times 12 bold').grid(row=0 ,column=1)
    quantity=Label(second_frame , text="Quantity \n (eg:1gm,1kg,1ps)",font='Times 12 bold').grid(row=0,column=2)
    price =Label(second_frame , text="Price" ,font='Times 12 bold').grid(row =0 ,column=3)
    discount =Label(second_frame , text="Discount",font='Times 12 bold').grid(row=0 ,column=4)
    tax =Label(second_frame , text="Tax( in %)" ,font='Times 12 bold').grid(row=0 ,column=5)
    
   
    l=[]
    
    # Align Entry wedget in grid fashion
    
    for i in range(c):
        l.append([])
        
        for j in range(5):
            
            #This x label object will print serial no before each row . 
            
            x=Label(second_frame ,text=i+1,font='Times 12 bold',padx="5").grid(row=i+1 ,column=0 )  
            
            emailBox=Entry(second_frame ,width=30 )
            emailBox.grid(row=i+1 ,column=j+1 , pady=5,padx=5   )
            l[i].append(emailBox)  
    genrate=Button(second_frame,text="Genrate Bill"  ,padx=5 ,width =20)   #button to show final detail to user for further modification
    genrate.grid(row=c+1,column= 3, pady=15,padx=15 )

    
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