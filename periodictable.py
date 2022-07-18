#-----------MODULES-------------------
from tkinter import *
from PIL import ImageTk, Image
#-----------=-------------------------


root=Tk()                                                   #root Window
root.configure(background='')
root.title('The Modern Periodic Table')
def press(txt):                                             #function to gather user input
    f=open("Data\\"+txt+".txt",'r')                         #datafile for element
    frame = Tk()                                            #Details window
    frame.title(txt)
    frame.geometry('1366x768')
    frame.config(bg='white')
    #---------SCROLLBAR-----------------
    w=Scrollbar(frame)
    w.pack(side=RIGHT,fill=BOTH)
    close = Button(frame, text = "FIND NEXT", command=frame.destroy,bg='red',fg='yellow')
    close.pack(side=BOTTOM,fill=NONE)
    close.config(font=('helvetica',15,'bold'))
    mylist = Listbox(frame, yscrollcommand = w.set )
    for i in f.readlines():                                 #fetching .txt file data
        mylist.insert(END, i)
    mylist.pack( expand=1,side = BOTTOM, fill = BOTH )
    w.config( command = mylist.yview )
    
#----------------------------------Legend--------------------------------------------------
img = ImageTk.PhotoImage(Image.open('Data\\lgnd.png'))      
panel = Label(root, image = img)
panel.grid(row=1,column=4,rowspan=5,columnspan=9)

#----------------------------------Title---------------------------------------------------
titl = Label(root, text='THE MODERN PERIODIC TABLE')
titl.grid(row=0,column=0,columnspan=20)
titl.config(font=('elephant',20,'underline'),bg='white')

#----------------------------------Groups--------------------------------------------------
groups=Label(root,text='1                   2               3               4               5               6               \
7               8               9               10               \
11               12               13               14               15               16               17               18')
groups.grid(row=1,column=1,columnspan=25,sticky=N)
groups.config(font=('helvetica',10,'bold'),bg='white')

#----------------------------------Preiods-------------------------------------------------
periods=Label(root,text='Groups ►\n\n Periods ▼')
periods.grid(row=1,column=0,sticky=S)
periods.config(font=('helvetica',10,'bold'),bg='white')

p1=Label(root,text='1')
p1.grid(row=3,column=0)
p1.config(font=('helvetica',10,'bold'),bg='white')

p2=Label(root,text='2')
p2.grid(row=4,column=0)
p2.config(font=('helvetica',10,'bold'),bg='white')

p3=Label(root,text='3')
p3.grid(row=5,column=0)
p3.config(font=('helvetica',10,'bold'),bg='white')

p4=Label(root,text='4')
p4.grid(row=6,column=0)
p4.config(font=('helvetica',10,'bold'),bg='white')

p5=Label(root,text='5')
p5.grid(row=7,column=0)
p5.config(font=('helvetica',10,'bold'),bg='white')

p6=Label(root,text='6')
p6.grid(row=8,column=0)
p6.config(font=('helvetica',10,'bold'),bg='white')

p7=Label(root,text='7')
p7.grid(row=9,column=0)
p7.config(font=('helvetica',10,'bold'),bg='white')
    
#====================================Group-1===============================================
l1=Label(root,text='s-block Elements')
l1.grid(row=2,column=1,columnspan=2)
l1.config(font=('arial', 12, 'bold'),bg='white')

h=Button(root,text='H',height=2,width=5,command=lambda:press('H'),fg='green3',bg='gold')
h.grid(row=3,column=0+1)
h.config(font=('helvetica', 15, 'bold'))
li=Button(root,text='Li',height=2,width=5,command=lambda:press('Li'),bg='SkyBlue1')
li.grid(row=4,column=0+1)
li.config(font=('helvetica', 15, 'bold'))
na=Button(root,text='Na',height=2,width=5,command=lambda:press('Na'),bg='SkyBlue1')
na.grid(row=5,column=0+1)
na.config(font=('helvetica', 15, 'bold'))
k=Button(root,text='K',height=2,width=5,command=lambda:press('K'),bg='SkyBlue1')
k.grid(row=6,column=0+1)
k.config(font=('helvetica', 15, 'bold'))
rb=Button(root,text='Rb',height=2,width=5,command=lambda:press('Rb'),bg='SkyBlue1')
rb.grid(row=7,column=0+1)
rb.config(font=('helvetica', 15, 'bold'))
cs=Button(root,text='Cs',height=2,width=5,command=lambda:press('Cs'),bg='SkyBlue1')
cs.grid(row=8,column=0+1)
cs.config(font=('helvetica', 15, 'bold'))
fr=Button(root,text='Fr',height=2,width=5,command=lambda:press('Fr'),bg='SkyBlue1')
fr.grid(row=9,column=0+1)
fr.config(font=('helvetica', 15, 'bold'))

