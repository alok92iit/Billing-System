from tkinter import *
from tkinter import messagebox
from tkinter import ttk

fontL ='Times 18'        #font style for labels
fontE ='Times 16' #font style for entry wedget
#Contains all form labels  
def dropM(event):
     return(event)
def validateAdd(ko):
            global sno
            global grandtotal
            mdlist=ko
            l.append(mdlist[1:])

            try:
            
                r=[dropMod.get()]
                if r[0] =='Choose':
                        messagebox.showinfo("Alert","Please select price at  quantity")
                elif l[-1][0]=='' or l[-1][1]=='' or l[-1][2]=='' or l[-1][0].isnumeric():
                        messagebox.showinfo('Alert','Either you miss somthing Or make some mistake product name')
                elif float(l[-1][2]) <0:
                        messagebox.showinfo('Alert','Please enter correct price of product')       
                elif l[-1][1][-2:] not in ['kg','gm','ps']:
                        messagebox.showinfo("Alert",'Please add unit of quantity you want to buy')
                elif r[0]=='per 1ps' and l[-1][1][-2:] in ['kg','gm'] or l[-1][1][-2:]=='ps' and r[0] in ['per 1kg','per 100g'] :
                        messagebox.showinfo('Alert','oops.. you select wrong combintion of quantity and price per unit')
                elif l[-1][1][:-2] =='':
                        messagebox.showinfo('Alert','please assign quantity in digit also \n(example  12kg)')
                elif  float(l[-1][1][:-2]) <=  0 :
                        messagebox.showinfo('Alert' ,'Please check quantity nigther 0 nor negative')
                elif  float(l[-1][3]) < 0 or float(l[-1][4]) <0:
                        messagebox.showinfo('Alert' ,'You enter invalid discount and tax %')
                else: 
                        global extraitem
                        extraitem=[]
                        extraitem.append(sno)
                        updatetotal=modifyTotal(-1,0,r)
                        grandtotal=grandtotal + updatetotal[0]
                        my_treeview.delete('101')
                        my_treeview.insert(parent='' ,index='end', iid=sno,text=sno+1,values =(l[-1][0],l[-1][1],str(l[-1][2])+" "+r[0],l[-1][3],l[-1][4],updatetotal[0]))
                        sno +=1
                        my_treeview.insert(parent='', index='end' ,iid=101,text='',value=('','','','','Grand Total', grandtotal))
            except : 
                messagebox.showinfo('Alert' ,'Please enter valid value of quantity in row \n or \t \t \n You enter wrong amount \n or \n You enter invalid discount and tax')


def addrecord():
    mdlist=[i.get() for i in mod]
    nodublicate=0
    dublicate=0 
    for i in range(0,itemBox.get()):
        if mdlist[1:]==l[i]:
            dublicate +=1
        else:
            nodublicate +=1
    if nodublicate== itemBox.get():
        validateAdd(mdlist)
    else:        
            option=messagebox.askyesno("Warning",'the entered details are already exist do you add the same record one more time or not ?')
            if option==True:
                validateAdd(mdlist)
            else:
                entry1.delete(0,END)
def validateModify(extralist,x):
    mdlist=extralist
    i=x
    global grandtotal
    l[i][0]=mdlist[1]
    l[i][1]=mdlist[2]
    l[i][2]=mdlist[3]
    l[i][3]=mdlist[4]
    l[i][4]=mdlist[5]
    try:
            
        r=[dropMod.get()]
        if r[0] =='Choose':
                messagebox.showinfo("Alert","Please select price at  quantity")
        elif l[i][0]=='' or l[i][1]=='' or l[i][2]=='' or l[i][0].isnumeric():
                 messagebox.showinfo('Alert','Either you miss somthing Or make some mistake product name')
        elif float(l[i][2]) <0:
                messagebox.showinfo('Alert','Please enter correct price of product')       
        elif l[i][1][-2:] not in ['kg','gm','ps']:
                messagebox.showinfo("Alert",'Please add unit of quantity you want to buy')
        elif r[0]=='per 1ps' and l[i][1][-2:] in ['kg','gm'] or l[i][1][-2:]=='ps' and r[0] in ['per 1kg','per 100g'] :
                messagebox.showinfo('Alert','oops.. you select wrong combintion of quantity and price per unit')
        elif l[i][1][:-2] =='':
                messagebox.showinfo('Alert','please assign quantity in digit also \n(example  12kg)')
        elif  float(l[i][1][:-2]) <=  0 :
                messagebox.showinfo('Alert' ,'Please check quantity nigther 0 nor negative')
        elif  float(l[i][3]) < 0 or float(l[i][4]) <0:
                messagebox.showinfo('Alert' ,'You enter invalid discount and tax %')
        else:
               
                pricetotal=my_treeview.item(i,'values')
                grandtotal = grandtotal -float(pricetotal[5])
                updatetotal=modifyTotal(i,i+1,r)
                grandtotal =grandtotal + updatetotal[0]
                my_treeview.item(i,text=i+1,values=(l[i][0],l[i][1],str(l[i][2])+" "+r[0],l[i][3],l[i][4],updatetotal[0]))
                my_treeview.item(101,text='',value=('','','','','Grand Total', grandtotal))
                        
    except : 
        messagebox.showinfo('Alert' ,'Please enter valid value of quantity in row \n or \t \t \n You enter wrong amount \n or \n You enter invalid discount and tax in row no{} ')

                
