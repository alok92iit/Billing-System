#creating the pdf
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate
def printpdf():
    global l
    global grandtotal
    global total 
    filename ='billpdf.pdf'
    shopname='Shop Name'
    slogan='Any slogan'
    address1='Address line one'
    address2 ="Adress line two "
    shopmobile="96856xxx45"
    consumerName="Name of consumer"
    consumerMobile='886642655xx'
    consumerEmailId="xyz@gmail.com"
    conaddress1="consumer address line one"
    conaddress2="consumer address line two"
    pdf=canvas.Canvas(filename)
    pdf.setFont('Helvetica-Bold',48)
    pdf.setTitle("Invoice")

    pdf.drawString(350,750,'INVOICE')
    pdf.setFontSize(28)
    pdf.drawString(50,740,shopname)
    pdf.setFont('Times-Italic',18)
    pdf.drawString(50,722,slogan)
    pdf.setFont("Courier-Bold",12)
    pdf.drawString(50,690,address1)
    pdf.drawString(50,670,address2)
    pdf.drawString(50,650,'Mobile number :'+shopmobile)

    pdf.drawString(50,620,"Customer Name :"+consumerName)
    pdf.drawString(50,600,'Mobile Number :'+consumerMobile)
    pdf.drawString(50,580,'Email Id :'+consumerEmailId)
    pdf.drawString(50,560,'Customer Address :'+conaddress1 )
    pdf.drawString(175,545, conaddress2)

    pdf.line(30,535,550,535)        #first horizontal line  
    pdf.setFont("Courier-Bold",11)
    pdf.drawString(30,520,"Sr.No.")
    pdf.drawString(75,520,"Product Name")
    pdf.drawString(200,520,"Quantity")
    pdf.drawString(260,520,"Rate")
    pdf.drawString(340,520,"Discount")
    pdf.drawString(400,520,"Tax")
    pdf.drawString(490,520,"Total")

    pdf.line(30,515,550,515)        #second horizontal line 
    pdf.line(73,535,73,150)         #first vertical line
    pdf.line(198,535,198,150)       #second vertical line 
    pdf.line(258,535,258,150)       #third vertical line
    pdf.line(338,535,338,150)       #fourth vertical line
    pdf.line(398,535,398,150)       #fivth vertical line 
    pdf.line(488,535,488,150)       #sixth vertical line
    pdf.line(30,150,550,150)        #third horizontal line
    """
    def rightalingn(pdf,string,left,right,ycoordinate):
        length=len(string)
        totalLength=(right-left)/7
        print(totalLength)
        spaces=int(totalLength-length)
        print(spaces)
        pdf.drawString(right,ycoordinate," "*spaces)
        left=left+(7*spaces)
        pdf.drawString(left,ycoordinate,string)
    """
    pdf.drawString(30,135,"Total Discount:")
#    rightalingn(pdf,"-"+"%.2f" +" INR",393,488,135)
    pdf.drawString(30,120,"Gross Total(Discount Included):")
 #   rightalingn(pdf,"%.2f" +" INR",400,488,120)
    pdf.drawString(30,105,"Tax:")
  #  rightalingn(pdf,"+"+"%.2f" " INR",393,488,105)
    pdf.line(30,100,550,100)
    pdf.drawString(30,90,"Grand Total: ")
   # rightalingn(pdf,"%.2f" +" INR",400,488,90)
    pdf.drawString(400,50,"Authorized Signatory")
    print("when pdf clic ",l)
    print("totals list",total)
    print("op list ",op)
    #####################CUSTOMER DATA TO PRINT ON PDF ############################################
    ycoordinate=500
    for i in range(len(l)):
        pdf.drawString(50,ycoordinate,str(i+1) )
        pdf.drawString(80,ycoordinate,l[i][0] )
        pdf.drawString(205,ycoordinate,l[i][1] )
        pdf.drawString(262,ycoordinate,str(l[i][2])+' '+op[i]  )
        pdf.drawString(345,ycoordinate,l[i][3] )
        pdf.drawString(405,ycoordinate,l[i][3] )
        pdf.drawString(495,ycoordinate,str(total[i]) )
        ycoordinate=ycoordinate-15
    pdf.drawString(495,90,str(grandtotal) )
    pdf.save()


fontL ='Times 18'        #font style for labels
fontE ='Times 16' #font style for entry wedget
#Contains all form labels
global extraitem
extraitem=[]
def dropM(event):
     return(event)
