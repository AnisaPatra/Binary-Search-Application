import tkinter
from tkinter import *
import webbrowser

# Python Program for recursive binary search. 

# Returns index of x in arr if present, else -1
#arraay list of seats,starting point,len arry-1,element to find
def binarySearch (arr, l, r, x): 

	# Check base case 
	if r >= l: 

		mid = l + (r - l)/2
		a=int(mid)

		# If element is present at the middle itself 
		if arr[a] == x:
			return a 
		
		# If element is smaller than mid, then it 
		# can only be present in left subarray 
		elif arr[a] > x: 
			return binarySearch(arr, l, a-1, x)             #using recursion 

		# Else the element can only be present 
		# in right subarray 
		else: 
			return binarySearch(arr, a + 1, r, x)           #using recursion

	else: 
		# Element is not present in the array 
		return -1
# Test array
#all movie names 

a="lukka chuppi"
#users can enter movie in any form therefore used different string methods
b=a.capitalize()                        #capitalize form i.e. Lukka chuppi
c=a.upper()                             #upper form i.e. LUKKA CHUPPI
d=a.title()                             #title form i.e. Lukka Chuppi

e="gully boy"
f=e.capitalize()
g=e.upper()
h=e.title()

i="sonchirya"
j=i.capitalize()
k=i.upper()
l=i.title()

m="uri"
n=m.capitalize()
o=m.upper()
p=m.title()

q="total dhammal"
r=q.capitalize()
s=q.upper()
t=q.title()

#list including all available movies

arr = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]

#sorting the list so that we can perform binary search on it
arr.sort() 
    
w=tkinter.Tk()
w.title("")
w.config(bg="black")
w.geometry("1350x760")
w.iconbitmap(r'favicon.ico')
logo=Label(w,text="  PVR CINEMAS ",font="algerian 20 bold",bg="white",
           fg="red",relief="raised",borderwidth=15,highlightbackground="red",
           highlightthickness=10,anchor=CENTER)
logo.place(x=540,y=20)
label=Label(w,text="SEARCH  MOVIES",font="Helvetica 12",fg="azure",bg="black")
label.place(x=320,y=120)
movie_name=Entry(w,fg="black")
movie_name.place(x=500,y=120,width=400)
def search():
    name=movie_name.get()
    result = binarySearch(arr, 0, len(arr)-1, name)
    if result != -1:
        label_2=Label(w,text=(arr[result],"is available. For tickets click on BOOK NOW"),bg="black",fg="white")
        label_2.place(x=500,y=150)
    else:
        label_2=Label(w,text="Sorry there is no such movie available!!!",fg="white",bg="black")
        label_2.place(x=500,y=150)
        
search_bt=PhotoImage(file="search(2).png")
button=Button(w,image=search_bt,cursor="hand2",bg="black",anchor=CENTER,relief="flat",borderwidth=5,command=search)
button.place(x=900,y=115,width=50,height=30)

	    
reserved=["A1","B1","E3","E4","B2","D5","A5","A3","E1","E2","E5"]
reserved.sort()   


def seats_confirm():
        Msg=Tk()
        Msg.geometry('320x240')
        Msg.title('Booking Confirm')
        reserved=["A1","B1","E3","E4","B2","D5","A5","A3","E1","E2","E5"]
        n=e.get()
        result = binarySearch(reserved, 0, len(reserved)-1, n)
        if result != -1:
            nlabel1=Label(Msg,text=(reserved[result],"is not available"),fg="white",bg='black')
            nlabel1.place(x=70,y=100)
            b1=Button(Msg,text="Ok",font="Courier 15 bold",bg="blue",fg="red",command=Msg.destroy)
            b1.place(x=100,y=160)
        else:
            nlabel2=Label(Msg,text="Seat is available U can confirm this seat",fg="white",bg="black")
            nlabel2.place(x=70,y=100)
            b2=Button(Msg,text="Confirm Seats",font="Courier 15 bold",bg="blue",fg="red",command=Msg.destroy)
            b2.place(x=100,y=160)

    

    
