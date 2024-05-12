import tkinter
from tkinter import messagebox, filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def nextpage2():
    firstpage.pack_forget()
    secondpage.pack()

def prevpage1():
    secondpage.pack_forget()
    firstpage.pack()

def nextpage3():
    global insname,semname
    insname = insnameentry.get()
    semname = semnameentry.get()
    secondpage.pack_forget()
    thirdpage.pack()

def prevpage2():
    thirdpage.pack_forget()
    secondpage.pack()

def nextpage4():
    global sub1name,sub2name,sub3name,sub4name,sub5name
    global sub1entry   
    sub1name = sub1entry.get()
    sub2name = sub2entry.get()
    sub3name = sub3entry.get()
    sub4name = sub4entry.get()
    sub5name = sub5entry.get()
    thirdpage.pack_forget()
    fourthpage.pack()

def prevpage3():
    fourthpage.pack_forget()
    thirdpage.pack()

def nextpage5():
    global stuname,sturollno,sturegno
    stuname = stunameentry.get()
    sturollno = sturollnoentry.get()
    sturegno = sturegnoentry.get()
    fourthpage.pack_forget()
    fifthpage.pack()

    #Subject 1 Marks Label
    sub1mlabfosi = ("Calibari",20)
    sub1mlab = tkinter.Label(fifthpage,text=f"{sub1name} :",font=sub1mlabfosi)
    sub1mlab.grid(row=1,column=0,sticky="W",pady=20)

    #Subject 2 Marks Label
    sub2mlabfosi = ("Calibari",20)
    sub2mlab = tkinter.Label(fifthpage,text=f"{sub2name} :",font=sub2mlabfosi)
    sub2mlab.grid(row=2,column=0,sticky="W",pady=20)  

    #Subject 3 Marks Label
    sub3mlabfosi = ("Calibari",20)
    sub3mlab = tkinter.Label(fifthpage,text=f"{sub3name} :",font=sub3mlabfosi)
    sub3mlab.grid(row=3,column=0,sticky="W",pady=20)  

    #Subject 4 Marks Label
    sub4mlabfosi = ("Calibari",20)
    sub4mlab = tkinter.Label(fifthpage,text=f"{sub4name} :",font=sub4mlabfosi)
    sub4mlab.grid(row=4,column=0,sticky="W",pady=20)  

    #Subject 5 Marks Label
    sub5mlabfosi = ("Calibari",20)
    sub5mlab = tkinter.Label(fifthpage,text=f"{sub5name} :",font=sub5mlabfosi)
    sub5mlab.grid(row=5,column=0,sticky="W",pady=20)     

def prevpage4():
    fifthpage.pack_forget()
    fourthpage.pack()

def nextpage6():
    global sub1m,sub2m,sub3m,sub4m,sub5m
    global total,avg,percentage
    sub1m = int(sub1mentry.get())
    sub2m = int(sub2mentry.get())
    sub3m = int(sub3mentry.get())
    sub4m = int(sub4mentry.get())
    sub5m = int(sub5mentry.get())
    fifthpage.pack_forget()
    sixthpage.pack()
    total = sub1m + sub2m + sub3m + sub4m + sub5m
    avg = total / 5
    percentage = avg
    
def prevpage5():
    sixthpage.pack_forget()
    fifthpage.pack()

