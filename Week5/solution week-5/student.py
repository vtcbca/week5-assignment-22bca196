attribute=['sid','sname','city','contect']
records=[[1,'om','surat',6598741235],
         [2,'sai','bardoli',8965231475],
         [3,'ram','vyara',8965324589],
         [4,'gopal','tapi',9874563215],
         [5,'kishan','bajipura',8745632985]]
li=[]
for i in range(5):
    sid=int(input("Enter Student Id:"))
    sname=input("Enter Student Name:")
    city=input("Enter Student's City:")
    contect=int(input("Enter Student Contect Number:"))
    l=[sid,sname,city,contect]
    li.append(l)
import csv
with open('student.csv','w',newline='')as csvfile:
    file=csv.writer(csvfile)
    file.writerow(attribute)
    file.writerows(records)
    file.writerows(li)

import csv
with open('student.csv','r')as read_obj:
    all_records=csv.reader(read_obj)
    for records in all_records:
        print(records)