def see_seats():
    top2=Toplevel()
    top2.config(bg="black")
    top2.title("see seats")
    label=Label(top2,text="Choose the seats you want: ",font="Helvetica 12",fg="white",bg="black")
    label.place(x=50,y=20)
    global e
    e=Entry(top2,fg="black")
    e.place(x=300,y=20,width=500)

    bu=Button(top2,text="SEARCH",cursor="hand2",anchor=CENTER,relief="flat",borderwidth=5,command=seats_confirm)
    bu.place(x=900,y=20,width=50,height=30)

    l1=Label(top2,text="A",fg="black",font="Times 10 bold",width=10,height=2)
    l1.place(x=50,y=100)
    #10 seats inn row A
    b1=Button(top2,text="1",fg="black")
    b1.place(x=200,y=100,width=50)
    b1=Button(top2,text="2",fg="black")
    b1.place(x=300,y=100,width=50)
    b1=Button(top2,text="3",fg="black")
    b1.place(x=400,y=100,width=50)
    b1=Button(top2,text="4",fg="black")
    b1.place(x=500,y=100,width=50)
    b1=Button(top2,text="5",fg="black")
    b1.place(x=600,y=100,width=50)
    b1=Button(top2,text="6",fg="black")
    b1.place(x=700,y=100,width=50)
    b1=Button(top2,text="7",fg="black")
    b1.place(x=800,y=100,width=50)
    b1=Button(top2,text="8",fg="black")
    b1.place(x=900,y=100,width=50)
    b1=Button(top2,text="9",fg="black")
    b1.place(x=1000,y=100,width=50)
    b1=Button(top2,text="10",fg="black")
    b1.place(x=1100,y=100,width=50)
    
    l2=Label(top2,text="B",fg="black",font="Times 10 bold",width=10,height=2)
    l2.place(x=50,y=200)
    #5 seats in row B
    b1=Button(top2,text="1",fg="black")
    b1.place(x=200,y=200,width=50)
    b1=Button(top2,text="2",fg="black")
    b1.place(x=300,y=200,width=50)
    b1=Button(top2,text="3",fg="black")
    b1.place(x=400,y=200,width=50)
    b1=Button(top2,text="4",fg="black")
    b1.place(x=500,y=200,width=50)
    b1=Button(top2,text="5",fg="black")
    b1.place(x=600,y=200,width=50)
    
    l3=Label(top2,text="C",fg="black",font="Times 10 bold",width=10,height=2)
    l3.place(x=50,y=300)
    #5 seats in row C
    b1=Button(top2,text="1",fg="black")
    b1.place(x=200,y=300,width=50)
    b1=Button(top2,text="2",fg="black")
    b1.place(x=300,y=300,width=50)
    b1=Button(top2,text="3",fg="black")
    b1.place(x=400,y=300,width=50)
    b1=Button(top2,text="4",fg="black")
    b1.place(x=500,y=300,width=50)
    b1=Button(top2,text="5",fg="black")
    b1.place(x=600,y=300,width=50)
    
    l4=Label(top2,text="D",fg="black",font="Times 10 bold",width=10,height=2)
    l4.place(x=50,y=400)
    #5 seats in row D
    b1=Button(top2,text="1",fg="black")
    b1.place(x=200,y=400,width=50)
    b1=Button(top2,text="2",fg="black")
    b1.place(x=300,y=400,width=50)
    b1=Button(top2,text="3",fg="black")
    b1.place(x=400,y=400,width=50)
    b1=Button(top2,text="4",fg="black")
    b1.place(x=500,y=400,width=50)
    b1=Button(top2,text="5",fg="black")
    b1.place(x=600,y=400,width=50)
    
    l5=Label(top2,text="E",fg="black",font="Times 10 bold",width=10,height=2)
    l5.place(x=50,y=500)
    #5 seats in row E
    b1=Button(top2,text="1",fg="black")
    b1.place(x=200,y=500,width=50)
    b1=Button(top2,text="2",fg="black")
    b1.place(x=300,y=500,width=50)
    b1=Button(top2,text="3",fg="black")
    b1.place(x=400,y=500,width=50)
    b1=Button(top2,text="4",fg="black")
    b1.place(x=500,y=500,width=50)
    b1=Button(top2,text="5",fg="black")
    b1.place(x=600,y=500,width=50)
    
    l6=Label(top2,text="F",fg="black",font="Times 10 bold",width=10,height=2)
    l6.place(x=50,y=600)
    #5 seats in row F
    b1=Button(top2,text="1",fg="black")
    b1.place(x=200,y=600,width=50)
    b1=Button(top2,text="2",fg="black")
    b1.place(x=300,y=600,width=50)
    b1=Button(top2,text="3",fg="black")
    b1.place(x=400,y=600,width=50)
    b1=Button(top2,text="4",fg="black")
    b1.place(x=500,y=600,width=50)
    b1=Button(top2,text="5",fg="black")
    b1.place(x=600,y=600,width=50)




    


