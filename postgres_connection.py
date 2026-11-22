import psycopg2

con=psycopg2.connect(
    host="localhost",
    database="Bank_DB",
    user="postgres",
    password="vrushali123",
    port="5432"
    
)
cursor=con.cursor()

def create_account():
    name=input("Enter Name:")
    phone=input("Enter phone:")
    address=input("Ente the address:")
    balance=float(input("Enter the initial deposit:"))

    query=""" INSERT INTO accounts (name,phone,address,balance)
      values(%s,%s,%s,%s) """

    cursor.execute(
        query,(name,phone,address,balance)

    )
    con.commit()
    print("Account created successfully")

# create_account()
def view_account():
    account_no=int(input("Enter the account number:"))

    query=""" SELECT * from accounts where account_no=%s"""
    cursor.execute(query,(account_no,))
    data=cursor.fetchone()

    if data:
        print("Account number:",data[0])
        print("Name:",data[1])
        print("Phone:",data[2])
        print("Address:",data[3])
        print("Balance:",data[4])
    else:
        print("account not found")

# view_account()      
def deposit_money():
     account_no=int(input("Enter the account number:"))
     amount=float(input("Enter the deposit:"))

     query=""" 
     UPDATE accounts
     SET balance=balance + %s 
     WHERE account_no= %s """

     cursor.execute(
        query,(amount,account_no,)
     )
     con.commit()

     if cursor.rowcount>0:
        print("money deposited successfully")
     else:
        print("account not found...")

# deposit_money()
def withdraw_money():
     account_no=int(input("Enter the account number:"))
     amount=float(input("Enter the withdraw:"))

     query=""" 
     SELECT balance 
     from accounts 
     where account_no=%s"""

     cursor.execute(query,(account_no,))

     data=cursor.fetchone()

     if not data:
         print("Account not found")

     balance=data[0]

     if (amount>balance):
         print("Insufficeient balance ")
         return

     query=""" 
     UPDATE accounts 
     SET balance=balance - %s
     WHERE account_no=%s"""

     cursor.execute(
            query,(amount,account_no,)
         )
     con.commit()
     print("Money withdraw successfully")

# withdraw_money()

def check_balance():
    account_no=int(input("Enter the account number:"))
    query=""" 
       SELECT balance 
       from accounts 
       where account_no=%s"""  
    
    cursor.execute(query,(account_no,))
    data=cursor.fetchone()

    if data:
        print("current balance:",data[0])
    else:
        print("Account not found")

# check_balance()

def delete_account():
     account_no=int(input("Enter the account number:"))

     query=""" delete from accounts
     where account_no=%s"""

     cursor.execute(query,(account_no,))
     con.commit()
     if(cursor.rowcount>0):
         print("account deleted successfully")
     else:
         print("account not found")

# delete_account() 
 
       
def transfer_money():
     sender=int(input("Enter sender account number:"))
     receiver=int(input("Enter receiver account number:"))
     amount=float(input("Enter the transfer amount:"))

     if amount<=0:
        print("Transfer amount must be greter than zero")
        return
     
     if sender==receiver:
           print("Cannot tansfer money to same account")
           return
    # Deduct money from sender account

     query1="""
         UPDATE accounts
         SET balance=balance-%s
         WHERE account_no=%s
         AND balance>=%s
         """
     cursor.execute(query1,(amount,sender,amount))
     if cursor.rowcount==0:
           con.rollback()
           print("Sender account not found or insufficient balance")
           return

    # Add money to receiver account

     query2="""
         UPDATE accounts
         SET balance=balance + %s
         WHERE account_no=%s
         """

     cursor.execute(query2,(amount,receiver))
     if cursor.rowcount==0:
           con.rollback()
           print("Receiver account not found")
           return
    
           
     con.commit()
     print("Money transferred successfully!")


transfer_money()
           
while True:
    print("========BANK MANAGEMENT SYSTEM========")

    print("1.create account")
    print("2.view account")
    print("3.deposit money")
    print("4.withdraw money")
    print("5.check balance")
    print("6.delete account")
    print("7.transfer money")
    print("8.Exit")
    choice=input("Enter the choice:")

    if choice=="1":
        create_account()
    elif choice=="2":
        view_account()
    elif choice=="3":
        deposit_money()
    elif choice=="4":
        withdraw_money()
    elif choice=="5":
        check_balance()
    elif choice=="6":
        delete_account()
    elif choice=="7":
        transfer_money()
        break
    elif choice=="8":
            print("Thank You!!!")
    else:
        ("Invalid choice")
        


        


    
       
       
       
       

    