def genpdfms():
    global insname,semname,sub1name,sub2name,sub3name,sub4name,sub5name,stuname,sturollno,sturegno,sub1m,sub2m,sub3m,sub4m,sub5m,total,avg,percentage

    # Asking the user for filename and location
    pdf_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    if pdf_filename:
        try:
            # calculating x coord positions
            x_centered = letter[0] / 2
            x_1octant = x_centered / 4
            x_7octant = x_1octant * 7
            x_6octant = x_7octant - x_1octant

            # initialization of the pdf page
            c = canvas.Canvas(pdf_filename, pagesize=letter)

            # displaying institution name
            c.setFont("Helvetica", 30)
            c.drawCentredString(x_centered, 725, f"==========\n{insname}\n==========")

            # displaying semester name
            c.setFontSize(21)
            c.drawCentredString(x_centered, 685, f"{semname}")
            c.drawCentredString(x_centered,665,"------------------------------------------------------------")

            # displaying Student Name,RollNo,RegNo
            c.setFontSize(16)
            c.drawString(x_1octant,615,text=f"Name:  {stuname}")
            c.drawString(x_1octant,585,text=f"Roll No:  {sturollno}")
            c.drawString(x_1octant,555,text=f"Registration No:  {sturegno}")
            c.drawCentredString(x_centered,510,"--------------------------------------------------------------------------------------------------------------")

            # displaying subjects & marks heading
            c.drawString(x_1octant,490,text="Subjects")
            c.drawString(x_7octant,490,text="| Marks")
            c.drawCentredString(x_centered,470,"--------------------------------------------------------------------------------------------------------------")
            c.drawCentredString(x_centered,460,"--------------------------------------------------------------------------------------------------------------")
            #displaying Subject 1 name & marks
            c.drawString(x_1octant,440,text=f"{sub1name}")
            c.drawString(x_7octant,440,text=f"| {sub1m}")
            c.drawCentredString(x_centered,420,"--------------------------------------------------------------------------------------------------------------")
            #displaying Subject 2 name & marks
            c.drawString(x_1octant,400,text=f"{sub2name}")
            c.drawString(x_7octant,400,text=f"| {sub2m}")
            c.drawCentredString(x_centered,380,"--------------------------------------------------------------------------------------------------------------")
            #displaying Subject 3 name & marks
            c.drawString(x_1octant,360,text=f"{sub3name}")
            c.drawString(x_7octant,360,text=f"| {sub3m}")
            c.drawCentredString(x_centered,340,"--------------------------------------------------------------------------------------------------------------")
            #displaying Subject 4 name & marks
            c.drawString(x_1octant,320,text=f"{sub4name}")
            c.drawString(x_7octant,320,text=f"| {sub4m}")
            c.drawCentredString(x_centered,300,"--------------------------------------------------------------------------------------------------------------")
            #displaying Subject 5 name & marks
            c.drawString(x_1octant,280,text=f"{sub5name}")
            c.drawString(x_7octant,280,text=f"| {sub5m}")
            c.drawCentredString(x_centered,260,"--------------------------------------------------------------------------------------------------------------")

            #displaying total,avg,percentage
            c.drawString((x_6octant-25),245,text="Total = ")
            c.drawString(x_7octant,245,text=f"{total}")
            c.drawString((x_6octant-25),225,text="Average = ")
            c.drawString(x_7octant,225,text=f"{avg}")
            c.drawString((x_6octant-25),205,text="Percentage = ")
            c.drawString(x_7octant,205,text=f"{percentage}%")

            # saving the pdf file and showing success/error message
            c.showPage()
            c.save()
            messagebox.showinfo("Success", "PDF generated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")



#creating main window
windowobj = tkinter.Tk()
windowobj.geometry("600x600")

#creating each page/frames
firstpage = tkinter.Frame(windowobj)
secondpage = tkinter.Frame(windowobj)
thirdpage = tkinter.Frame(windowobj)
fourthpage = tkinter.Frame(windowobj)
fifthpage = tkinter.Frame(windowobj)
sixthpage = tkinter.Frame(windowobj)
firstpage.pack()

#required variables
insname,semname = None,None
sub1name,sub2name,sub3name,sub4name,sub5name = None,None,None,None,None
stuname,sturollno,sturegno = None,None,None
sub1m,sub2m,sub3m,sub4m,sub5m = 0,0,0,0,0
total,avg,percentage = 0,0,0





#begining of page1

#intro Label
introlabfosi = ("Calibari",20)
introlab = tkinter.Label(firstpage, text = "🏫🥸📝Student Marksheet Generating Software📝🥸🏫",font=introlabfosi)
introlab.grid(row=0,column=0,sticky="N",pady=150)