def validateAdd(ko):
            global sno
            global grandtotal
            mdlist=ko
            l.append(mdlist[1:])
            print("when add click", l)
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
                        op.append(r[0])
                        
                        extraitem.append(sno)
                        updatetotal=modifyTotal(-1,0,r)
                        total.append(updatetotal[0])
                        print("\n when add clicked total is ",total)
                        print("\n when add clicked op is ",op)
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
    loop=itemBox.get()
    rmvitems= list(selectedItems)
    itemSelected=0
    
    for i in range (len(rmvitems)):
        if int(rmvitems[i]) in list(range(loop)):
            itemSelected+=1   
    for i in range(0,loop-itemSelected):
        if mdlist[1:]==l[i]:
                dublicate +=1
        else:
                nodublicate +=1
    
    if nodublicate== loop-itemSelected:
        validateAdd(mdlist)
    else:        
            option=messagebox.askyesno("Warning",'the entered details are already exist do you add the same record one more time or not ?')
            if option==True:
                validateAdd(mdlist)
def validateModify(extralist,x ,iid):
        mdlist=extralist
        i=x
        iidno =iid
        global grandtotal
        l[i][0]=mdlist[1]
        l[i][1]=mdlist[2]
        l[i][2]=mdlist[3]
        l[i][3]=mdlist[4]
        l[i][4]=mdlist[5]
        print("when modify click",l)
        #try:
            
        r=[dropMod.get()]
        if r[0] =='Choose':
                messagebox.showinfo("Alert","Please select price at  quantity")
        elif l[i][0]=='' or l[i][1]=='' or l[i][2]=='' or l[i][0].isnumeric():
                 messagebox.showinfo('Alert','Either you miss somthing Or make some mistake product name')
        elif float(l[i][2]) <0:
                messagebox.showinfo('Alert','Please enter correct price of product')       
        elif l[i][1][-2:] not in ['kg','gm','ps']:
                messagebox.showinfo("Alert",'Please add unit of quantity you want to buy')
        elif r[0]=='per 1ps' and l[i][1][-2:] in ['kg','gm+'] or l[i][1][-2:]=='ps' and r[0] in ['per 1kg','per 100g'] :
                messagebox.showinfo('Alert','oops.. you select wrong combintion of quantity and price per unit')
        elif l[i][1][:-2] =='':
                messagebox.showinfo('Alert','please assign quantity in digit also \n(example  12kg)')
        elif  float(l[i][1][:-2]) <=  0 :
                messagebox.showinfo('Alert' ,'Please check quantity nigther 0 nor negative')
        elif  float(l[i][3]) < 0 or float(l[i][4]) <0:
                messagebox.showinfo('Alert' ,'You enter invalid discount and tax %')
        else:
                
                pricetotal=my_treeview.item(iidno,'values')
                grandtotal = grandtotal -float(pricetotal[5])
                updatetotal=modifyTotal(i,i+1,r)
                total[i]=updatetotal[0]
                print("total ",total)
                op[i]=r[0]
                grandtotal =grandtotal + updatetotal[0]
                my_treeview.item(iidno,text=iidno+1,values=(l[i][0],l[i][1],str(l[i][2])+" "+r[0],l[i][3],l[i][4],updatetotal[0]))
                my_treeview.item(101,text='',value=('','','','','Grand Total', grandtotal))
                        
  #  except : 
   #     messagebox.showinfo('Alert' ,'Please enter valid value of quantity in row \n or \t \t \n You enter wrong amount \n or \n You enter invalid discount and tax in row no{} ')

                
def modifies():
    mdlist=[i.get() for i in mod]
    selectedItems =my_treeview.selection()
#    if mdlist[0].isnumeric():
    i=int(selectedItems[0])
    indxPostion =my_treeview.index(i)
    print("selected item to modifies",selectedItems)#serial which user want to modify 
  #  if i<=itemBox.get()-1 and i+1>0:

    print(i)
    print(indxPostion)
    
    validateModify(mdlist,indxPostion,i)
   # elif i in extraitem:
    
    #    validateModify(mdlist,i)
     #   else:
      #      messagebox.showinfo('Alert','Please enter correct serial number')
    #else:
     #   messagebox.showinfo('Alert','please enter serial number in digits')
def removeRecord():
    global grandtotal
    global selectedItems
    selectedItems =my_treeview.selection() # will select selected record selection() method will return tuple that contain iid no 
                                        #in form of string
    temp=' '.join([str(int(y)+1) for y in selectedItems]) # add 1 to see the serial number 

    yesN0=messagebox.askyesno("Alert" ,'Selected serial numbers {} for removing form list'.format(temp))
    if yesN0==True:
        for item in selectedItems:
            indexpstnofItem =my_treeview.index(item)
            pricetotal=my_treeview.item(item,'values')
            my_treeview.delete(item)
            grandtotal = grandtotal -float(pricetotal[5])
            print("the removed item is ",l[indexpstnofItem])
            l.remove(l[indexpstnofItem])
            op.remove(op[indexpstnofItem])
            total.remove(total[indexpstnofItem])
            
        print("when remove click",l)
        print('op list is',op)
        
        my_treeview.item(101,text='',value=('','','','','Grand Total', grandtotal))    
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
            createpdf=Button(modification,text='Genrate Invoice',command =printpdf)
            createpdf.grid(row=3,column=0)
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