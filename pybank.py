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
            print("1.check balance 2.deposit 3.withdraw 0.logout\n")
            op2=int(input("Enter option: "))
            if op2==1:
                cur3=mydb.cursor()
                q3="select balance from bank where acc_no=%s"
                cur3.execute(q3,(log_accno,))
                result3=cur3.fetchone()
                print("Current balance: ",result3[0])
            elif op2==2:
                deposit_amount=int(input("Enter amount to deposit: "))
                cur3=mydb.cursor()
                q3="update bank set balance=balance+%s where acc_no=%s"
                cur3.execute(q3,(deposit_amount,log_accno))
                mydb.commit()
            elif op2==3:
                withdraw_amount=int(input("Enter amount to withdraw: "))
                cur3=mydb.cursor()
                q3="select balance from bank where acc_no=%s"
                cur3.execute(q3,(log_accno,))
                result3=cur3.fetchone()
                if result3[0]>=withdraw_amount:
                    q4="update bank set balance=balance-%s where acc_no=%s"
                    cur3.execute(q4,(withdraw_amount,log_accno))
                    mydb.commit()
                else:
                    print("Insufficient balance")
                
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