#Lets's Begin Label
letbeglabfosi = ("Calibari",30)
letbeglab = tkinter.Label(firstpage, text = "Let's Begin...",font=letbeglabfosi)
letbeglab.grid(row=1,column=0,sticky="",pady=50)

#page1 announce
page1fosi = ("Calibari",10)
page1 = tkinter.Label(firstpage, text = "|Page 1|",font=page1fosi)
page1.grid(row=4,column=0,sticky="S",pady=95)

#to page2 from page1
nextbu2 = tkinter.Button(firstpage,text="next",command=nextpage2)
nextbu2.grid(row=3,column=0,sticky="E",pady=20)

#ending of page1





#begining of page2

#Prov Ins & Sem Label
insandsemdetlabfosi = ("Calibari",35)
insandsemdetlab = tkinter.Label(secondpage, text = "Provide Institution & Semester Details\n-------------------------------------------",font=insandsemdetlabfosi)
insandsemdetlab.grid(row=0,column=0,sticky="N",padx=50,pady=120)

#Ins name Label
insnamelabfosi = ("Calibari",20)
insnamelab = tkinter.Label(secondpage,text="Enter Institution name: ",font=insnamelabfosi)
insnamelab.grid(row=1,column=0,sticky="NW",padx=120,pady=20)

#Ins name Entry
insnameent = tkinter.StringVar(secondpage,value="")
insnameentry = tkinter.Entry(secondpage,textvariable=insnameent,width=35)
insnameentry.grid(row=1,column=0,sticky="NW",padx=420,pady=33)


#Sem name Label
semnamelabfosi = ("Calibari",20)
semnamelab = tkinter.Label(secondpage,text="Enter Semester name: ",font=semnamelabfosi)
semnamelab.grid(row=2,column=0,sticky="NW",padx=120,pady=20)

#Sem name Entry
semnameent = tkinter.StringVar(secondpage,value="")
semnameentry = tkinter.Entry(secondpage,textvariable=semnameent,width=35)
semnameentry.grid(row=2,column=0,sticky="NW",padx=420,pady=33)


#to page1 from page2
prevbu1 = tkinter.Button(secondpage,text="back",command=prevpage1)
prevbu1.grid(row=2,column=0,sticky="W",pady=130)

#page2 announce
page2fosi = ("Calibari",10)
page2 = tkinter.Label(secondpage, text = "|Page 2|",font=page2fosi)
page2.grid(row=3,column=0,sticky="N")

#to page3 from page2
nextbu3 = tkinter.Button(secondpage,text="next",command=nextpage3)
nextbu3.grid(row=2,column=0,sticky="E",pady=130)

#endling page2




#begining of page3

#Prov Sub Name Label
papnamedetlabfosi = ("Calibari",35)
papnamedetlab = tkinter.Label(thirdpage, text = "Provide Name of 5 Subjects\n-------------------------------------------",font=papnamedetlabfosi)
papnamedetlab.grid(row=0,column=0,sticky="N",padx=50,pady=60)


#Subject 1 Label
sub1labfosi = ("Calibari",20)
sub1lab = tkinter.Label(thirdpage,text="Subject 1: ",font=sub1labfosi)
sub1lab.grid(row=1,column=0,sticky="W",padx=120,pady=20)

#Subject 1 Entry
sub1ent = tkinter.StringVar(thirdpage,value="")
sub1entry = tkinter.Entry(thirdpage,textvariable=sub1ent,width=45)
sub1entry.grid(row=1,column=0,sticky="NW",padx=275,pady=33)

#Subject 2 Label
sub2labfosi = ("Calibari",20)
sub2lab = tkinter.Label(thirdpage,text="Subject 2: ",font=sub2labfosi)
sub2lab.grid(row=2,column=0,sticky="W",padx=120,pady=20)

#Subject 2 Entry
sub2ent = tkinter.StringVar(thirdpage,value="")
sub2entry = tkinter.Entry(thirdpage,textvariable=sub2ent,width=45)
sub2entry.grid(row=2,column=0,sticky="NW",padx=275,pady=33)

