from django.shortcuts import render
from .models import student
import csv

import sys
from static.python.web import data ,toatt


# Create your views here.


def sub(request):
    if request.method == "POST" :
        if (request.POST['username'] == 'Jayant')   :
            if (request.POST['pass'] == 'Jayant') :
                val = 1
                return ok(request) 

              
    return render(request ,  'login.html' )  
              

def ok(request) :
    dat=data()
    print("dat")
    print(dat)


    return render(request , 's.html',{'data1':dat,'id':1})
    
def table(request) :
    j = student.objects.all()
    
    return render(request , 'data2.html' , {'j': j ,})
    
def floar(request) :
    return render(request , 'flot.html')
    
def details(request) :
    
    with open('attendance/attendance.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data=[]
        l=[]
        print(csv_reader)
        for row in csv_reader:
            if line_count == 0:
                
                line_count += 1
                for i in row :
                    l.append(i) 
            else:
                
                line_count += 1
                d={}
                for i in range(len(row)) :
                    d.update( { l[i] : row[i] ,} )
                     
                    
                data.append(d)     
        print(data)   


        details = toatt() 
        print("isd") 
        print(details)   
                    
        key = details[0].keys()             



                
   

    return render(request , 'attendance.html' , {'data' : data , 'details':details ,'key':key})
    

    
    
    