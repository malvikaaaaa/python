import csv

try:
    #field names

    fields=['Id','Name','Age','Salary']

    #data rows of csv file

    rows=[['1','Malu','23','10000'],['2','Rose','23','10000']]

    #writing into a csv file

    f=open('details.csv','w',newline='')
    w=csv.writer(f) #creating a csv writer object
    w.writerow(fields) #writing fields
    w.writerows(rows)
    print("Successfully Inserted")
    
except exception as ae:
    print(ae)

finally:
    f.close()