#Subject 3 Labe
sub3labfosi = ("Calibari",20)
sub3lab = tkinter.Label(thirdpage,text="Subject 3: ",font=sub3labfosi)
sub3lab.grid(row=3,column=0,sticky="W",padx=120,pady=20)

#Subject 3 Entry
sub3ent = tkinter.StringVar(thirdpage,value="")
sub3entry = tkinter.Entry(thirdpage,textvariable=sub3ent,width=45)
sub3entry.grid(row=3,column=0,sticky="NW",padx=275,pady=33)

#Subject 4 Label
sub4labfosi = ("Calibari",20)
sub4lab = tkinter.Label(thirdpage,text="Subject 4: ",font=sub4labfosi)
sub4lab.grid(row=4,column=0,sticky="W",padx=120,pady=20)

#Subject 4 Entry
sub4ent = tkinter.StringVar(thirdpage,value="")
sub4entry = tkinter.Entry(thirdpage,textvariable=sub4ent,width=45)
sub4entry.grid(row=4,column=0,sticky="NW",padx=275,pady=33)

#Subject 5 Label
sub5labfosi = ("Calibari",20)
sub5lab = tkinter.Label(thirdpage,text="Subject 5: ",font=sub5labfosi)
sub5lab.grid(row=5,column=0,sticky="W",padx=120,pady=20)

#Subject 5 Entry
sub5ent = tkinter.StringVar(thirdpage,value="")
sub5entry = tkinter.Entry(thirdpage,textvariable=sub5ent,width=45)
sub5entry.grid(row=5,column=0,sticky="NW",padx=275,pady=33)

#to page2 from page3
prevbu2 = tkinter.Button(thirdpage,text="back",command=prevpage2)
prevbu2.grid(row=6,column=0,sticky="W",pady=30)

#page3 announce
page3fosi = ("Calibari",10)
page3 = tkinter.Label(thirdpage, text = "|Page 3|",font=page3fosi)
page3.grid(row=6,column=0,sticky="N",pady=60)

#to page4 from page3
nextbu4 = tkinter.Button(thirdpage,text="next",command=nextpage4)
nextbu4.grid(row=6,column=0,sticky="E",pady=30)

#ending of page3





# begining of page 4

# Student Details Label
studetlabfosi = ("Calibari",30)
studetlab = tkinter.Label(fourthpage, text = "Provide Student Details\n---------------------------------",font=studetlabfosi)
studetlab.grid(row=0,column=0,sticky="N",padx=50,pady=50)

#Student Name Label
stunamelabfosi = ("Calibari",20)
stunamelab = tkinter.Label(fourthpage,text="Enter Name: ",font=stunamelabfosi)
stunamelab.grid(row=1,column=0,sticky="W",padx=120,pady=20)

#Student Name Entry
stunameent = tkinter.StringVar(fourthpage,value="")
stunameentry = tkinter.Entry(fourthpage,textvariable=stunameent,width=45)
stunameentry.grid(row=1,column=0,sticky="NW",padx=290,pady=33)


#Student Roll No Label
sturollnolabfosi = ("Calibari",20)
sturollnolab = tkinter.Label(fourthpage,text="Enter Roll No: ",font=sturollnolabfosi)
sturollnolab.grid(row=2,column=0,sticky="W",padx=105,pady=20)

#Student Roll No Entry
sturollnoent = tkinter.StringVar(fourthpage,value="")
sturollnoentry = tkinter.Entry(fourthpage,textvariable=sturollnoent,width=45)
sturollnoentry.grid(row=2,column=0,sticky="NW",padx=290,pady=33)


#Student Reg. No Label
sturegnolabfosi = ("Calibari",20)
sturegnolab = tkinter.Label(fourthpage,text="Enter Reg. No: ",font=sturegnolabfosi)
sturegnolab.grid(row=3,column=0,sticky="W",padx=95,pady=20)

#Student Reg. No Entry
sturegnoent = tkinter.StringVar(fourthpage,value="")
sturegnoentry = tkinter.Entry(fourthpage,textvariable=sturegnoent,width=45)
sturegnoentry.grid(row=3,column=0,sticky="NW",padx=290,pady=33)