def modifies():
    mdlist=[i.get() for i in mod]
    
    if mdlist[0].isnumeric():
        i=int(mdlist[0]) -1          #serial which user want to modify 
        if i<=itemBox.get()-1 and i+1>0:
            validateModify(mdlist,i)
        elif i in extraitem:
            print(i)
            validateModify(mdlist,i)
        else:
            messagebox.showinfo('Alert','Please enter correct serial number')
    #else:
     #   messagebox.showinfo('Alert','please enter serial number in digits')
def removeRecord():
    selectedItems =my_treeview.selection()
    temp=' '.join([str(int(y)+1) for y in selectedItems])
    yesN0=messagebox.askyesno("Alert" ,'Selected serial numbers {} for removing form list'.format(temp))
    if yesN0==True:
        for item in selectedItems:
            my_treeview.delete(item)
            l.remove(l[int(item)])
            op.remove(l[int(item)])
def modifyTotal(intial,end,f): #This funtion simply calculate total price of the productand return list of total value of every product
            u=intial
            totalprs=[]
            endval=end
            tmpl=f
            
            for i in range(u,endval): 
                #if no discount and no tax 
                    if l[i][1][-2:]=='kg':  
                        if tmpl[0]=='per 1kg':
                            tax= float(l[i][4])/100
                            discount=float(l[i][3])/100
                            pricepergram= float(l[i][2])/1000
                            actualprice =float(l[i][1][:-2])*pricepergram*1000 +tax -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
             
                        elif tmpl[0]=='per 100g':
                            tax= float(l[i][4])/100
                            discount=float(l[i][3])/100
                            pricepergram= float(l[i][2])/100
                            actualprice =float(l[i][1][:-2])*pricepergram*1000 +tax -discount
                         #   actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            
                    elif l[i][1][-2:]=='gm':
                        if tmpl[0]=='per 100g':
                            tax= float(l[i][4])/100
                            discount=float(l[i][3])/100
                            pricepergram= float(l[i][2])/100
                            actualprice =float(l[i][1][:-2])*pricepergram  +tax -discount 
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                        
                        elif tmpl[0]=='per 1kg':
                            tax= float(l[i][4])/100
                            discount=float(l[i][3])/100
                            pricepergram= float(l[i][2])/1000
                            actualprice =float(l[i][1][:-2])*pricepergram +tax -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            
                    elif l[i][1][-2:]=='ps':
                        if tmpl[0]=='per 1ps':
                            tax= float(l[i][4])/100
                            discount=float(l[i][3])/100
                            pricepergram= float(l[i][2])
                            actualprice =int(l[i][1][:-2])*pricepergram  +tax -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
            return(totalprs)

