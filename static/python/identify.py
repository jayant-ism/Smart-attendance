import cv2
import numpy as np
import os
import face_recognition
import json
import pyrebase
config  = {
    "apiKey": "AIzaSyDf0-5WbFoPVvS5pA3Snp5Ww_ViQXfII1g",
    "authDomain": "smart-classroom-b5d31.firebaseapp.com",
    "databaseURL": "https://smart-classroom-b5d31.firebaseio.com",
    "projectId": "smart-classroom-b5d31",
    "storageBucket": "smart-classroom-b5d31.appspot.com",
    "messagingSenderId": "556523240301",
    "appId": "1:556523240301:web:180204e9316a57a7113864",
    "measurementId": "G-P9GCKK59T9"
}




firebase = pyrebase.initialize_app(config)
db = firebase.database()



import pandas as pd


from multiprocess import pool

import csv

out=[]
with open('out.csv', newline='') as f:

    reader = csv.reader(f)
    your_list = list(reader)
   
    
    for li in your_list :
        if li !=[] :
           out.append(li[0])
     
res = out           




h = csv.reader(open('Datadet.csv')) # Here your csv file
lines1 = list(h)
dicti = [] 
    
key=lines1[0]
for li in lines1 :
    if li!=[] and li!=key :
        ra={}
         
        for k in range(0,len(key)) :
            ra[key[k]]=li[k]
        dicti.append(ra)       
        


 
li=[]
    

for  i  in range(0,len(res)) :
    numpy_array = np.genfromtxt("individual/"+str(dicti[i]["reg"])+".csv", delimiter=";", skip_header=0)
    li.append(numpy_array)
       


def Oor(lines1 ,lines2 ) :
    
    for i in range(0,len(lines1)):
        a = lines1[i]
        b = lines2[i]
        if a=='False' and b=='False' :
            a = 'False'
        else :
            a= 'True'    

        lines1[i]=a
    return lines1    
   
   


def savecsv(toCSV) :

    
  

    csv_columns =toCSV[0].keys()     
    csv_file="Datadet.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in toCSV:
                writer.writerow(data)
    except IOError:
        print("I/O error")
        
 

    
   



def regr(ks , camera) :
    if not os.path.exists("data"):
        os.makedirs("data")   # this is the location of pictures of the students , used for backup

    if not os.path.exists("json"):
        os.makedirs("json")   # all json files will be stored here

    direc = "data/"
    cap = cv2.VideoCapture(camera)  #'http://192.168.137.163:4747/mjpegfeed'  it changes every time a connectipn is made


    while True :
        _, frame = cap.read()
     # frame size 
        x1 = int(10) 
        y1 = 10
        x2 = int(frame.shape[1])
        y2 = int(frame.shape[1])

        cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.imshow("Frame", frame)

        interrupt = cv2.waitKey(10)
          
        if  interrupt & 0xFF ==ord('1') :

            try :
                fi = face_recognition.face_encodings(frame)[0]               
                cv2.imwrite(direc +ks+'.jpg', frame)
                cap.release()
                cv2.destroyAllWindows()
                return frame , fi

            except IndexError :
                print("ERROR")    




def resu(frame) :
    global  res
    fi  = face_recognition.face_encodings(frame)
   
   

    
   

    if(len(fi)!=0) :
      
        try :
            for face in fi :
                
                result = face_recognition.compare_faces(li,face)
                print(result)
                res = result
              
                for i in range(0,len(result)) :
                    if result[i]==True :
                        db.child("wards").child(dicti[i]['reg']).child("total_attendance").set("1")
                        db.child("wards").child(dicti[i]['reg']).child("message").set("your ward has reached to the school on time")
                        db.child("wards").child(dicti[i]['reg']).child("name").set(dicti[i]["name"])
                    



             
                
        except    IOError :
            print("sddas")
        pu=[]
        
        
  
    if len(res) == len(dicti) :
        
        with open('out.csv' , 'w' , newline='')  as file :

            writer =  csv.writer(file) 
            
            for p in res:
                s=[]         
                
                s.append(p)

                writer.writerow(s) 
        file.close()        
                     
def update() :
    for i  in range(len(res)) :
        if(res[i]=='False') :
            db.child("wards").child(dicti[i]['reg']).child("total_attendance").set("0")
            db.child("wards").child(dicti[i]['reg']).child("message").set("your ward has not reached to the school ")
                             
      
                     
        
   





 
            



















