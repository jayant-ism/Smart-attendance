import cv2
import numpy as np
import os
import face_recognition
import json

from multiprocess import pool

import csv

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

def resu(frame ) :
    
     with open('Datadet.csv', 'r', encoding='utf-8') as csvfile:
                #sniff to find the format
                fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
                csvfile.seek(0)
                #create a CSV reader
                myReader = csv.reader(csvfile, dialect=fileDialect)
                #read each row
                print(myReader)








