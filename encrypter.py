from tkinter import *
from PIL import ImageTk



def encrypter():
    global finalword
    key=user_entry.get()
    word=pass_entry.get()
    letterlist=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letterlist2=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    indexlist=[]
    for digit in key:
        indexlist.append(letterlist.index(digit)+1)
    letterlists=[]
  
    for letter in word:
        letterlists.append(letterlist.index(letter)+1)
    
    finallist=[]
    jay=0
    for i in range(len(letterlists)):
        
        finallist.append(letterlist2[(indexlist[jay])+(letterlists[i])-1+jay])
       
        jay+=1
        if jay>2:
            jay=0
        else:
            continue    
    finalword=""
    for a in range(len(finallist)):
        finalword+=finallist[a]


    print(finalword) 
    answer()
        


    

    

def Window():
    global user_entry
    global pass_entry
    global root5
    root5 = Tk()
    root5.title("Encryption")
    root5.geometry("800x400")
    root5.resizable(False, False)
    # key=input("Enter a 3 Digit Alphabetic Key : ")
    # word=input("Enter The Word to be encrypted : ")
    bg = ImageTk.PhotoImage(file = "D:\Coding\my stuff\CYBER CREW\DECODEX\Encryted.jpg") 
    Label(root5, image=bg).place(x=0, y=0, relwidth=1, relheight=1 )
    
    
   
    
    login_box=Frame(root5,bg="white")
    login_box.place(x=110,y=20,height=360,width=600)   
    # #42f5bf

    #bgg2 = ImageTk.PhotoImage(file="C:/Users/Deepanshu Singh/Desktop/CS_PROJECT/Shoezz.png")  # LOGO IMAGE
    #Label(root, image=bgg2).place(x=750, y=200)

    heading=Label(login_box,text="Cryptii",font=("Azonix",38,"bold"),fg="#bf0d04",bg="white").place(x=180,y=30)
    heading=Label(login_box,text="Enter your key and Word",font=("roboto",18,),fg="#bf0d04",bg="white").place(x=170,y=100)

    user_label=Label(login_box,text="3 Digit Key : ",font=("bebas",20),fg="black",bg="white").place(x=50,y=170)
    user_entry=Entry(login_box,font=("roboto,20"),fg="#3b3838",bg="#f7f7f7")
    user_entry.place(x=180,y=175,height=35,width=280)



    pass_label= Label(login_box,text="Word : ",font=("bebas",20),fg="black",bg="white").place(x=50,y=250)
    pass_entry=Entry(login_box,font=("roboto,20"),fg="#3b3838",bg="#f7f7f7")
    pass_entry.place(x=180,y=255,height=35,width=280)
    sign_up_button=Button(login_box,text="Encrypt",command=encrypter,font=("roboto",12),bg="red",fg="white",bd=0).place(x=270,y=310)

    



    root5.mainloop()

   

def Window2():
    root6.destroy()q
    global user_entry
    global pass_entry
    global root5
    root5 = Tk()
    root5.title("Encryption")
    root5.geometry("800x400")
    root5.resizable(False, False)
    # key=input("Enter a 3 Digit Alphabetic Key : ")
    # word=input("Enter The Word to be encrypted : ")
    bg = ImageTk.PhotoImage(file = "D:\Coding\my stuff\CYBER CREW\DECODEX\Encryted.jpg") 
    Label(root5, image=bg).place(x=0, y=0, relwidth=1, relheight=1 )
    
    
   
    
    login_box=Frame(root5,bg="white")
    login_box.place(x=110,y=20,height=360,width=600)   
    # #42f5bf

    #bgg2 = ImageTk.PhotoImage(file="C:/Users/Deepanshu Singh/Desktop/CS_PROJECT/Shoezz.png")  # LOGO IMAGE
    #Label(root, image=bgg2).place(x=750, y=200)

    heading=Label(login_box,text="Cryptii",font=("Azonix",38,"bold"),fg="#bf0d04",bg="white").place(x=180,y=30)
    heading=Label(login_box,text="Enter your key and Word",font=("roboto",18,),fg="#bf0d04",bg="white").place(x=170,y=100)

    user_label=Label(login_box,text="3 Digit Key : ",font=("bebas",20),fg="black",bg="white").place(x=50,y=170)
    user_entry=Entry(login_box,font=("roboto,20"),fg="#3b3838",bg="#f7f7f7")
    user_entry.place(x=180,y=175,height=35,width=280)



    pass_label= Label(login_box,text="Word : ",font=("bebas",20),fg="black",bg="white").place(x=50,y=250)
    pass_entry=Entry(login_box,font=("roboto,20"),fg="#3b3838",bg="#f7f7f7")
    pass_entry.place(x=180,y=255,height=35,width=280)
    sign_up_button=Button(login_box,text="Encrypt",command=encrypter,font=("roboto",12),bg="red",fg="white",bd=0).place(x=270,y=310)

    



    root5.mainloop()
def answer():

    global root6
    root5.destroy()
    root6 = Tk()
    root6.title("Encryption")
    root6.geometry("800x400")
    root6.resizable(False, False)
    # key=input("Enter a 3 Digit Alphabetic Key : ")
    # word=input("Enter The Word to be encrypted : ")
    bg = ImageTk.PhotoImage(file = "D:\Coding\my stuff\CYBER CREW\DECODEX\Encryted.jpg") 
    Label(root6, image=bg).place(x=0, y=0, relwidth=1, relheight=1 )
      
    login_box=Frame(root6,bg="white")
    login_box.place(x=110,y=20,height=360,width=600)   
    # #42f5bf

    #bgg2 = ImageTk.PhotoImage(file="C:/Users/Deepanshu Singh/Desktop/CS_PROJECT/Shoezz.png")  # LOGO IMAGE
    #Label(root, image=bgg2).place(x=750, y=200)

    heading=Label(login_box,text="Cryptii Answer",font=("Azonix",33,"bold"),fg="#bf0d04",bg="white").place(x=80,y=30)
    


    
    heading2=Label(login_box,text=finalword,font=("Bebas",35,"bold"),fg="#091fe6",bg="white").place(x=210,y=170)
    
    retry_button=Button(login_box,text="Retry",command=Window2,font=("roboto",12),bg="red",fg="white",bd=0).place(x=240,y=310)





    root6.mainloop()



if __name__ == "__main__":
    
    Window()



