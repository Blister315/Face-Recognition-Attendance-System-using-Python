from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",28,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1330,height=35) #height=45

        img_top1=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition system\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top1=img_top1.resize((1300,650),Image.LANCZOS)   #130
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        
        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=0,y=45,width=1300,height=665) #original y=55 height=650

        dev_label=Label(f_lbl,text="Email ID: xyz@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=450,y=180) 
        




if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()