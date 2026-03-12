import mysql.connector as m
mydb=m.connect(host="localhost",user="root", password="root", database="project")
def create_ac():
    name = input("enter name:")
    email=input("enter email:")
    phone = int(input("enter phone no:"))
    address = input("enter address:")
    aadhar=int(input("enter aadhar: "))
    pin=int(input("Entert pin:"))
    balance=int(input("Enter balance:"))
    cur1=mydb.cursor()
    q1="insert into bank (name, email, phone, address,aadhar,pin,balance) values(%s,%s,%s,%s,%s,%s,%s)"
    values=[name,email,phone,address,aadhar,pin,balance]
    cur1.execute(q1,values)
    mydb.commit()
    print("Account created successfully")
def login():
    log_accno=input("Enter account number: ")
    cur2=mydb.cursor()
    q2="select pin from bank where acc_no=%s"
    cur2.execute(q2,(log_accno,))
    result2=cur2.fetchone()
    if result2:
        log_pin=int(input("Enter pin: "))
        if result2[0]==log_pin:
            print("Login successfull")
            
        else:
            print("Login fail! incorrect pin")
    else:
        print("Account does'nt exist")
exit=False
while exit==False:
    print("1.create account 2.login 0.exit\n")
    op=int(input("Enter option: "))
    if op==1:
        create_ac()
    elif op==2:
        login()
    elif op==0:
        exit=True
print("Exited!!")