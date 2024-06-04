from tkinter import*
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import csv
import webbrowser
import requests
import json

class Login_System:
    def _init_(self, root):
        self.root=root
        self.root.title=('Login System | ')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='#006400')
        #image
        self.fitur_image=ImageTk.PhotoImage(file='bk2.jpg')
        self.lbl_fitur_image=Label(self.root, image=self.fitur_image, bd=0).place(x=0, y=0, width=1350, height=700)
        self.fitur_image2=ImageTk.PhotoImage(file='bk2.jpg')
        self.lbl_fitur_image2=Label(self.root, image=self.fitur_image, bd=0).place(x=0, y=0, width=1350, height=700)
        #login_frame
        login_frame=Frame(self.root, bd=2, relief=RIDGE, bg='#469536')
        login_frame.place(x=750, y=100,width=350,height=495)

        title=Label(login_frame, text='Login System', font=('Elephant',30,'bold'),bg='#93bf85').place(x=0, y=30, relwidth=1)
        
        lbl_user=Label(login_frame, text='username',font=('Andalus',15),bg='white',fg='#2e6b23').place(x=50,y=100)
        self.username=StringVar()
        self.password=StringVar()
        txt_username=Entry(login_frame,textvariable=self.username, font=('times new roman',15),bg='#2d7121').place(x=50,y=140, width=250)

        lbl_pass=Label(login_frame, text='Alamat',font=('Andalus',15),bg='white',fg='#767171').place(x=50,y=180)
        txt_pass=Entry(login_frame,textvariable=self.password, font=('times new roman',15),bg='#2d7121').place(x=50,y=220, width=250)

        btn_login=Button(login_frame,command=self.fitur,text='Submit',font=('Arial Rounded MT Bold',15),bg='#93bf85',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=50,y=300, width=250,height=35)
        btn_login = open('Username And Address.csv', 'a')
        btn_login.write('Username : '+self.username.get()+'\n')
        btn_login.write('Alamat : '+self.password.get()+'\n')

        
        #animation
        self.im1=ImageTk.PhotoImage(file='bd.jpg')
        self.im2=ImageTk.PhotoImage(file='bf.jpg')
        self.im3=ImageTk.PhotoImage(file='bg.jpg')

        self.lbl_change_image=Label(self.root,bg='white')
        self.lbl_change_image.place(x=400, y=280, width=300, height=200)

        self.animation()

    def animation(self):
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im1
        self.lbl_change_image.config(image=self.im1)
        self.lbl_change_image.after(2000,self.animation)

    def sign_up(self):
        login_frame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        login_frame.place(x=750, y=100,width=350,height=460)

        title=Label(login_frame, text='Register System', font=('Elephant',30,'bold'),bg='green').place(x=0, y=30, relwidth=1)
        
        lbl_user=Label(login_frame, text='username',font=('Andalus',15),bg='white',fg='#767171').place(x=50,y=100)
        self.username=StringVar()
        self.password=StringVar()
        txt_username=Entry(login_frame,textvariable=self.username, font=('times new roman',15),bg='#2d7121').place(x=50,y=140, width=250)

        lbl_pass=Label(login_frame, text='password',font=('Andalus',15),bg='white',fg='#767171').place(x=50,y=180)
        txt_pass=Entry(login_frame,textvariable=self.password,show='*', font=('times new roman',15),bg='#2d7121').place(x=50,y=220, width=250)
    
        lbl_repeat=Label(login_frame, text='repeat password',font=('Andalus',15),bg='white',fg='#767171').place(x=50,y=260)
        txt_repeat=Entry(login_frame,textvariable=self.password,show='*', font=('times new roman',15),bg='#2d7121').place(x=50,y=300, width=250)

        btn_login=Button(login_frame,command=self.login,text='Sign Up',font=('Arial Rounded MT Bold',15),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=50,y=360, width=250,height=35)
    
        file_csv = open('Username.csv','a')
        file_csv.write(txt_username.get()+','+txt_pass.get()+'\n')

    def fitur(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='#93bf85')
         fitur_frame.place(x=0,y=0)

         self.fitur_image=ImageTk.PhotoImage(file='bs.jpg')
         self.lbl_fitur_image=Label(self.root, image=self.fitur_image, bd=0).place(x=600, y=450)

         btn_daftar_bank_sampah=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Daftar Bank Sampah', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=70, width=500,height=50)

         btn_jenis_sampah=Button(fitur_frame,command=self.fitur_jenis_sampah, text='Jenis Sampah',font=('times new roman',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=150, width=500,height=50)
         
         btn_cari_lokasi=Button(fitur_frame,command=self.cari_lokasi, text='Pencarian Lokasi',font=('times new roman',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=230, width=500,height=50)

    def fitur_Daftar_bank_sampah(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='#93bf85')
         fitur_frame.place(x=0,y=0)

         btn_bank1=Button(fitur_frame,command=self.gambar_bank1, text='Bank Sampah Kampung Dinoyo', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=100,y=70, width=500,height=50)
         btn_bank2=Button(fitur_frame,command=self.gambar_bank2, text='Bank Sampah Sejahter Hang Tuah', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=100,y=120, width=500,height=50)
         btn_bank3=Button(fitur_frame,command=self.gambar_bank3, text='Bank Sampah Moro Ijo', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=100,y=170, width=500,height=50)
         btn_bank4=Button(fitur_frame,command=self.gambar_bank4, text='Bank Sampah Twebar', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=100,y=220, width=500,height=50)
         btn_bank5=Button(fitur_frame,command=self.gambar_bank5, text='Bank Sampah Makmur 5 Surabaya', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=100,y=270, width=500,height=50)
         btn_bank6=Button(fitur_frame,command=self.gambar_bank6, text='Bank Sampah Bintang', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=100,y=320, width=500,height=50)
         btn_bank7=Button(fitur_frame,command=self.gambar_bank7, text='Bank Sampah Mandiri', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=100,y=370, width=500,height=50)
         btn_bank8=Button(fitur_frame,command=self.gambar_bank8, text='Bank Sampah Sido Makmur', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=100,y=420, width=500,height=50)
         btn_bank9=Button(fitur_frame,command=self.gambar_bank9, text='Bank Sampah Guyub Sayekti', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=700,y=70, width=500,height=50)
         btn_bank10=Button(fitur_frame,command=self.gambar_bank10, text='Bank Sampah Lestari', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=700,y=120, width=500,height=50)
         btn_bank11=Button(fitur_frame,command=self.gambar_bank11, text='Bank Sampah Anggrek', font=('times new roamn',14),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=700,y=170, width=500,height=50)
         btn_bank12=Button(fitur_frame,command=self.gambar_bank12, text='Bank Sampah GKS', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=700,y=220, width=500,height=50)
         btn_bank13=Button(fitur_frame,command=self.gambar_bank13, text='Bank Sampah Jambangan Pintu', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=700,y=270, width=500,height=50)
         btn_bank14=Button(fitur_frame,command=self.gambar_bank14, text='Bank Sampah Mulyorejo', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=700,y=320, width=500,height=50)
         btn_bank15=Button(fitur_frame,command=self.gambar_bank15, text='Bank Sampah Mekar Jaya', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=700,y=370, width=500,height=50)
         btn_bank16=Button(fitur_frame,command=self.gambar_bank16, text='Bank Sampah Induk Surabaya', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=700,y=420, width=500,height=50)
         btn_back1=Button(fitur_frame,command=self.fitur, text='Back', font=('times new roamn',14),bg='#006400',activebackground='#296329',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=630, width=500,height=50)

    def gambar_bank1(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='green')
         fitur_frame.place(x=0,y=0)

         btn_back1=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Back', font=('times new roamn',14),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=630, width=500,height=50)

         lbl_pass=Label(fitur_frame, text='Nama Bank : Bank Sampah Kampung Dinoyo',font=('Andalus',15),bg='green',fg='black').place(x=50,y=20)
         lbl_pass=Label(fitur_frame, text='Alamat : Jl. Dinoyo Tengah No.32, RT.002/RW.03, Keputran, Kec. Tegalsari, Kota SBY, Jawa Timur 60265',font=('Andalus',15),bg='green',fg='black').place(x=50,y=60)
         lbl_pass=Label(fitur_frame, text='Telephone : 0811-3046-595',font=('Andalus',15),bg='green',fg='black').place(x=50,y=100)
     

    def gambar_bank2(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='green')
         fitur_frame.place(x=0,y=0)
         
         btn_back1=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Back', font=('times new roamn',14),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=630, width=500,height=50)
         lbl_pass=Label(fitur_frame, text='Nama Bank : Bank Sampah Sejahtera Hang Tuah',font=('Andalus',15),bg='green',fg='black').place(x=50,y=20)
         lbl_pass=Label(fitur_frame, text='Alamat : Jl, Komp. Hangtuah blok D-17, Ujung, Kec. Semampir, Kota SBY, Jawa Timur',font=('Andalus',15),bg='green',fg='black').place(x=50,y=60)
         lbl_pass=Label(fitur_frame, text='Telephone : 085231715915',font=('Andalus',15),bg='green',fg='black').place(x=50,y=100)
    def gambar_bank3(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='green')
         fitur_frame.place(x=0,y=0)

         self.fitur_image=ImageTk.PhotoImage(file='bs.jpg')
         self.lbl_fitur_image=Label(self.root, image=self.fitur_image, bd=0).place(x=600, y=100)
         
         btn_back1=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Back', font=('times new roamn',14),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=630, width=500,height=50)
         lbl_pass=Label(fitur_frame, text='Nama Bank : Bank Sampah Moro Ijo ',font=('Andalus',15),bg='green',fg='black').place(x=50,y=20)
         lbl_pass=Label(fitur_frame, text='Alamat : Jl. Mojo Klanggru Lor, Mojo, no68e, Kota SBY, Jawa Timur',font=('Andalus',15),bg='green',fg='black').place(x=50,y=60)
         lbl_pass=Label(fitur_frame, text='Telephone : 081321112693 ',font=('Andalus',15),bg='green',fg='black').place(x=50,y=100)
    def gambar_bank4(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='green')
         fitur_frame.place(x=0,y=0)

         self.fitur_image=ImageTk.PhotoImage(file='bs.jpg')
         self.lbl_fitur_image=Label(self.root, image=self.fitur_image, bd=0).place(x=600, y=100)
         
         btn_back1=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Back', font=('times new roamn',14),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=630, width=500,height=50)
         lbl_pass=Label(fitur_frame, text='Nama Bank : Bank Sampah Twebar',font=('Andalus',15),bg='green',fg='black').place(x=50,y=20)
         lbl_pass=Label(fitur_frame, text='Alamat : Jl. Tambak Wedi Barat No.6 no.40, Tambak Wedi, Kec. Kenjeran, Kota SBY, Jawa Timur',font=('Andalus',15),bg='green',fg='black').place(x=50,y=60)
         lbl_pass=Label(fitur_frame, text='Telephone : 081332788989',font=('Andalus',15),bg='green',fg='black').place(x=50,y=100)    
    def gambar_bank5(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='green')
         fitur_frame.place(x=0,y=0)

         self.fitur_image=ImageTk.PhotoImage(file='bs.jpg')
         self.lbl_fitur_image=Label(self.root, image=self.fitur_image, bd=0).place(x=600, y=100)
         
         btn_back1=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Back', font=('times new roamn',14),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=630, width=500,height=50)
         lbl_pass=Label(fitur_frame, text='Nama Bank : Bank Sampah makmur 5 Surabaya',font=('Andalus',15),bg='green',fg='black').place(x=50,y=20)
         lbl_pass=Label(fitur_frame, text='Alamat : Jl. Demak Timur V No.5, Gundih, Kec. Bubutan, Kota SBY, Jawa Timur',font=('Andalus',15),bg='green',fg='black').place(x=50,y=60)
         lbl_pass=Label(fitur_frame, text='Telephone : 082141669033',font=('Andalus',15),bg='green',fg='black').place(x=50,y=100)   
    def gambar_bank6(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='green')
         fitur_frame.place(x=0,y=0)

         self.fitur_image=ImageTk.PhotoImage(file='bs.jpg')
         self.lbl_fitur_image=Label(self.root, image=self.fitur_image, bd=0).place(x=600, y=100)
         
         btn_back1=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Back', font=('times new roamn',14),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=630, width=500,height=50)
         lbl_pass=Label(fitur_frame, text='Nama Bank : Bank Sampah Bintang',font=('Andalus',15),bg='green',fg='black').place(x=50,y=20)
         lbl_pass=Label(fitur_frame, text='Alamat : Jl. Kapasan Kidul Kapasan Lor No.1, RT.001/RW.03, Kapasan, Kec. Simokerto, Kota SBY, Jawa Timur',font=('Andalus',15),bg='green',fg='black').place(x=50,y=60)
         lbl_pass=Label(fitur_frame, text='Telephone : 085100162694',font=('Andalus',15),bg='green',fg='black').place(x=50,y=100)
    def gambar_bank7(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='green')
         fitur_frame.place(x=0,y=0)

         self.fitur_image=ImageTk.PhotoImage(file='bs.jpg')
         self.lbl_fitur_image=Label(self.root, image=self.fitur_image, bd=0).place(x=600, y=100)
         
         btn_back1=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Back', font=('times new roamn',14),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=630, width=500,height=50)
         lbl_pass=Label(fitur_frame, text='Nama Bank : Bank Sampah Mandiri',font=('Andalus',15),bg='green',fg='black').place(x=50,y=20)
         lbl_pass=Label(fitur_frame, text='Alamat : Jl Kalongan V no 1, RT.3/RW.6, Krembangan Sel., Kec. Krembangan, Kota SBY, Jawa Timur',font=('Andalus',15),bg='green',fg='black').place(x=50,y=60)
         lbl_pass=Label(fitur_frame, text='Telephone : 081331108012',font=('Andalus',15),bg='green',fg='black').place(x=50,y=100)
    def gambar_bank8(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='green')
         fitur_frame.place(x=0,y=0)

         self.fitur_image=ImageTk.PhotoImage(file='bs.jpg')
         self.lbl_fitur_image=Label(self.root, image=self.fitur_image, bd=0).place(x=600, y=100)
         
         btn_back1=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Back', font=('times new roamn',14),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=630, width=500,height=50)
         lbl_pass=Label(fitur_frame, text='Nama Bank : Bank Sampah Sido Makmur',font=('Andalus',15),bg='green',fg='black').place(x=50,y=20)
         lbl_pass=Label(fitur_frame, text='Alamat : Jl. Sidosermo III No.10, Sidosermo, Kec. Wonocolo, Kota SBY, Jawa Timur 60239',font=('Andalus',15),bg='green',fg='black').place(x=50,y=60)
         lbl_pass=Label(fitur_frame, text='Telephone : 085707697317',font=('Andalus',15),bg='green',fg='black').place(x=50,y=100)
    def gambar_bank9(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='green')
         fitur_frame.place(x=0,y=0)

         self.fitur_image=ImageTk.PhotoImage(file='bs.jpg')
         self.lbl_fitur_image=Label(self.root, image=self.fitur_image, bd=0).place(x=600, y=100)
         
         btn_back1=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Back', font=('times new roamn',14),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=630, width=500,height=50)
         lbl_pass=Label(fitur_frame, text='Nama Bank : Bank Sampah Guyub Sayekti',font=('Andalus',15),bg='green',fg='black').place(x=50,y=20)
         lbl_pass=Label(fitur_frame, text='Alamat : Jl. Ngagel Mulyo VI No.11-17, Ngagelrejo, Kec. Wonokromo, Kota SBY, Jawa Timur 60245',font=('Andalus',15),bg='green',fg='black').place(x=50,y=60)
         lbl_pass=Label(fitur_frame, text='Telephone : -',font=('Andalus',15),bg='green',fg='black').place(x=50,y=100)
    def gambar_bank10(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='green')
         fitur_frame.place(x=0,y=0)

         self.fitur_image=ImageTk.PhotoImage(file='bs.jpg')
         self.lbl_fitur_image=Label(self.root, image=self.fitur_image, bd=0).place(x=600, y=100)
         
         btn_back1=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Back', font=('times new roamn',14),bg='#006400',activebackground='#006400',fg='white',activeforeground='white',cursor='hand2').place(x=450,y=630, width=500,height=50)
         lbl_pass=Label(fitur_frame, text='Nama Bank : Bank Sampah Lestari',font=('Andalus',15),bg='green',fg='black').place(x=50,y=20)
         lbl_pass=Label(fitur_frame, text='Alamat :QQ63+WPQ, RW VII, Simokerto, Kec. Simokerto, Kota SBY, Jawa Timur 60143',font=('Andalus',15),bg='green',fg='black').place(x=50,y=60)
         lbl_pass=Label(fitur_frame, text='Telephone : 0312345576',font=('Andalus',15),bg='green',fg='black').place(x=50,y=100)
    def gambar_bank11(self):
         fitur_frame=Frame(self.root,width=1400, height=850, bg='green')
         fitur_frame.place(x=0,y=0)

         self.fitur_image=ImageTk.PhotoImage(file='bs.jpg')
         self.lbl_fitur_image=Label(self.root, image=self.fitur_image, bd=0).place(x=600, y=100)
         
         btn_back1=Button(fitur_frame,command=self.fitur_Daftar_bank_sampah, text='Back', font=('times new roamn',14),bg='#296329',activebackground='#006400',fg='white',activeforeground='white',cursor='han