#===================================Group-2================================================

be=Button(root,text='Be',height=2,width=5,command=lambda:press('Be'),bg='tomato')
be.grid(row=4,column=1+1)
be.config(font=('helvetica', 15, 'bold'))
mg=Button(root,text='Mg',height=2,width=5,command=lambda:press('Mg'),bg='tomato')
mg.grid(row=5,column=1+1)
mg.config(font=('helvetica', 15, 'bold'))
ca=Button(root,text='Ca',height=2,width=5,command=lambda:press('Ca'),bg='tomato')
ca.grid(row=6,column=1+1)
ca.config(font=('helvetica', 15, 'bold'))
sr=Button(root,text='Sr',height=2,width=5,command=lambda:press('Sr'),bg='tomato')
sr.grid(row=7,column=1+1)
sr.config(font=('helvetica', 15, 'bold'))
ba=Button(root,text='Ba',height=2,width=5,command=lambda:press('Ba'),bg='tomato')
ba.grid(row=8,column=1+1)
ba.config(font=('helvetica', 15, 'bold'))
ra=Button(root,text='Ra',height=2,width=5,command=lambda:press('Ra'),bg='tomato')
ra.grid(row=9,column=1+1)
ra.config(font=('helvetica', 15, 'bold'))

#===================================Group-3===============================================

sc=Button(root,text='Sc',height=2,width=5,command=lambda:press('Sc'),bg='DarkOliveGreen2')
sc.grid(row=6,column=2+1)
sc.config(font=('helvetica', 15, 'bold'))
y=Button(root,text='Y',height=2,width=5,command=lambda:press('Y'),bg='DarkOliveGreen2')
y.grid(row=7,column=2+1)
y.config(font=('helvetica', 15, 'bold'))
lalu=Button(root,text='La',height=2,width=5,command=lambda:press('La'),bg='DarkOliveGreen2')
lalu.grid(row=8,column=2+1)
lalu.config(font=('helvetica', 15, 'bold'))
aclr=Button(root,text='Ac',height=2,width=5,command=lambda:press('Ac'),bg='DarkOliveGreen2')
aclr.grid(row=9,column=2+1)
aclr.config(font=('helvetica', 15, 'bold'))

#===================================Group-4===============================================

ti=Button(root,text='Ti',height=2,width=5,command=lambda:press('Ti'),bg='DarkOliveGreen2')
ti.grid(row=6,column=3+1)
ti.config(font=('helvetica', 15, 'bold'))
zr=Button(root,text='Zr',height=2,width=5,command=lambda:press('Zr'),bg='DarkOliveGreen2')
zr.grid(row=7,column=3+1)
zr.config(font=('helvetica', 15, 'bold'))
hf=Button(root,text='Hf',height=2,width=5,command=lambda:press('Hf'),bg='DarkOliveGreen2')
hf.grid(row=8,column=3+1)
hf.config(font=('helvetica', 15, 'bold'))
rf=Button(root,text='Rf',height=2,width=5,command=lambda:press('Rf'),bg='DarkOliveGreen2',fg='blue2')
rf.grid(row=9,column=3+1)
rf.config(font=('helvetica', 15, 'bold'))

#===================================Group-5===============================================