#to page3 form page4
prevbu3 = tkinter.Button(fourthpage,text="back",command=prevpage3)
prevbu3.grid(row=4,column=0,sticky="W",pady=30)

#page4 announce
page4fosi = ("Calibari",10)
page4 = tkinter.Label(fourthpage, text = "|Page 4|",font=page4fosi)
page4.grid(row=4,column=0,sticky="N",pady=60)

#to page5 from page4
nextbu5 = tkinter.Button(fourthpage,text="next",command=nextpage5)
nextbu5.grid(row=4,column=0,sticky="E",pady=30)

# ending of page 4




#beggining of page5

# Student Marks Details Label
provmarkslabfosi = ("Calibari",30)
provmarkslab = tkinter.Label(fifthpage, text = "Provide Marks for The 5 Subjects\n---------------------------------------------",font=provmarkslabfosi)
provmarkslab.grid(row=0,column=0,sticky="N",padx=50,pady=50)

#Subject 1 Marks Entry
sub1ment = tkinter.IntVar(fifthpage,value="")
sub1mentry = tkinter.Entry(fifthpage,textvariable=sub1ment,width=3)
sub1mentry.grid(row=1,column=0,sticky="E",pady=33)

#Subject 2 Marks Entry
sub2ment = tkinter.IntVar(fifthpage,value="")
sub2mentry = tkinter.Entry(fifthpage,textvariable=sub2ment,width=3)
sub2mentry.grid(row=2,column=0,sticky="E",pady=33)

#Subject 3 Marks Entry
sub3ment = tkinter.IntVar(fifthpage,value="")
sub3mentry = tkinter.Entry(fifthpage,textvariable=sub3ment,width=3)
sub3mentry.grid(row=3,column=0,sticky="E",pady=33)

#Subject 4 Marks Entry
sub4ment = tkinter.IntVar(fifthpage,value="")
sub4mentry = tkinter.Entry(fifthpage,textvariable=sub4ment,width=3)
sub4mentry.grid(row=4,column=0,sticky="E",pady=33)

#Subject 5 Marks Entry
sub5ment = tkinter.IntVar(fifthpage,value="")
sub5mentry = tkinter.Entry(fifthpage,textvariable=sub5ment,width=3)
sub5mentry.grid(row=5,column=0,sticky="E",pady=33)

#to page4 form page5
prevbu4 = tkinter.Button(fifthpage,text="back",command=prevpage4)
prevbu4.grid(row=6,column=0,sticky="W",pady=30)

#page5 announce
page5fosi = ("Calibari",10)
page5 = tkinter.Label(fifthpage, text = "|Page 5|",font=page5fosi)
page5.grid(row=6,column=0,sticky="N",pady=60)

# to page6 from page5
nextbu6 = tkinter.Button(fifthpage,text="next",command=nextpage6)
nextbu6.grid(row=6,column=0,sticky="E",pady=30)

# ending of page5





# begining of page6

# Create Marksheet Label
cretmslabfosi = ("Calibari",30)
cretmslab = tkinter.Label(sixthpage, text = "Generate Marksheet & Finish\n---------------------------------------------",font=cretmslabfosi)
cretmslab.grid(row=0,column=0,sticky="N",padx=50,pady=50)

# button to generate PDF File
cretpdfbu = tkinter.Button(sixthpage,text="Generate PDF File",command=genpdfms)
cretpdfbu.grid(row=1,column=0,sticky="N",pady=30)

# button to generate Word Document File
cretdocbu = tkinter.Button(sixthpage,text="Generate Word Document File")
cretdocbu.grid(row=2,column=0,sticky="N",pady=30)

# button to generate Text File
crettextbu = tkinter.Button(sixthpage,text="Generate Text File")
crettextbu.grid(row=3,column=0,sticky="N",pady=30)

#to page5 form page6
prevbu5 = tkinter.Button(sixthpage,text="back",command=prevpage5)
prevbu5.grid(row=4,column=0,sticky="W",pady=30)

#ending of page6

#Starting of the Software
tkinter.mainloop()