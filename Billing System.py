from tkinter import *
from tkinter import messagebox
from tkinter import ttk

fontL ='Times 18'        #font style for labels
fontE ='Times 16'        #font style for entry wedget

#Contains all form labels   

def labels(frameobject):
     
    frame=frameobject
    
    n=Label(frame,text="Name :",font= fontL)
    n.grid(row="0", column ="0",sticky =W , padx=25 ,pady =10)
    
    y1=Label(frame,text="Mobile No :",font= fontL)
    y1.grid(row="1", column ="0", padx=25 ,pady =(0,10))

    z=Label(frame,text="Address :",font= fontL)
    z.grid(row="1", column ="2",sticky =W , padx=25 ,pady =(0,10))
    
    q=Label(frame,text="Email Id :",font= fontL)
    q.grid(row="0", column ="2",sticky =W , padx=25, pady =10)

def labelUserData(frameName):
    frame =frameName
    
    c=Name.get().strip()
    x=Label(buyerData,text=c.title() ,font= fontL )
    x.grid(row="0", column ="1", pady =10)
    

    y=mobno.get()
    y2=Label(buyerData,text=y,font= fontL)
    y2.grid(row="1", column ="1",sticky =W ,pady =(0,10) )
    
    z1=Address.get()
    z2=Label(buyerData,text=z1.upper(),font= fontL)
    z2.grid(row="1", column ="3",sticky =W ,pady =(0,10) )
    

    q1=EmailId.get()
    q2=Label(buyerData,text=q1,font= fontL)
    q2.grid(row="0", column ="3",sticky =W ,pady =10 )

    
def show(): #third window
    #Window that will show the data
    temp=0
    global itemsno
    itemsno=itemBox.get()
    l= [[grid[i][j].get() for j in range(5)] for i in range(itemsno)]
    for i in range(itemsno):
        if l[i][0]=='' or l[i][1]=='' or l[i][2]=='' or l[i][0].isnumeric():
                messagebox.showinfo('Alert','You miss somthing in row number {} .\n\t\tOr\n Make some mistake product name'.format(i+1) )
        elif l[i][2].isnumeric()==False:
            messagebox.showinfo('Alert','Please enter correct price of product in row {}'.format(i+1))
        else:
            temp+=1
    if temp==itemsno:        
            showWin =Toplevel() 
            showWin.geometry('{}x{}'.format(showWin.winfo_screenwidth(),showWin.winfo_screenheight()))
            #this section only show the customer details
            global buyerData
            buyerData =LabelFrame(showWin, text="Consumer Details..")
            buyerData.pack(fill= BOTH ,pady =10 ,padx=10 )
        
            labels(buyerData)          #Call fuction that display label(eg Name Mobile no ..)
            labelUserData(buyerData)   #Call fuction that display user data enter in entry wedget

            productData=LabelFrame(showWin ,text="Product Details..")
            productData.pack(fill=BOTH ,pady=10 ,padx=10)

            my_treeview =ttk.Treeview(productData )
            #define columns 
            my_treeview['columns'] =('Product Name','Quantity','Price', 'Discount','Tax','Total')
            #formatting the tree

            my_treeview.column('#0',width=50,anchor=W)     #Phantom column(extra column)
            my_treeview.column('Product Name' ,width=120 ,anchor=W)  
            my_treeview.column('Quantity', width=120 ,anchor=W)
            my_treeview.column('Price' ,width=120 ,anchor=CENTER)
            my_treeview.column('Discount' ,width=120 ,anchor=W)
            my_treeview.column('Tax' ,width=120 , anchor=W)
            my_treeview.column('Total' ,width=120 ,anchor=W)

            my_treeview.heading('#0',text='S.No',anchor=W)
            my_treeview.heading('Product Name',text='Product Name' ,anchor=W)
            my_treeview.heading('Quantity',text='Quantity',anchor=W)
            my_treeview.heading('Price' ,text='Price',anchor=CENTER)
            my_treeview.heading('Discount' ,text='Discount' ,anchor=W)
            my_treeview.heading('Tax' ,text='Tax' ,anchor=W)
            my_treeview.heading('Total',text='Total' ,anchor=W)


            sno=1
            for row  in l:

                my_treeview.insert(parent='' ,index='end',iid = row, text=sno ,
                                   values=(row[0], row[1], row[2] ,row[3],row[4]))
                sno +=1
            my_treeview.pack(fill=BOTH ) 
    #this section only show the custimer details