v=Button(root,text='V',height=2,width=5,command=lambda:press('V'),bg='DarkOliveGreen2')
v.grid(row=6,column=4+1)
v.config(font=('helvetica', 15, 'bold'))
nb=Button(root,text='Nb',height=2,width=5,command=lambda:press('Nb'),bg='DarkOliveGreen2')
nb.grid(row=7,column=4+1)
nb.config(font=('helvetica', 15, 'bold'))
ta=Button(root,text='Ta',height=2,width=5,command=lambda:press('Ta'),bg='DarkOliveGreen2')
ta.grid(row=8,column=4+1)
ta.config(font=('helvetica', 15, 'bold'))
db=Button(root,text='Db',height=2,width=5,command=lambda:press('Db'),bg='DarkOliveGreen2',fg='blue2')
db.grid(row=9,column=4+1)
db.config(font=('helvetica', 15, 'bold'))

#===================================Group-6===============================================

cr=Button(root,text='Cr',height=2,width=5,command=lambda:press('Cr'),bg='DarkOliveGreen2')
cr.grid(row=6,column=5+1)
cr.config(font=('helvetica', 15, 'bold'))
mo=Button(root,text='Mo',height=2,width=5,command=lambda:press('Mo'),bg='DarkOliveGreen2')
mo.grid(row=7,column=5+1)
mo.config(font=('helvetica', 15, 'bold'))
w=Button(root,text='W',height=2,width=5,command=lambda:press('W'),bg='DarkOliveGreen2')
w.grid(row=8,column=5+1)
w.config(font=('helvetica', 15, 'bold'))
sg=Button(root,text='Sg',height=2,width=5,command=lambda:press('Sg'),bg='DarkOliveGreen2',fg='blue2')
sg.grid(row=9,column=5+1)
sg.config(font=('helvetica', 15, 'bold'))

#===================================Group-7===============================================
l1=Label(root,text='-------------------------------------------------d-block Elements-------------------------------------------------')
l1.grid(row=5,column=3,columnspan=10)
l1.config(font=('arial', 12, 'bold'),bg='white')

mn=Button(root,text='Mn',height=2,width=5,command=lambda:press('Mn'),bg='DarkOliveGreen2')
mn.grid(row=6,column=6+1)
mn.config(font=('helvetica', 15, 'bold'))
tc=Button(root,text='Tc',height=2,width=5,command=lambda:press('Tc'),bg='DarkOliveGreen2',fg='blue2')
tc.grid(row=7,column=6+1)
tc.config(font=('helvetica', 15, 'bold'))
re=Button(root,text='Re',height=2,width=5,command=lambda:press('Re'),bg='DarkOliveGreen2')
re.grid(row=8,column=6+1)
re.config(font=('helvetica', 15, 'bold'))
bh=Button(root,text='Bh',height=2,width=5,command=lambda:press('Bh'),bg='DarkOliveGreen2',fg='blue2')
bh.grid(row=9,column=6+1)
bh.config(font=('helvetica', 15, 'bold'))

#===================================Group-8===============================================

fe=Button(root,text='Fe',height=2,width=5,command=lambda:press('Fe'),bg='DarkOliveGreen2')
fe.grid(row=6,column=7+1)
fe.config(font=('helvetica', 15, 'bold'))
ru=Button(root,text='Ru',height=2,width=5,command=lambda:press('Ru'),bg='DarkOliveGreen2')
ru.grid(row=7,column=7+1)
ru.config(font=('helvetica', 15, 'bold'))
os=Button(root,text='Os',height=2,width=5,command=lambda:press('Os'),bg='DarkOliveGreen2')
os.grid(row=8,column=7+1)
os.config(font=('helvetica', 15, 'bold'))
hs=Button(root,text='Hs',height=2,width=5,command=lambda:press('Hs'),bg='DarkOliveGreen2',fg='blue2')
hs.grid(row=9,column=7+1)
hs.config(font=('helvetica', 15, 'bold'))

#===================================Group-9===============================================

