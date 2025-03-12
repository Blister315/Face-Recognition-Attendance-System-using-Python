from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",28,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1330,height=35) #height=45

        img_top1=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition system\college_images\dev.jpg")
        img_top1=img_top1.resize((1300,650),Image.LANCZOS)   #130
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        
        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=0,y=45,width=1300,height=665) #original y=55 height=650



        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=900,y=10,width=370,height=450) #600 y=55



        #Developer info
        dev_label=Label(main_frame,text="Developed By:",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5) 
        
        dev_label1=Label(main_frame,text="Harshit",font=("times new roman",20,"bold"),bg="white")
        dev_label1.place(x=0,y=40) 



       





if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()