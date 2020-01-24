from django.shortcuts import render
from .models import eta
from  static.python.identify import regr ,savecsv ,resu ,update
from numpy import savetxt 
import pyrebase
import cv2
import numpy as np
import os
import face_recognition
import json
import csv

def start(Httprequest) :
    name = eta.objects.all().values()

    savecsv(name) 
    print(name)
    with open('out.csv' , 'w' , newline='')  as file :
        writer =  csv.writer(file) 
        for n in name:
           
            
            
            writer.writerow(['False']) 
    file.close()        
                  



    


    return render(Httprequest,'for.html' )

    

def server(Httprequest) :
    cap = cv2.VideoCapture(0)  #'http://192.168.137.163:4747/mjpegfeed'  it changes every time a connectipn is made


    while True :
        _, frame = cap.read()
     # frame size 
        x1 = int(10) 
        y1 = 10
        x2 = int(frame.shape[1])
        y2 = int(frame.shape[1])

        cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
        
        cv2.imshow("Frame", frame)

        interrupt = cv2.waitKey(10)
        #resu(frame) 
        resu(frame) 
        if  interrupt & 0xFF ==ord('1') :
            break
      
        


        


        
    cap.release()
    cv2.destroyAllWindows()  
    update()
     


    return render(Httprequest,'for.html' )

    

def index(Httprequest):

    
    return render(Httprequest,'for.html')



def submit(Httprequest):
    
    s = str(Httprequest.POST['name'])
    reg = str(Httprequest.POST['reg'])
    phone = int(Httprequest.POST['phone'])
    cam = 0 
    t , e = regr(s ,cam)
    savetxt('static/csv/' +reg + '.csv',e, delimiter=',')
    
    savetxt('individual/' +reg + '.csv',e, delimiter=',')


   


   
    p = eta(name=s, phone=phone, reg=reg  )
    p.save()

    

    
    return render(Httprequest,'for.html')   



def disp(request) :

    
    return render(request, 'for.html')

def attend(request) :
    
    return render(request, 'for.html')