co=Button(root,text='Co',height=2,width=5,command=lambda:press('Co'),bg='DarkOliveGreen2')
co.grid(row=6,column=8+1)
co.config(font=('helvetica', 15, 'bold'))
rh=Button(root,text='Rh',height=2,width=5,command=lambda:press('Rh'),bg='DarkOliveGreen2')
rh.grid(row=7,column=8+1)
rh.config(font=('helvetica', 15, 'bold'))
ir=Button(root,text='Ir',height=2,width=5,command=lambda:press('Ir'),bg='DarkOliveGreen2')
ir.grid(row=8,column=8+1)
ir.config(font=('helvetica', 15, 'bold'))
mt=Button(root,text='Mt',height=2,width=5,command=lambda:press('Mt'),bg='DarkOliveGreen2',fg='blue2')
mt.grid(row=9,column=8+1)
mt.config(font=('helvetica', 15, 'bold'))

#===================================Group-10===============================================

ni=Button(root,text='Ni',height=2,width=5,command=lambda:press('Ni'),bg='DarkOliveGreen2')
ni.grid(row=6,column=9+1)
ni.config(font=('helvetica', 15, 'bold'))
pd=Button(root,text='Pd',height=2,width=5,command=lambda:press('Pd'),bg='DarkOliveGreen2')
pd.grid(row=7,column=9+1)
pd.config(font=('helvetica', 15, 'bold'))
pt=Button(root,text='Pt',height=2,width=5,command=lambda:press('Pt'),bg='DarkOliveGreen2')
pt.grid(row=8,column=9+1)
pt.config(font=('helvetica', 15, 'bold'))
ds=Button(root,text='Ds',height=2,width=5,command=lambda:press('Ds'),bg='DarkOliveGreen2',fg='blue2')
ds.grid(row=9,column=9+1)
ds.config(font=('helvetica', 15, 'bold'))

#===================================Group-11===============================================

cu=Button(root,text='Cu',height=2,width=5,command=lambda:press('Cu'),bg='DarkOliveGreen2')
cu.grid(row=6,column=10+1)
cu.config(font=('helvetica', 15, 'bold'))
ag=Button(root,text='Ag',height=2,width=5,command=lambda:press('Ag'),bg='DarkOliveGreen2')
ag.grid(row=7,column=10+1)
ag.config(font=('helvetica', 15, 'bold'))
au=Button(root,text='Au',height=2,width=5,command=lambda:press('Au'),bg='DarkOliveGreen2')
au.grid(row=8,column=10+1)
au.config(font=('helvetica', 15, 'bold'))
rg=Button(root,text='Rg',height=2,width=5,command=lambda:press('Rg'),bg='DarkOliveGreen2',fg='blue2')
rg.grid(row=9,column=10+1)
rg.config(font=('helvetica', 15, 'bold'))

#===================================Group-12===============================================

zn=Button(root,text='Zn',height=2,width=5,command=lambda:press('Zn'),bg='DarkOliveGreen2')
zn.grid(row=6,column=11+1)
zn.config(font=('helvetica', 15, 'bold'))
cd=Button(root,text='Cd',height=2,width=5,command=lambda:press('Cd'),bg='DarkOliveGreen2')
cd.grid(row=7,column=11+1)
cd.config(font=('helvetica', 15, 'bold'))
hg=Button(root,text='Hg',height=2,width=5,command=lambda:press('Hg'),bg='DarkOliveGreen2')
hg.grid(row=8,column=11+1)
hg.config(font=('helvetica', 15, 'bold'))
cn=Button(root,text='Cn',height=2,width=5,command=lambda:press('Cn'),bg='DarkOliveGreen2',fg='blue2')
cn.grid(row=9,column=11+1)
cn.config(font=('helvetica', 15, 'bold'))

#===================================Group-13================================================

l1=Label(root,text='-----------------------p-block Elements-----------------------')
l1.grid(row=2,column=13,columnspan=7)
l1.config(font=('arial', 12, 'bold'),bg='white')