def calTotal(intialval ,lastval ,f): #This funtion simply calculate total price of the productand return list of total value of every product
            u=intialval
            totalprs=[]
            endval=lastval
            tmpl=f
            
            while u<endval: 
                #if no discount and no tax
                if l[u][3]=='' and l[u][4]=='':    
                    if l[u][1][-2:]=='kg':  
                        if tmpl[u]=='per 1kg':
                            pricepergram= float(l[u][2])/1000
                            actualprice =round(float(l[u][1][:-2])*pricepergram*1000,2)
                            totalprs.append(actualprice)
                            u +=1 
                        elif tmpl[u]=='per 100g':
                            pricepergram= float(l[u][2])/100
                            actualprice =round(float(l[u][1][:-2])*pricepergram*1000,2)
                            totalprs.append(actualprice)
                            u +=1 
                    elif l[u][1][-2:]=='gm':
                        if tmpl[u]=='per 100g':
                            pricepergram= float(l[u][2])/100
                            actualprice =round(float(l[u][1][:-2])*pricepergram,2)
                            totalprs.append(actualprice)
                            u +=1 
                        elif tmpl[u]=='per 1kg':
                            pricepergram= float(l[u][2])/1000
                            actualprice =round(float(l[u][1][:-2])*pricepergram,2)
                            totalprs.append(actualprice)
                            u +=1
                    elif l[u][1][-2:]=='ps':
                        if tmpl[u]=='per 1ps':
                            pricepergram= float(l[u][2])
                            actualprice =round(int(l[u][1][:-2])*pricepergram,2)
                            totalprs.append(actualprice)
            # if thier is no tax on product
            #discount apply on total price of product
                elif l[u][4]=='':
                    if l[u][1][-2:]=='kg':  
                        if tmpl[u]=='per 1kg':
                            discount= float(l[u][3])/100
                            pricepergram= float(l[u][2])/1000
                            actualprice =float(l[u][1][:-2])*pricepergram*1000 -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1 
                        elif tmpl[u]=='per 100g':
                            discount= float(l[u][3])/100
                            pricepergram= float(l[u][2])/100
                            actualprice =float(l[u][1][:-2])*pricepergram*1000 -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1 
                    elif l[u][1][-2:]=='gm':
                        if tmpl[u]=='per 100g':
                            discount= float(l[u][3])/100
                            pricepergram= float(l[u][2])/100
                            actualprice =float(l[u][1][:-2])*pricepergram -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1 
                        elif tmpl[u]=='per 1kg':
                            discount= float(l[u][3])/100
                            pricepergram= float(l[u][2])/1000
                            actualprice =float(l[u][1][:-2])*pricepergram -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1
                    elif l[u][1][-2:]=='ps':
                        if tmpl[u]=='per 1ps':
                            discount= float(l[u][3])/100
                            pricepergram= float(l[u][2])
                            actualprice =int(l[u][1][:-2])*pricepergram -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1
                elif l[u][3]=='':
                    tax=0
                    if l[u][1][-2:]=='kg':  
                        if tmpl[u]=='per 1kg':
                            tax= float(l[u][4])/100
                            pricepergram= float(l[u][2])/1000
                            actualprice =float(l[u][1][:-2])*pricepergram*1000 +tax
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1 
                        elif tmpl[u]=='per 100g':
                            tax= float(l[u][4])/100
                            pricepergram= float(l[u][2])/100
                            actualprice =float(l[u][1][:-2])*pricepergram*1000 +tax
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1 
                    elif l[u][1][-2:]=='gm':
                        if tmpl[u]=='per 100g':
                            tax= float(l[u][4])/100
                            pricepergram= float(l[u][2])/100
                            actualprice =float(l[u][1][:-2])*pricepergram  +tax
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1 
                        elif tmpl[u]=='per 1kg':
                            tax= float(l[u][4])/100
                            pricepergram= float(l[u][2])/1000
                            actualprice =float(l[u][1][:-2])*pricepergram +tax
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1
                    elif l[u][1][-2:]=='ps':
                        if tmpl[u]=='per 1ps':
                            tax= float(l[u][4])/100
                            pricepergram= float(l[u][2])
                            actualprice =int(l[u][1][:-2])*pricepergram  +tax
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1
                else: 
                    if l[u][1][-2:]=='kg':  
                        if tmpl[u]=='per 1kg':
                            tax= float(l[u][4])/100
                            discount=float(l[u][3])/100
                            pricepergram= float(l[u][2])/1000
                            actualprice =float(l[u][1][:-2])*pricepergram*1000 +tax -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1 
                        elif tmpl[u]=='per 100g':
                            tax= float(l[u][4])/100
                            discount=float(l[u][3])/100
                            pricepergram= float(l[u][2])/100
                            actualprice =float(l[u][1][:-2])*pricepergram*1000 +tax -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1 
                    elif l[u][1][-2:]=='gm':
                        if tmpl[u]=='per 100g':
                            tax= float(l[u][4])/100
                            discount=float(l[u][3])/100
                            pricepergram= float(l[u][2])/100
                            actualprice =float(l[u][1][:-2])*pricepergram  +tax -discount 
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1 
                        elif tmpl[u]=='per 1kg':
                            tax= float(l[u][4])/100
                            discount=float(l[u][3])/100
                            pricepergram= float(l[u][2])/1000
                            actualprice =float(l[u][1][:-2])*pricepergram +tax -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1
                    elif l[u][1][-2:]=='ps':
                        if tmpl[u]=='per 1ps':
                            tax= float(l[u][4])/100
                            discount=float(l[u][3])/100
                            pricepergram= float(l[u][2])
                            actualprice =int(l[u][1][:-2])*pricepergram  +tax -discount
                            actualprice=round(actualprice,2)
                            totalprs.append(actualprice)
                            u +=1
            return(totalprs)
