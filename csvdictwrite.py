import csv

try:
    #field names

    fields=['Id','Name','Age','Salary']

    #data rows of csv file

    rows=[{'Id':'1','Name':'Ram','Age':'23','Salary':'10000'},
          {'Id':'2','Name':'Rose','Age':'23','Salary':'10000'}]

    #writing into a csv file

    f=open('details1.csv','w',newline='')
    w=csv.DictWriter(f,fieldnames=fields) #creating a csv writer object
    w.writeheader() #writing fields
    w.writerows(rows)
    print("Successfully Inserted")
    
except Exception as ae:
    print(ae)

finally:
    f.close()