b=Button(root,text='B',height=2,width=5,command=lambda:press('B'),fg='Black',bg='VioletRed2')
b.grid(row=4,column=13)
b.config(font=('helvetica', 15, 'bold'))
al=Button(root,text='Al',height=2,width=5,command=lambda:press('Al'),fg='Black',bg='lightgoldenrod2')
al.grid(row=5,column=13)
al.config(font=('helvetica', 15, 'bold'))
ga=Button(root,text='Ga',height=2,width=5,command=lambda:press('Ga'),fg='Black',bg='lightgoldenrod2')
ga.grid(row=6,column=13)
ga.config(font=('helvetica', 15, 'bold'))
In=Button(root,text='In',height=2,width=5,command=lambda:press('In'),fg='Black',bg='lightgoldenrod2')
In.grid(row=7,column=13)
In.config(font=('helvetica', 15, 'bold'))
tl=Button(root,text='Tl',height=2,width=5,command=lambda:press('Tl'),fg='Black',bg='lightgoldenrod2')
tl.grid(row=8,column=13)
tl.config(font=('helvetica', 15, 'bold'))
nh=Button(root,text='Nh',height=2,width=5,command=lambda:press('Nh'),fg='blue2',bg='DarkOliveGreen2')
nh.grid(row=9,column=13)
nh.config(font=('helvetica', 15, 'bold'))

#===================================Group-14================================================
c=Button(root,text='C',height=2,width=5,command=lambda:press('C'),fg='Black',bg='VioletRed2')
c.grid(row=4,column=14)
c.config(font=('helvetica', 15, 'bold'))
si=Button(root,text='Si',height=2,width=5,command=lambda:press('Si'),fg='Black',bg='VioletRed2')
si.grid(row=5,column=14)
si.config(font=('helvetica', 15, 'bold'))
ge=Button(root,text='Ge',height=2,width=5,command=lambda:press('Ge'),fg='Black',bg='lightgoldenrod2')
ge.grid(row=6,column=14)
ge.config(font=('helvetica', 15, 'bold'))
sn=Button(root,text='Sn',height=2,width=5,command=lambda:press('Sn'),fg='Black',bg='lightgoldenrod2')
sn.grid(row=7,column=14)
sn.config(font=('helvetica', 15, 'bold'))
pb=Button(root,text='Pb',height=2,width=5,command=lambda:press('Pb'),fg='Black',bg='lightgoldenrod2')
pb.grid(row=8,column=14)
pb.config(font=('helvetica', 15, 'bold'))
fl=Button(root,text='Fl',height=2,width=5,command=lambda:press('Fl'),fg='blue2',bg='DarkOliveGreen2')
fl.grid(row=9,column=14)
fl.config(font=('helvetica', 15, 'bold'))

#===================================Group-15================================================
n=Button(root,text='N',height=2,width=5,command=lambda:press('N'),fg='green3',bg='VioletRed2')
n.grid(row=4,column=15)
n.config(font=('helvetica', 15, 'bold'))
p=Button(root,text='P',height=2,width=5,command=lambda:press('P'),fg='Black',bg='VioletRed2')
p.grid(row=5,column=15)
p.config(font=('helvetica', 15, 'bold'))
As=Button(root,text='As',height=2,width=5,command=lambda:press('As'),fg='Black',bg='VioletRed2')
As.grid(row=6,column=15)
As.config(font=('helvetica', 15, 'bold'))
sb=Button(root,text='Sb',height=2,width=5,command=lambda:press('Sb'),fg='Black',bg='lightgoldenrod2')
sb.grid(row=7,column=15)
sb.config(font=('helvetica', 15, 'bold'))
bi=ButtoMc=Button(root,text='Bi',height=2,width=5,command=lambda:press('Bi'),fg='Black',bg='lightgoldenrod2')
bi.grid(row=8,column=15)
bi.config(font=('helvetica', 15, 'bold'))
mc=Button(root,text='Mc',height=2,width=5,command=lambda:press('Mc'),fg='blue2',bg='DarkOliveGreen2')
mc.grid(row=9,column=15)
mc.config(font=('helvetica', 15, 'bold'))