def columnName(frameName):
    frame=frameName
    sn0=Label(frame ,text ="S.No",font='Times 12 bold').grid(row =0 ,column= 0)
    product=Label(frame  ,text="Product Name",font='Times 12 bold').grid(row=0 ,column=1)
    quantity=Label(frame , text="Quantity \n (eg:1gm,1kg,1ps)",font='Times 12 bold').grid(row=0,column=2)
    price =Label(frame , text="Price \n " ,font='Times 12 bold').grid(row =0 ,column=3)
    pricePer  =Label(frame , text="Per \n 100g/1kg/1ps" ,font='Times 12 bold').grid(row =0 ,column=4)

    discount =Label(frame , text="Discount in %",font='Times 12 bold').grid(row=0 ,column=5)
    tax =Label(frame , text="Tax in %" ,font='Times 12 bold').grid(row=0 ,column=6)
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
def show(): #third window
    #Window that will show the data
    temp=0      #temp use to all condition for each row
    itemsno=itemBox.get()
    global l
    l= [[grid[i][j].get() for j in range(5)] for i in range(itemsno)]
    try:
        for i in range(itemsno):
            if l[i][0]=='' or l[i][1]=='' or l[i][2]=='' or l[i][0].isnumeric():
                    messagebox.showinfo('Alert','You miss somthing in row number {} .\n\t\tOr\n Make some mistake product name'.format(i+1) )
            elif float(l[i][2]) <0:
                messagebox.showinfo('Alert','Please enter correct price of product in row {}'.format(i+1))       
            elif l[i][1][-2:] not in ['kg','gm','ps']:
                messagebox.showinfo("Alert",'Please add unit of quantity you want to buy in row {}'.format(i+1))
            elif op[i]=='per 1ps' and l[i][1][-2:] in ['kg','gm'] or l[i][1][-2:]=='ps' and op[i] in ['per 1kg','per 100g'] :
                messagebox.showinfo('Alert','oops.. you select wrong combintion of quantity and price per unit')
                frame.destroy()
                ok.config(state=NORMAL)

            elif l[i][1][:-2] =='':
                messagebox.showinfo('Alert','please assign quantity in digit also \n(example  12kg)')

            elif  float(l[i][1][:-2]) <=  0 :
                messagebox.showinfo('Alert' ,'Please check quantity nigther 0 nor negative in row {}'.format(i+1))

            elif  float(l[i][3]) < 0 or float(l[i][4]) <0:
                messagebox.showinfo('Alert' ,'You enter invalid discount and tax %')
            else:
                temp+=1
    except: 
            messagebox.showinfo('Alert' ,'Please enter valid value of quantity in row \n or \t \t \n You enter wrong amount \n or \n You enter invalid discount and tax in row no{} '.format(i+1))
        
    if temp==itemsno :
        if len(op)==itemsno:
            global total
            total=calTotal(0,itemsno,op)   #Return list of total values
            showWin =Toplevel() 
            showWin.geometry('{}x{}'.format(showWin.winfo_screenwidth(),showWin.winfo_screenheight()))
                    #this section only show the customer details
            global buyerData
            buyerData =LabelFrame(showWin, text="Consumer Details..")
            buyerData.pack(fill= BOTH ,pady =10 ,padx=10 )

            labels(buyerData)          #Call fuction that display label(eg Name Mobile no ..)
            labelUserData(buyerData)   #Call fuction that display user data enter in entry wedget

            productData=LabelFrame(showWin ,text="Product Details..")
            productData.pack(fill=X,pady=10 ,padx=10) 
            
            scrollbar= Scrollbar(productData) 
            scrollbar.pack(side=RIGHT ,fill=Y)
            
            global my_treeview
            my_treeview =ttk.Treeview(productData ,yscrollcommand=scrollbar.set )
            my_treeview.pack(fill=BOTH ) 
            
            scrollbar.config(command=my_treeview.yview)
                    #define columns 
            my_treeview['columns'] =('Product Name','Quantity','Price', 'Discount','Tax','Total')
                    #formatting t tree

            my_treeview.column('#0',width=10,anchor=W)     #Phantom column(extra column)
            my_treeview.column('Product Name' ,width=75,anchor=W)  
            my_treeview.column('Quantity', width=50 ,anchor=W)
            my_treeview.column('Price' ,width=75 ,anchor=W)
            my_treeview.column('Discount' ,width=50 ,anchor=W)
            my_treeview.column('Tax' ,width=50 , anchor=W)
            my_treeview.column('Total' ,width=75 ,anchor=W)

            my_treeview.heading('#0',text='S.No',anchor=W)
            my_treeview.heading('Product Name',text='Product Name' ,anchor=W)
            my_treeview.heading('Quantity',text='Quantity',anchor=W)
            my_treeview.heading('Price' ,text='Price Per 100g/1kg/1ps',anchor=W)
            
            my_treeview.heading('Discount' ,text='Discount' ,anchor=W)
            my_treeview.heading('Tax' ,text='Tax' ,anchor=W)
            my_treeview.heading('Total',text='Total' ,anchor=W)
            ps=itemsno
            global sno
            sno=0
            global grandtotal
            grandtotal=0
            for i in range(ps):
                    grandtotal= grandtotal +total[i]
                    my_treeview.insert(parent='' ,index='end',iid = sno, text=i+1,
                                    values=(l[i][0], l[i][1], str(l[i][2])+" "+op[i] ,l[i][3],l[i][4] ,total[i]))
                    sno +=1
            my_treeview.insert(parent='', index='end' ,iid=101,text='',value=('','','','','Grand Total', grandtotal))
            modification=LabelFrame(showWin,text='Modification Section..')
            modification.pack(pady=10 ,padx=10) 

            
            columnName(modification) #display labels of product details
            global mod
            mod =[]
            for x in range (7):   
                if x==4 :
                    dropMod.set('Choose')
                    drop=OptionMenu(modification ,dropMod,'per 100g','per 1kg','per 1ps',command=dropM)
                    drop.grid(row=1 ,column =4)
                    
                else :
                    
                    entry1= Entry(modification,width=30 )
                    entry1.grid(row=1 ,column=x , pady=5,padx=5)
                    mod.append(entry1)
            addRecord=Button(modification ,text='Add Record' ,command=addrecord).grid(row=2 ,column =2)
            modify= Button(modification ,text="Modify It" ,command = modifies)
            modify.grid(row=2 ,column =3)
            remove=Button(modification,text='Remove Record' ,command=removeRecord)
            remove.grid(row=2,column =4)
        else:
            response=messagebox.showinfo('Alert','Please select price per 100g/1kg/1ps \n make choose in one click multiple click genrate error ')
            frame.destroy()
            ok.config(state=NORMAL)
                       
                    
