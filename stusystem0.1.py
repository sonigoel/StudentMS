import MySQLdb
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import os

db=MySQLdb.connect('localhost','root','admin123','stu')
#print('db= ',db)
cur=db.cursor()
#print('cur: ',cur)
print("\n   WELCOME TO STUDENT INFORMATION SYSTEM ")


#cur.execute("DROP table if exists records_table,marks_table")
#cur.execute(''' create table records_table(
 #                ID INT(5) PRIMARY KEY  NOT NULL ,
 #                NAME VARCHAR(20),
 #                PHONE_NO INT(12),
  #               ADDRESS VARCHAR(30),
  #               GENDER CHAR);
 #            ''')
#cur.execute(''' insert into records_table values (1,'simi',416234634,'12taysham','F'),
 #                                        (2,'ravi',416234987,'25eglinton','M' );''')
#cur.execute('''create table marks_table(
  #                     ID INT(5) ,
  #                     MATH INT(2),
  #                     SCIENCE INT(2),
  #                     ENGLISH INT(2),
  #                     TOTAL INT(3),
  #                     PER INT(4),
  #                     GRADE CHAR );
  #           ''')
#cur.execute('''insert into marks_table values (1,85,80,90,255,85,'B'),
  #                                       (2,75,82,68,225,75,'C');''')
#db.commit()


while True:
    print('''
         1.create student record
         2.read the record
         3.update record
         4.delete student record''')
    try: 
        inp = int(input("Please Select from Above Options 1-4: "))
    except ValueError:
        print("You have entered incorrect option!!!")
        exit()

    if inp==1 :   #create new record
        ans=input("\nDo you want to create a new student record or you want to exit- Press y to create a record: ")
        if ans=='y':
            name_of_stu=input("\nEnter name:")
            id_of_stu=input("Enter id:")
            #print(name_of_stu,"        ",id_of_stu)
            phoneno_of_stu=input("Enter your phone number:")
            address_of_stu=input("Enter your adress: ")
            gender_of_stu=input("Enter your Gender M or F: ")
            sql1 ="INSERT into records_table(ID,NAME,PHONE_NO,ADDRESS,GENDER) VALUES ("+id_of_stu+","+"'"+name_of_stu+"'"+","+phoneno_of_stu+","+"'"+address_of_stu+"'"+","+"'"+gender_of_stu+"'"+");"
            #print(sql1)
            cur.execute(sql1)
            math_marks=input("Enter math marks :")
            science_marks=input("Enter science marks:")
            english_marks=input("Enter english marks:")
            sql2="INSERT into marks_table(ID,MATH,SCIENCE,ENGLISH) VALUES ("+id_of_stu+","+math_marks+","+science_marks+","+english_marks+");"
            #print(sql2)
            cur.execute(sql2)
            print("\nStudent with Name {} and ID {} is successfully added".format(name_of_stu,id_of_stu))
            db.commit()
        else:
            break

    elif inp==2:  #read a specific records
        id_of_stu=input("\nEnter the id if student whose information you need: ")
        sql1="SELECT records_table.ID,records_table.NAME,records_table.PHONE_NO,records_table.ADDRESS,records_table.GENDER,marks_table.MATH,marks_table.SCIENCE,marks_table.ENGLISH,marks_table.total,marks_table.PER,marks_table.GRADE FROM records_table JOIN marks_table ON records_table.ID=marks_table.ID AND records_table.ID="+id_of_stu+";"
        cur.execute(sql1)
        print("\nRecord is :")
        print(cur.fetchall())
        #print(sql1)
        #no_of_rows=cur.execute(sql1)
        #print(no_of_rows)
        #for i in range (no_of_rows):
        #    print(record[i])

    elif (inp==3):  #update record
        id_of_stu=input("\nEnter id of the student whose record you want to update:\n")

        sql1="SELECT records_table.ID,records_table.NAME,records_table.PHONE_NO,records_table.ADDRESS,records_table.GENDER,marks_table.MATH,marks_table.SCIENCE,marks_table.ENGLISH,marks_table.TOTAL,marks_table.PER,marks_table.GRADE FROM records_table JOIN marks_table ON records_table.ID=marks_table.ID AND records_table.ID="+id_of_stu+";"
        print(sql1)
        cur.execute(sql1)
        print(cur.fetchall())
        ans=input("\nEnter the name of field you want to update:")
        new=input("Enter new value of the field {}:".format(ans))
        print("ans:", type(ans))
        print("new:", new)
        if (ans == 'NAME' or ans == 'ADDRESS' or ans == 'GENDER'):
            print("hello")
            sql2 = "UPDATE records_table SET "+ans+"="+"'"+new+"'"+" WHERE ID="+id_of_stu+";"
        else:
            sql2 = "UPDATE records_table SET "+ans+"="+new+" WHERE ID="+id_of_stu+";"
        print(sql2)
        cur.execute(sql2)
        #if ( ans == 'MATH' or 'SCIENCE' or 'ENGLISH'):
        #    sql3="UPDATE marks_table SET"+ ans+"="+new+" WHERE ID="+id_of_stu+";"
         #   cur.execute(sql3)
        db.commit()

        db.commit()
        print("\n Record is successfully updated ")
    elif (inp==4): #delete record
        id_of_stu=input("\nEnter id of student you want to delete: ")
        sql1="DELETE from records_table WHERE ID= " +id_of_stu +" ;"
        sql2="DELETE from marks_table WHERE ID="+id_of_stu+";"
        #print(sql1)
        #print(sql2)
        cur.execute(sql1)
        cur.execute(sql2)
        print("\nStudent with id {} is successfully removed from the list".format(id_of_stu))
        db.commit()

    else:
        print("\nWrong option, Try again!!!\n")
    choice=input("\nDo you want to coninue: Press y for YES and n for NO: ")
    if choice==('y' or 'Y'):
        continue
    else:
        break
db.close()