#===================================Group-16================================================
o=Button(root,text='O',height=2,width=5,command=lambda:press('O'),fg='green3',bg='VioletRed2')
o.grid(row=4,column=16)
o.config(font=('helvetica', 15, 'bold'))
s=Button(root,text='S',height=2,width=5,command=lambda:press('S'),fg='Black',bg='VioletRed2')
s.grid(row=5,column=16)
s.config(font=('helvetica', 15, 'bold'))
se=Button(root,text='Se',height=2,width=5,command=lambda:press('Se'),fg='Black',bg='VioletRed2')
se.grid(row=6,column=16)
se.config(font=('helvetica', 15, 'bold'))
te=Button(root,text='Te',height=2,width=5,command=lambda:press('Te'),fg='Black',bg='VioletRed2')
te.grid(row=7,column=16)
te.config(font=('helvetica', 15, 'bold'))
po=Button(root,text='Po',height=2,width=5,command=lambda:press('Po'),fg='Black',bg='lightgoldenrod2')
po.grid(row=8,column=16)
po.config(font=('helvetica', 15, 'bold'))
lv=Button(root,text='Lv',height=2,width=5,command=lambda:press('Lv'),fg='blue2',bg='DarkOliveGreen2')
lv.grid(row=9,column=16)
lv.config(font=('helvetica', 15, 'bold'))

#===================================Group-17================================================
f=Button(root,text='F',height=2,width=5,command=lambda:press('F'),fg='green3',bg='VioletRed2')
f.grid(row=4,column=17)
f.config(font=('helvetica', 15, 'bold'))
cl=Button(root,text='Cl',height=2,width=5,command=lambda:press('Cl'),fg='green3',bg='VioletRed2')
cl.grid(row=5,column=17)
cl.config(font=('helvetica', 15, 'bold'))
br=Button(root,text='Br',height=2,width=5,command=lambda:press('Br'),fg='DodgerBlue3',bg='VioletRed2')
br.grid(row=6,column=17)
br.config(font=('helvetica', 15, 'bold'))
i=Button(root,text='I',height=2,width=5,command=lambda:press('I'),fg='Black',bg='VioletRed2')
i.grid(row=7,column=17)
i.config(font=('helvetica', 15, 'bold'))
at=Button(root,text='At',height=2,width=5,command=lambda:press('At'),fg='black',bg='VioletRed2')
at.grid(row=8,column=17)
at.config(font=('helvetica', 15, 'bold'))
ts=Button(root,text='Ts',height=2,width=5,command=lambda:press('Ts'),fg='blue2',bg='DarkOliveGreen2')
ts.grid(row=9,column=17)
ts.config(font=('helvetica', 15, 'bold'))

#====================================Group-18===============================================
he=Button(root,text='He',height=2,width=5,command=lambda:press('He'),fg='green3',bg='honeydew4')
he.grid(row=3,column=18)
he.config(font=('helvetica', 15, 'bold'))
ne=Button(root,text='Ne',height=2,width=5,command=lambda:press('Ne'),fg='green3',bg='honeydew4')
ne.grid(row=4,column=18)
ne.config(font=('helvetica', 15, 'bold'))
ar=Button(root,text='Ar',height=2,width=5,command=lambda:press('Ar'),fg='green3',bg='honeydew4')
ar.grid(row=5,column=18)
ar.config(font=('helvetica', 15, 'bold'))
kr=Button(root,text='Kr',height=2,width=5,command=lambda:press('Kr'),fg='green3',bg='honeydew4')
kr.grid(row=6,column=18)
kr.config(font=('helvetica', 15, 'bold'))
xe=Button(root,text='Xe',height=2,width=5,command=lambda:press('Xe'),fg='green3',bg='honeydew4')
xe.grid(row=7,column=18)
xe.config(font=('helvetica', 15, 'bold'))
rn=Button(root,text='Rn',height=2,width=5,command=lambda:press('Rn'),fg='green3',bg='honeydew4')
rn.grid(row=8,column=18)
rn.config(font=('helvetica', 15, 'bold'))
og=Button(root,text='Og',height=2,width=5,command=lambda:press('Og'),fg='blue2',bg='DarkOliveGreen2')
og.grid(row=9,column=18)
og.config(font=('helvetica', 15, 'bold'))


#===================================Lanthanides===============================================

l1=Label(root,text='-------------------------------------------------INNER TRANSITION ELEMENTS (f-block Elements)------------------------------------------------')
l1.grid(row=10,column=5,columnspan=16,ipady=10)
l1.config(font=('arial', 12, 'bold'),bg='white')