def seats():
    top1=Toplevel()
    top1.title("seats")
    l1=Label(top1,text="HOW MANY SEATS",bg="black",fg="green",font="Times 20 bold")
    l1.place(x=0,y=0,width=1400,height=100)
    seat_photo=PhotoImage(file="chairs(2).png")
    l2=Label(top1,image=seat_photo)
    l2.place(x=580,y=180)
    b1=Button(top1,text="1",bg="blue",fg="white")
    b1.place(x=200,y=450,width=50)
    b1=Button(top1,text="2",bg="blue",fg="white")
    b1.place(x=300,y=450,width=50)
    b1=Button(top1,text="3",bg="blue",fg="white")
    b1.place(x=400,y=450,width=50)
    b1=Button(top1,text="4",bg="blue",fg="white")
    b1.place(x=500,y=450,width=50)
    b1=Button(top1,text="5",bg="blue",fg="white")
    b1.place(x=600,y=450,width=50)
    b1=Button(top1,text="6",bg="blue",fg="white")
    b1.place(x=700,y=450,width=50)
    b1=Button(top1,text="7",bg="blue",fg="white")
    b1.place(x=800,y=450,width=50)
    b1=Button(top1,text="8",bg="blue",fg="white")
    b1.place(x=900,y=450,width=50)
    b1=Button(top1,text="9",bg="blue",fg="white")
    b1.place(x=1000,y=450,width=50)
    b1=Button(top1,text="10",bg="blue",fg="white")
    b1.place(x=1100,y=450,width=50)
    l3=Label(top1,text="PREMIUM\nRS.130\nAVAILABLE",fg="red",font="Courier 15 bold",bg="white",relief="raised",borderwidth=10)
    l3.place(x=580,y=520)
    b2=Button(top1,text="Select Seats",font="Courier 15 bold",bg="blue",fg="white",command=see_seats)
    b2.place(x=560,y=650)
    top1.mainloop()
