import  tkinter as tk
root=tk.Tk()

root.geometry("2000x900")
root.title("my application")
root.config(bg='light green')

m1=tk.Label(root,text="welcome to my new application",font=("Algerian",20,"bold"))
m1.place(x=420,y=50)

m2=tk.Label(root,text="LOGIN PAGE",font=("Algerian",10))
m2.place(x=600,y=100)

m3=tk.Label(root,text="USER NAME",font=("Algerian",10))
m3.place(x=500,y=200)

e1=tk.Entry(root,font=("arial",16))
e1.place(x=650,y=200)

m1=tk.Label(root,text="PASSWORD",font=("arial",10))
m1.place(x=500,y=300)

e2=tk.Entry(root,font=("arial",16))
e2.place(x=650,y=300)

b1=tk.Button(root,text="LOGIN",font=("arial",10))
b1.place(x=500,y=400)

b2=tk.Button(root,text="SIGN UP",font=("arial",10))
b2.place(x=600,y=400)

b3=tk.Button(root,text="CLOSE",font=("arial",10))
b3.place(x=700,y=400)

root.mainloop()
