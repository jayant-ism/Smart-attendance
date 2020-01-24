
import csv






def data():
    print("s")

    out=[]
    with open('out.csv', newline='') as f:

        reader = csv.reader(f)
        your_list = list(reader)
        print(your_list)
    
        for li in your_list :
            if li !=[] :
                out.append(li[0])
        print(out)  
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

    print(dicti)        
    out = dicti[0]
    out['attend'] = res[0]        
    
   
    return out      




def  toatt() :
    h = csv.reader(open('demo_data.csv')) # Here your csv file    
    lines1 = list(h)
    dicti = [] 
    
    key=lines1[0]
    for li in lines1 :
        if li!=[] and li!=key :
            ra={}
         
            for k in range(0,len(key)) :
                ra[key[k]]=li[k]
            dicti.append(ra) 

    print(dicti) 
    return dicti




        


 
  