def gb():
    top=Toplevel()
    top.title("GULLY BOY")
    top.config(bg="black")
    n1=PhotoImage(file="gullyboy.png")
    l1=Label(top,image=n1,bg="white",relief="groove",borderwidth=5)
    l1.place(x=300,y=10,width=800,height=300)
    l3=Label(top,text="GULLY BOY",font="algerian 30 bold",bg="sea green",fg="gold2")
    l3.place(x=580,y=330)
    l4=Label(top,text="Show Timings",fg="white",bg="black",font= "Times 15 bold")
    l4.place(x=630,y=400)
    l5=Label(top,text="06-03-2019\nTODAY",fg="white",bg="black",font="Courier 15 bold")
    l5.place(x=630,y=450)
    b1=Button(top,text="08:55 AM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b1.place(x=150,y=530,width=100)
    b2=Button(top,text="12:00 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b2.place(x=450,y=530,width=100)
    top.mainloop()
def lc():
    top=Toplevel()
    top.title("LUKKA CHUPPI")
    top.config(bg="black")
    n2=PhotoImage(file="lukkachuppi.png")
    l2=Label(top,image=n2,bg="white",relief="groove",borderwidth=10)
    l2.place(x=300,y=10,width=800,height=300)
    l3=Label(top,text="LUKKA CHUPPI",font="algerian 30 bold",bg="sea green",fg="gold2")
    l3.place(x=550,y=330)
    l4=Label(top,text="Show Timings",fg="white",bg="black",font= "Times 15 bold")
    l4.place(x=630,y=400)
    l5=Label(top,text="06-03-2019\nTODAY",fg="white",bg="black",font="Courier 15 bold")
    l5.place(x=630,y=450)
    b1=Button(top,text="08:55 AM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b1.place(x=150,y=530,width=100)
    b2=Button(top,text="10:05 AM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b2.place(x=450,y=530,width=100)
    b3=Button(top,text="11:25 AM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b3.place(x=750,y=530,width=100)
    b4=Button(top,text="12:40 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b4.place(x=1050,y=530,width=100)
    b5=Button(top,text="01:55 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b5.place(x=150,y=580,width=100)
    b6=Button(top,text="02:30 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b6.place(x=450,y=580,width=100)
    b7=Button(top,text="05:50 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b7.place(x=750,y=580,width=100)
    b8=Button(top,text="08:25 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b8.place(x=1050,y=580,width=100)
    b9=Button(top,text="09:45 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b9.place(x=150,y=630,width=100)
    b10=Button(top,text="11:00 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b10.place(x=450,y=630,width=100)
    top.mainloop()
def sc():
    top=Toplevel()
    top.title("SONCHIRAYA")
    top.config(bg="black")
    n3=PhotoImage(file="s.png")
    l2=Label(top,image=n3,bg="white",relief="groove",borderwidth=5)
    l2.place(x=300,y=10,width=800,height=350)
    l3=Label(top,text="SONCHIRAYA",font="algerian 30 bold",bg="sea green",fg="gold2")
    l3.place(x=580,y=400)
    l4=Label(top,text="Show Timings",fg="white",bg="black",font= "Times 15 bold")
    l4.place(x=630,y=470)
    l5=Label(top,text="06-03-2019\nTODAY",fg="white",bg="black",font="Courier 15 bold")
    l5.place(x=630,y=500)
    b1=Button(top,text="11:00 AM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b1.place(x=150,y=580,width=100)
    top.mainloop()
def ur():
    top=Toplevel()
    top.title("URI")
    top.config(bg="black")
    n4=PhotoImage(file="u.png")
    l4=Label(top,image=n4,bg="white",relief="groove",borderwidth=5)
    l4.place(x=300,y=10,width=800,height=300)
    l3=Label(top,text="URI",font="algerian 30 bold",bg="sea green",fg="gold2")
    l3.place(x=530,y=330,width=300)
    l4=Label(top,text="Show Timings",fg="white",bg="black",font= "Times 15 bold")
    l4.place(x=630,y=400)
    l5=Label(top,text="06-03-2019\nTODAY",fg="white",bg="black",font="Courier 15 bold")
    l5.place(x=630,y=450)
    b1=Button(top,text="09:00 AM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b1.place(x=150,y=530,width=100)
    b2=Button(top,text="11:45 AM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b2.place(x=450,y=530,width=100)
    b3=Button(top,text="07:25 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b3.place(x=750,y=530,width=100)
    top.mainloop()
def td():
    top=Toplevel()
    top.title("TOTAL DHAMMAL")
    top.config(bg="black")
    n5=PhotoImage(file="total.png")
    l5=Label(top,image=n5,bg="white",relief="groove",borderwidth=5)
    l5.place(x=300,y=10,width=800,height=300)
    l3=Label(top,text="TOTAL DHAMMAL",font="algerian 30 bold",bg="sea green",fg="gold2")
    l3.place(x=550,y=330)
    l4=Label(top,text="Show Timings",fg="white",bg="black",font= "Times 15 bold")
    l4.place(x=630,y=400)
    l5=Label(top,text="06-03-2019\nTODAY",fg="white",bg="black",font="Courier 15 bold")
    l5.place(x=630,y=450)
    b1=Button(top,text="09:50 AM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b1.place(x=150,y=550,width=100)
    b2=Button(top,text="12:25 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b2.place(x=450,y=550,width=100)
    b3=Button(top,text="03:00 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b3.place(x=750,y=550,width=100)
    b4=Button(top,text="04:25 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b4.place(x=1050,y=550,width=100)
    b5=Button(top,text="07:15 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b5.place(x=150,y=650,width=100)
    b6=Button(top,text="10:45 PM",bg="white",fg="blue",relief="ridge",borderwidth=5,command=seats)
    b6.place(x=450,y=650,width=100)
    top.mainloop()

lukka_chuppi=PhotoImage(file="lc.png")
f=Label(w,image=lukka_chuppi,bg="white",cursor="hand2",relief="groove",borderwidth=5)
f.place(x=30,y=190,width=218,height=316)
sonchirya=PhotoImage(file="sonchirya.png")
f=Label(w,image=sonchirya,bg="white",cursor="hand2",relief="groove",borderwidth=5)
f.place(x=300,y=190,width=218,height=316)
total_dhammal=PhotoImage(file="td.png")
f=Label(w,image=total_dhammal,bg="white",cursor="hand2",relief="groove",borderwidth=5)
f.place(x=570,y=190,width=218,height=310)
gully_boy=PhotoImage(file="gb.png")
f=Label(w,image=gully_boy,bg="white",cursor="hand2",relief="groove",borderwidth=5)
f.place(x=840,y=190,width=218,height=316)
uri=PhotoImage(file="uri.png")
f=Label(w,image=uri,bg="white",cursor="hand2",relief="groove",borderwidth=5)
f.place(x=1110,y=190,width=218,height=316)
button=Button(w,text="BOOK NOW",font="Courier 13 bold",bg="red",fg="white",cursor="hand1",anchor=CENTER,relief="sunken",borderwidth=5,command=lc)
button.place(x=80,y=525,width=100,height=40)
button=Button(w,text="BOOK NOW",font="Courier 13 bold",bg="red",fg="white",cursor="hand1",anchor=CENTER,relief="sunken",borderwidth=5,command=sc)
button.place(x=360,y=525,width=100,height=40)
button=Button(w,text="BOOK NOW",font="Courier 13 bold",bg="red",fg="white",cursor="hand1",anchor=CENTER,relief="sunken",borderwidth=5,command=td)
button.place(x=630,y=525,width=100,height=40)
button=Button(w,text="BOOK NOW",font="Courier 13 bold",bg="red",fg="white",cursor="hand1",anchor=CENTER,relief="sunken",borderwidth=5,command=gb)
button.place(x=900,y=525,width=100,height=40)
button=Button(w,text="BOOK NOW",font="Courier 13 bold",bg="red",fg="white",cursor="hand1",anchor=CENTER,relief="sunken",borderwidth=5,command=ur)
button.place(x=1170,y=525,width=100,height=40)
button=Button(w,text="QUIT",font="Times 15 bold",bg="purple",fg="white",cursor="hand2",anchor=CENTER,command=w.destroy,relief="ridge",borderwidth=8)
button.place(x=630,y=600,width=100,height=60)
mainloop()