ce=Button(root,text='Ce',height=2,width=5,command=lambda:press('Ce'),bg='medium purple')
ce.grid(row=11,column=5)
ce.config(font=('helvetica', 15, 'bold'))

pr=Button(root,text='Pr',height=2,width=5,command=lambda:press('Pr'),bg='medium purple')
pr.grid(row=11,column=6)
pr.config(font=('helvetica', 15, 'bold'))

nd=Button(root,text='Nd',height=2,width=5,command=lambda:press('Nd'),bg='medium purple')
nd.grid(row=11,column=7)
nd.config(font=('helvetica', 15, 'bold'))

pm=Button(root,text='Pm',height=2,width=5,command=lambda:press('Pm'),bg='medium purple',fg='blue2')
pm.grid(row=11,column=8)
pm.config(font=('helvetica', 15, 'bold'))

sm=Button(root,text='Sm',height=2,width=5,command=lambda:press('Sm'),bg='medium purple')
sm.grid(row=11,column=9)
sm.config(font=('helvetica', 15, 'bold'))

eu=Button(root,text='Eu',height=2,width=5,command=lambda:press('Eu'),bg='medium purple')
eu.grid(row=11,column=10)
eu.config(font=('helvetica', 15, 'bold'))

gd=Button(root,text='Gd',height=2,width=5,command=lambda:press('Gd'),bg='medium purple')
gd.grid(row=11,column=11)
gd.config(font=('helvetica', 15, 'bold'))

tb=Button(root,text='Tb',height=2,width=5,command=lambda:press('Tb'),bg='medium purple')
tb.grid(row=11,column=12)
tb.config(font=('helvetica', 15, 'bold'))

dy=Button(root,text='Dy',height=2,width=5,command=lambda:press('Dy'),bg='medium purple')
dy.grid(row=11,column=13)
dy.config(font=('helvetica', 15, 'bold'))

ho=Button(root,text='Ho',height=2,width=5,command=lambda:press('Ho'),bg='medium purple')
ho.grid(row=11,column=14)
ho.config(font=('helvetica', 15, 'bold'))

er=Button(root,text='Er',height=2,width=5,command=lambda:press('Er'),bg='medium purple')
er.grid(row=11,column=15)
er.config(font=('helvetica', 15, 'bold'))

tm=Button(root,text='Tm',height=2,width=5,command=lambda:press('Tm'),bg='medium purple')
tm.grid(row=11,column=16)
tm.config(font=('helvetica', 15, 'bold'))

yb=Button(root,text='Yb',height=2,width=5,command=lambda:press('Yb'),bg='medium purple')
yb.grid(row=11,column=17)
yb.config(font=('helvetica', 15, 'bold'))

lu=Button(root,text='Lu',height=2,width=5,command=lambda:press('Lu'),bg='medium purple')
lu.grid(row=11,column=18)
lu.config(font=('helvetica', 15, 'bold'))

#===================================Actinides===============================================

th=Button(root,text='Th',height=2,width=5,command=lambda:press('Th'),bg='DarkSlateGray1')
th.grid(row=12,column=5)
th.config(font=('helvetica', 15, 'bold'))

pa=Button(root,text='Pa',height=2,width=5,command=lambda:press('Pa'),bg='DarkSlateGray1')
pa.grid(row=12,column=6)
pa.config(font=('helvetica', 15, 'bold'))

u=Button(root,text='U',height=2,width=5,command=lambda:press('U'),bg='DarkSlateGray1')
u.grid(row=12,column=7)
u.config(font=('helvetica', 15, 'bold'))

np=Button(root,text='Np',height=2,width=5,command=lambda:press('Np'),bg='DarkSlateGray1',fg='blue2')
np.grid(row=12,column=8)
np.config(font=('helvetica', 15, 'bold'))

pu=Button(root,text='Pu',height=2,width=5,command=lambda:press('Pu'),bg='DarkSlateGray1',fg='blue2')
pu.grid(row=12,column=9)
pu.config(font=('helvetica', 15, 'bold'))

am=Button(root,text='Am',height=2,width=5,command=lambda:press('Am'),bg='DarkSlateGray1',fg='blue2')
am.grid(row=12,column=10)
am.config(font=('helvetica', 15, 'bold'))