def drop(event):  
    op.append(event)    
    
def insertData():

    name=Name.get().strip()
    mobileno =mobno.get()
    tor=[]                #this list is use to genrate variable class for dropdownbox
    global c
    c=itemBox.get()
    for i in range(c):
        tor.append(i)
        tor[i]=IntVar()
    if(len(name) <= 2):
        messagebox.showwarning("Alert" ,"Please Enter Valid Name")
    
    elif(len(mobileno) == 0 or len(mobileno)==10):
    
            ok.config(state=DISABLED)  #config() to change coniguration of ok button to Disable ok button of frame1
            sec.geometry('{}x{}'.format(sec.winfo_screenwidth(),sec.winfo_screenheight())) #create window of monitor size
            
            global frame
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

            columnName(second_frame)
            
            global grid
            grid=[]
            # Align Entry wedget in grid fashion
            global op 
            op=[]            #this list contains dropdownbox choice
            for i in range(c):
                grid.append([])
                for j in range(6):

                    #This x label object will print serial no before each row . 
                    
                    x=Label(second_frame ,text=i+1,font='Times 12 bold',padx="5").grid(row=i+1 ,column=0 )  
                    
                    if j==3:
                        tor[i].set('Choose')
                        dropbox=OptionMenu(second_frame,tor[i] ,'per 100g','per 1kg','per 1ps', command=drop).grid(row=i+1,column=j+1,pady=5,padx=5 )
                    else:
                        emailBox=Entry(second_frame ,width=30 )
                        emailBox.grid(row=i+1 ,column=j+1 , pady=5,padx=5   )
                        grid[i].append(emailBox)  
            genrate=Button(second_frame,text="Genrate Bill" ,command =show ,padx=5 ,width =20)   #button to insert items 
            genrate.grid(row=c+1,column= 3, pady=15,padx=15 )
            
    else:
        messagebox.showwarning("Alert" ,"Oops you enter wrong mobile number")
        
    
window=Tk() # Main window of application

Name=StringVar()
mobno=StringVar()
Address=StringVar()
EmailId=StringVar()
dropMod=StringVar()
modifyentry=StringVar()


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