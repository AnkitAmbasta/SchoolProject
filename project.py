print(
'''      STUDENTS ACADEMIC PROFILE
           MANAGEMENT SYSTEM
        -devloped by AnkitAmbasta''',"\n",'='*100)
#Connection statement
import mysql.connector  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="1234",
  database="csproject")
#Defining Connection Object
cursor=dataBase.cursor()
print(
'''Enter 1 New records
Enter 2 View all record
Enter 3 Search record
Enter 4 Modify record
Enter 5 Delete record
Enter 6 Exit
''')
#Add Function
def add():
    print('='*100)
    c1=int(input("How many record(s): "))
    for i in range(1,c1+1):
        print("Collecting details: ")
        roll=int(input("Roll_no. : "))
        name=input("Name : ")
        P=float(input("Physics_Score: "))
        C=float(input("Chemistry_Score: "))
        M=float(input("Maths_Score: "))
        E=float(input("English_Score: "))
        Cs=float(input("ComputerScience_Score: "))
        T=(P+C+M+E+Cs)   
        p=(T/500)*100
        #sql
        insert="insert into report(RollNo,Name,Physics,Chemistry,Maths,English,CS,Total,Percentage) values(%s, %s,%s, %s,%s, %s,%s, %s,%s)"
        val = (roll,name,P,C,M,E,Cs,T,p)
        cursor.execute(insert, val)
        dataBase.commit()
        print("Successfully added: ",i," record(s)")
    print("BackToHomeScreen","."*20)
    print('='*100)
#View Function
def view():
    print('='*100)
    print("LoadingData","."*20)
    #sql
    cursor.execute("select * from report")
    data=cursor.fetchall()
    count=cursor.rowcount
    print("Total no. of rows retrieved: ",count)
    L1=['RollNo    ','Name      ','Physics   ','Chemistry ','Maths     ','English   ','C.S       ','Total     ','Percentage']
    for i in range(0,len(data)):
        print('='*100)
        for j in range(0,9):
            print(L1[j],' ',data[i][j])
    print("BackToHomeScreen","."*20)
    print('='*100)
#search Function
def search():
    print('='*100)
    roll=int(input("Enter rollno.: "))
    L1=['RollNo    ','Name      ','Physics   ','Chemistry ','Maths     ','English   ','C.S       ','Total     ','Percentage']
    c=0
    print("Searching","."*20)
    #sql
    cursor.execute("select * from report ")
    data=cursor.fetchall()
    print('='*100)
    for i in range(0,len(data)):
        if data[i][0]==roll:
            for j in range(0,9):
               print(L1[j],' ',data[i][j])
               c=c+1
    if c==0:
            print("No record found",'.'*20)        
    print("BackToHomeScreen","."*20)
    print('='*100)
#Modify Function
def modify():
    print('='*100)
    roll1=int(input("Enter rollno.: "))
    print("Collecting details")
    roll=int(input("Roll_no. : "))
    name=input("Name : ")
    P=int(input("Physics_Score: "))
    C=int(input("Chemistry_Score: "))
    M=int(input("Maths_Score: "))
    E=int(input("English_Score: "))
    Cs=int(input("ComputerScience_Score: "))
    T=(P+C+M+E+Cs)   
    p=(T/500)*100
    #sql
    sql="update report set RollNo=%s,Name=%s,Physics=%s,Chemistry=%s,Maths=%s,English=%s,CS=%s ,Total=%s,Percentage=%s where RollNo=%s"
    val = (roll,name,P,C,M,E,Cs,T,p,roll1)
    cursor.execute(sql,val)
    dataBase.commit()

    print("Successfuly Updated: ","."*20)
    print("BackToHomeScreen","."*20)
    print('='*100)
#Delete Function
def delete():
    print('='*100)
    roll=int(input("Enter rollno.: "))
    data=(roll,)
    #sql
    sql="delete from report where RollNo=%s"
    cursor.execute(sql,data)
    dataBase.commit()
    print("Successfully Deleted","."*20)
    print("BackToHomeScreen","."*20)
    print('='*100)
#____Main_____    
while True :
    choice=int(input("Enter your choice: "))
    if choice==1:
      add()
    elif choice==2:
        view()
    elif choice==3:
        search()
    elif choice==4:
        modify()
    elif choice==5:
        delete()            
    elif choice==6:
        print("Thank You ! Visit Again")
        print("Terminating","."*20)
        exit()
    else :
        print("Please enter a valid choice: ")
#disconnectiing
dataBase.close()