cm=Button(root,text='Cm',height=2,width=5,command=lambda:press('Cm'),bg='DarkSlateGray1',fg='blue2')
cm.grid(row=12,column=11)
cm.config(font=('helvetica', 15, 'bold'))

bk=Button(root,text='Bk',height=2,width=5,command=lambda:press('Bk'),bg='DarkSlateGray1',fg='blue2')
bk.grid(row=12,column=12)
bk.config(font=('helvetica', 15, 'bold'))

cf=Button(root,text='Cf',height=2,width=5,command=lambda:press('Cf'),bg='DarkSlateGray1',fg='blue2')
cf.grid(row=12,column=13)
cf.config(font=('helvetica', 15, 'bold'))

es=Button(root,text='Es',height=2,width=5,command=lambda:press('Es'),bg='DarkSlateGray1',fg='blue2')
es.grid(row=12,column=14)
es.config(font=('helvetica', 15, 'bold'))

fm=Button(root,text='Fm',height=2,width=5,command=lambda:press('Fm'),bg='DarkSlateGray1',fg='blue2')
fm.grid(row=12,column=15)
fm.config(font=('helvetica', 15, 'bold'))

md=Button(root,text='Md',height=2,width=5,command=lambda:press('Md'),bg='DarkSlateGray1',fg='blue2')
md.grid(row=12,column=16)
md.config(font=('helvetica', 15, 'bold'))

no=Button(root,text='No',height=2,width=5,command=lambda:press('No'),bg='DarkSlateGray1',fg='blue2')
no.grid(row=12,column=17)
no.config(font=('helvetica', 15, 'bold'))

lr=Button(root,text='Lr',height=2,width=5,command=lambda:press('Lr'),bg='DarkSlateGray1',fg='blue2')
lr.grid(row=12,column=18)
lr.config(font=('helvetica', 15, 'bold'))

#============================================================================================================
act=Label(root,text='               ACTINIDES ►')
act.grid(row=12,column=2,columnspan=3)
act.configure(font=('helvetica', 10, 'bold'),bg='white')

lan=Label(root,text='          LANTHANIDES ►')
lan.grid(row=11,column=2,columnspan=3)
lan.configure(font=('helvetica', 10, 'bold'),bg='white')

#=======================================Legends==============================================================

solid=Button(root,text='C',height=1,width=3)
solid.grid(row=10,column=1,pady=5)
solid.config(font=('elephant', 10, 'bold'))
slabel=Label(root,text='Solid')
slabel.grid(row=10,column=2,sticky=W)
slabel.config(font=('helvetica', 10, 'bold'),bg='white')

liquid=Button(root,text='Br',height=1,width=3,fg='DodgerBlue3')
liquid.grid(row=11,column=1)
liquid.config(font=('elephant', 10, 'bold'))
lqlabel=Label(root,text='Liquid',fg='DodgerBlue3')
lqlabel.grid(row=11,column=2,sticky=W)
lqlabel.config(font=('helvetica', 10, 'bold'),bg='white')

gas=Button(root,text='H',height=1,width=3,fg='green3')
gas.grid(row=12,column=1)
gas.config(font=('elephant', 10, 'bold'))
gaslabel=Label(root,text='Gas',fg='green3')
gaslabel.grid(row=12,column=2,sticky=W)
gaslabel.config(font=('helvetica', 10, 'bold'),bg='white')

syn=Button(root,text='Tc',height=1,width=3,fg='blue2')
syn.grid(row=13,column=1)
syn.config(font=('elephant', 10, 'bold'))
synlabel=Label(root,text='Synthetic',fg='blue2')
synlabel.grid(row=13,column=2,sticky=W)
synlabel.config(font=('helvetica', 10, 'bold'),bg='white')
#---------------------------------------------------------------------------------------------------

#----------------------EXIT SEQUENCES------------------------
quitb=Button(root,text='QUIT',fg='yellow',bg='red',height=1,width=5,command=root.destroy)
quitb.grid(row=13,column=0,sticky=S)
quitb.configure(font=('helvetica',15,'bold italic'))
mainloop()