def genrateBill():   #second window take user detail
    global sec 
    sec= Toplevel(window )
    
    sec.geometry("850x225")
    global frame1
    frame1=LabelFrame(sec  ,text="Customer  Details.. " , padx=10   )
    frame1.pack(fill=BOTH , padx=10,pady =10)
    
    labels(frame1)
    
    nameBox=Entry(frame1,textvariable= Name ,font= fontE)
    nameBox.grid(row="0" , column="1")
    

    emailBox=Entry(frame1 ,textvariable=EmailId ,font= fontE)
    emailBox.grid(row="1" ,column="1")
       
    mobileBox=Entry(frame1,textvariable=mobno ,font= fontE)
    mobileBox.grid(row="0" ,column ="3" )
        
    addressBox=Entry(frame1 ,textvariable=Address ,font= fontE)
    addressBox.grid(row="1" ,column="3")

    
    items=Label(frame1, text="No Of Items" ,font= fontL)
    items.grid(row =2 ,column =0 , padx=25 ,pady =(0,10))
    
    #slider which will take number of products as a input
    
    global itemBox
 
    itemBox=Scale(frame1 ,from_ =1 ,to=100 ,orient =HORIZONTAL ,length =200 ,font= fontE)
    itemBox.grid(row =2 ,column= 1 ,pady=(0,10))
    
    global ok
    ok=Button(frame1,text="Ok" ,command=insertData ,padx=25 ,width =10, font= 'Times 12')   #button to insert items 
    ok.grid(row=2,column=2 , pady=10,padx=(35,0) )
    
def insertData():
    name=Name.get().strip()
    mobileno =mobno.get()
    if(len(name) <= 2):
        messagebox.showwarning("Alert" ,"Please Enter Valid Name")
    
    elif(len(mobileno) == 0 or len(mobileno)==10):
    
            ok.config(state=DISABLED)  #config() to change coniguration of ok button to Disable ok button of frame1
            sec.geometry('{}x{}'.format(sec.winfo_screenwidth(),sec.winfo_screenheight())) #create window of monitor size
            
            c=itemBox.get()

            frame=LabelFrame(sec  ,text="products Details.. " ) #Box inner padding
            frame.pack(padx=10 ,pady= 20 ,fill=BOTH ,expand=1)

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
            price =Label(second_frame , text="Price \n (per" ,font='Times 12 bold').grid(row =0 ,column=3)
            discount =Label(second_frame , text="Discount",font='Times 12 bold').grid(row=0 ,column=4)
            tax =Label(second_frame , text="Tax( in %)" ,font='Times 12 bold').grid(row=0 ,column=5)
            
            global grid
            grid=[]

            # Align Entry wedget in grid fashion

            for i in range(c):
                grid.append([])

                for j in range(5):

                    #This x label object will print serial no before each row . 

                    x=Label(second_frame ,text=i+1,font='Times 12 bold',padx="5").grid(row=i+1 ,column=0 )  

                    emailBox=Entry(second_frame ,width=30 )
                    emailBox.grid(row=i+1 ,column=j+1 , pady=5,padx=5   )
                    grid[i].append(emailBox)  
            genrate=Button(second_frame,text="Genrate Bill" ,command =show ,padx=5 ,width =20)   #button to insert items 
            genrate.grid(row=c+1,column= 3, pady=15,padx=15 )
            
    else:
        messagebox.showwarning("Alert" ,"Oops you enter wrong mobile number")

    
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
button =Button(window,text ="Genrate Bill" ,width ='30' ,padx ="20",command=genrateBill)   #button to show final detail to user for further modification
sale   =Button(window,
               text ="Show sales" ,
               width="30",
               padx="20")
hading.pack()
button.pack()
sale.pack(pady="20")
window.mainloop()