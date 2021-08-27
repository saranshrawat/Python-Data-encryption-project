from tkinter import *

from tkinter import messagebox

from tkinter import filedialog

from cryptography.fernet import Fernet

class Display:

 def __init__(self):

  self.root =Tk()

  self.root.wm_title("ENCRYPTION")

  self.label1= Label(self.root,text="enter file path",padx=30,pady=9)

  self.label1.pack
  
  self.label2=Label(self.root,text="The Sole Purpose OF This Software is to Encrypt/Decrypt files for security purpose.")

  self.label2.pack()

  self.button1 = Button(master = self.root, text = 'Browse', width = 6,command=self.browse_file)

  self.button1.pack(padx=70,pady=10)

  self.entry=Entry(self.root,width=50)

  self.entry.pack()

  self.button2= Button(self.root,text="next",command=self.open_win)

  self.button2.config(state="disabled")

  self.button2.pack(padx=70,pady=30)

  self.label6=Label(self.root,text=".")

  self.label6.pack()

  self.root.geometry("450x300+250+200")

  self.root.mainloop()

 def browse_file(self):

  global fname

  fname = filedialog.askopenfilename(initialdir="/",title="select file",filetypes = ( ("All files", "*.*"),("Text files", "*.txt")))

  print (fname)

# getting a file name

  self.entry.insert(END,fname)

  if (len(fname)!=0):

   self.button2.config(state="active")

 def open_file(self):

  if self.vari.get()==2:

   global oname

   oname = filedialog.askopenfilename(initialdir="/",title="select file",filetypes = (("Text files", "*.key"), ("All files", "*.*")))

   print(oname)

  else:

   self.flag2+=1

   if self.flag2==1:

     messagebox.showwarning("warning","please do not choose this option for encryption")

     self.flag2=0

#GUI for 2nd window

 def open_win(self):

  global vari,var

  global flag,flag2,flag3

  self.flag=0
   
  self.flag2=0

  self.flag3=0

  self.sec_win= Toplevel()

  self.vari = IntVar()

  self.root.withdraw()

  self.sec_win.deiconify()

  self.sec_win.geometry("350x300+250+200")

  self.sec_win.title("Encryption key")

  self.label3=Label(self.sec_win,text="Please choose any one option ")

  self.label3.pack()
  
  self.r1=Radiobutton(self.sec_win,text="Encrypt",variable= self.vari,value=1)

  self.r1.pack()

  self.r2=Radiobutton(self.sec_win,text="decrypt",variable= self.vari,value=2)

  self.r2.pack()

  self.label3= Label(self.sec_win,text="Please enter the secret key only in case of decryption!!!")

  self.label3.pack(padx=10,pady=15)

  self.button4=Button(self.sec_win,text="open_key",command=self.open_file)

  self.button4.pack()

  self.button5=Button(self.sec_win,text="start",command=self.final)

  self.button5.pack(padx=10,pady=10)

  self.sec_win.protocol("WM_DELETE_WINDOW",self.on_closing)

 def on_closing(self):

  self.flag+=1

  if self.flag==1:

     if messagebox.askokcancel("Quit", "do you want to quit?"):

       self.sec_win.destroy()

       self.root.deiconify()
 
       self.entry.delete(0, END)

       self.button2.config(state="disabled")

  else: self.flag=0

 def generate_key(self):

  global kname

  global me

  global count

  try:

    count=0

    key = Fernet.generate_key()

    messagebox.showwarning("info","file please save your key!!!")

    kname = filedialog.asksaveasfile(mode='w', defaultextension='.key')

    print(kname)

    me=kname.name

    key_file=open(me,"wb")

    key_file.write(key)

    messagebox.showwarning("success","key generated and saved !!")

    count=1

  except:

    if kname=="None":

      self.sec_win.destroy()

      self.root.deiconify()

 def load_key(self):

  """

  Load the previously generated key

  """

  try:

    if self.vari.get()==1:

     return open(me,"rb").read()

    if self.vari.get()==2:

      self.button5.config(state="active")

      return open( oname,"rb").read()

  except:
  
    if kname=="None":

       self.sec_win.destroy()

       self.root.deiconify()

 def encrypt_file(self):

  """

  Encrypts a message

  """

  try:

     self.generate_key()

     print("en called")

     file=open(fname,"rb")

     msg=file.read()

     key = self.load_key()

     f = Fernet(key)

     encrypted_data = f.encrypt(msg)

     with open(fname,"wb")as f:

       f.write(encrypted_data)

  except:

      self.sec_win.destroy()

      self.root.deiconify()

 def decrypt(self):

  try:

    print("de called")

    key=self.load_key()

    f= Fernet(key)

    with open(fname, "rb") as file:

# read the encrypted data

      encrypted_data = file.read()

# decrypt data

      decrypted_data = f.decrypt(encrypted_data)

# write the original file

    with open(fname, "wb") as file:

        file.write(decrypted_data)

        messagebox.showwarning("success","file decrypted")

  except:

   self.flag3+=1

   if self.flag3==1:

     messagebox.showwarning("ERROR","WRONG KEY ENTERED")

     self.flag3=0

 def final(self):

   print("final called")

   if self.vari.get()==1:

     self.encrypt_file()

     if count==1:

       messagebox.showwarning("success","file encrypted")

   elif self.vari.get()==2:

     self.decrypt()

   elif self.vari.get()!=[1-2] :

     self.flag3+=1

     if self.flag3==1:

      messagebox.showwarning("warning","please choose an option")
 
      self.flag3=0

display= Display() 
